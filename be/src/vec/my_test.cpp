#define BE_TEST 1

#include <assert.h>

#include <filesystem>
#include <iostream>
#include <string>
#include <vector>

#include "common/config.h"
#include "common/object_pool.h"
#include "exec/exec_node.h"
#include "gen_cpp/Descriptors_types.h"
#include "gen_cpp/PlanNodes_types.h"
#include "io/fs/file_writer.h"
#include "io/fs/local_file_system.h"
#include "runtime/descriptors.h"
// #include "runtime/mem/mem_tracker.h"
#include "runtime/runtime_state.h"
#include "util/disk_info.h"
#include "vec/core/block.h"
#include "vec/exec/scan/new_file_scan_node.h"
#include "vec/exec/scan/vfile_scanner.h"
#include "vec/exec/scan/split_source_connector.h"

namespace doris::vectorized {

// A mock SplitSourceConnector to provide file scan ranges.
class TestSplitSourceConnector : public SplitSourceConnector {
public:
    TestSplitSourceConnector(const TFileScanRange& scan_range) : _scan_range(scan_range) {}

    Status get_next(bool* has_next, TFileRangeDesc* range) override {
        std::lock_guard<std::mutex> l(_range_lock);
        if (_range_index < _scan_range.ranges.size()) {
            *has_next = true;
            *range = _scan_range.ranges[_range_index++];
        } else {
            *has_next = false;
        }
        return Status::OK();
    }

    int num_scan_ranges() override { return _scan_range.ranges.size(); }
    TFileScanRangeParams* get_params() override { return &_scan_range.params; }

private:
    std::mutex _range_lock;
    TFileScanRange _scan_range;
    int _range_index = 0;
};

class FileScanNodeTest {
public:
    FileScanNodeTest() : _runtime_state(TQueryGlobals()) {
        // Basic setup
        _env = ExecEnv::GetInstance();
        _test_dir = "/tmp/file_scan_node_test_" + std::to_string(time(nullptr));
    }

    ~FileScanNodeTest() {
        if (std::filesystem::exists(_test_dir)) {
            std::filesystem::remove_all(_test_dir);
        }
    }

    void setup() {
        // 1. Create test directory and a CSV file
        std::filesystem::create_directory(_test_dir);
        _test_file_path = _test_dir + "/test.csv";
        io::FileWriterPtr file_writer;
        auto st = io::global_local_filesystem()->create_file(_test_file_path, &file_writer);
        assert(st.ok());

        // Write 3x3 CSV data
        const char* csv_data = R"("col1_row1","col2_row1","col3_row1"
                               ""col1_row2","col2_row2","col3_row2"
                               ""col1_row3","col2_row3","col3_row3")";
        st = file_writer->append(csv_data);
        assert(st.ok());
        st = file_writer->close();
        assert(st.ok());

        // 2. Initialize RuntimeState and DescriptorTbl
        init_desc_table();
        st = _runtime_state.init(_unique_id, _query_options, _query_globals, _env);
        assert(st.ok());
        _runtime_state.set_desc_tbl(_desc_tbl);

        // 3. Configure the FileScanNode
        _tnode.node_id = 0;
        _tnode.node_type = TPlanNodeType::FILE_SCAN_NODE;
        _tnode.num_children = 0;
        _tnode.limit = -1;
        _tnode.row_tuples.push_back(0);
        _tnode.nullable_tuples.push_back(false);
        _tnode.file_scan_node.tuple_id = 0;
        _tnode.__isset.file_scan_node = true;

        _scan_node = std::make_unique<NewFileScanNode>(&_obj_pool, _tnode, *_desc_tbl);

        // 4. Set up the scan range to point to our CSV file
        TFileRangeDesc range_desc;
        range_desc.path = _test_file_path;
        range_desc.start_offset = 0;
        range_desc.size = std::filesystem::file_size(_test_file_path);

        _scan_range.ranges.push_back(range_desc);
        _scan_range.params.format_type = TFileFormatType::FORMAT_CSV_PLAIN;
        // _scan_range.params.column_separator = ",";
        // _scan_range.params.row_delimiter = "\n";
        _scan_range.__isset.params = true;

        // 5. Prepare the scan node
        st = _scan_node->init(_tnode, &_runtime_state);
        assert(st.ok());
        st = _scan_node->prepare(&_runtime_state);
        assert(st.ok());

        auto _kv_cache = std::make_shared<ShardedKVCache>(48);
        auto _profile = _runtime_state.runtime_profile();

        auto split_source = std::make_shared<TestSplitSourceConnector>(_scan_range);
        // _scan_node->set_split_source(split_source.get());
        auto scanner = std::make_shared<VFileScanner>(&_runtime_state, _scan_node.get(), -1, split_source,
                                                 _profile, _kv_cache.get());
        // scanner->_is_load = false;
        vectorized::VExprContextSPtrs _conjuncts;
        std::unordered_map<std::string, ColumnValueRangeType> _colname_to_value_range;
        std::unordered_map<std::string, int> _colname_to_slot_id;
        WARN_IF_ERROR(scanner->prepare(_conjuncts, &_colname_to_value_range, &_colname_to_slot_id),
                      "fail to prepare scanner");
        
// -void VWalScannerTest::generate_scanner(std::shared_ptr<VFileScanner>& scanner) {
// -    auto split_source = std::make_shared<TestSplitSourceConnector>(_scan_range);
// -    scanner = std::make_shared<VFileScanner>(&_runtime_state, _scan_node.get(), -1, split_source,
// -                                             _profile, _kv_cache.get());
// -    scanner->_is_load = false;
// -    vectorized::VExprContextSPtrs _conjuncts;
// -    std::unordered_map<std::string, ColumnValueRangeType> _colname_to_value_range;
// -    std::unordered_map<std::string, int> _colname_to_slot_id;
// -    WARN_IF_ERROR(scanner->prepare(_conjuncts, &_colname_to_value_range, &_colname_to_slot_id),
// -                  "fail to prepare scanner");
// -}

    }

    void run_test() {
        std::cout << "--- Starting FileScanNode Test ---" << std::endl;
        setup();

        // Open the scanner
        auto st = _scan_node->open(&_runtime_state);
        assert(st.ok());

        // Get data blocks
        Block block;
        bool eof = false;
        int total_rows = 0;

        while (!eof) {
            st = _scan_node->get_next(&_runtime_state, &block, &eof);
            assert(st.ok());
            if (block.rows() > 0) {
                std::cout << "Read " << block.rows() << " rows." << std::endl;
                total_rows += block.rows();
                // Optional: print block structure and content for debugging
                // std::cout << block.dump_structure() << std::endl;
            }
            block.clear();
        }

        // Verify results
        std::cout << "Total rows read: " << total_rows << std::endl;
        assert(total_rows == 3);
        std::cout << "Assertion PASSED: Expected 3 rows, got " << total_rows << "." << std::endl;

        // Close the scanner
        std::ignore = _scan_node->close(&_runtime_state);
        std::cout << "--- Test Finished ---" << std::endl;
    }

private:
    void init_desc_table() {
        TDescriptorTable t_desc_table;
        // Table descriptor
        TTableDescriptor t_table_desc;
        t_table_desc.id = 0;
        t_table_desc.tableType = TTableType::BROKER_TABLE; // Use BROKER_TABLE for file scans
        t_table_desc.numCols = 3;
        t_table_desc.numClusteringCols = 0;
        t_desc_table.tableDescriptors.push_back(t_table_desc);

        // Slot descriptors (c1, c2, c3)
        for (int i = 0; i < 3; ++i) {
            TSlotDescriptor slot_desc;
            slot_desc.id = i;
            slot_desc.parent = 0;
            TTypeDesc type;
            TTypeNode node;
            node.__set_type(TTypeNodeType::SCALAR);
            TScalarType scalar_type;
            scalar_type.__set_type(TPrimitiveType::VARCHAR);
            scalar_type.__set_len(100);
            node.__set_scalar_type(scalar_type);
            type.types.push_back(node);
            slot_desc.slotType = type;
            slot_desc.columnPos = i;
            slot_desc.byteOffset = i * sizeof(StringRef);
            slot_desc.nullIndicatorByte = 0;
            slot_desc.nullIndicatorBit = -1;
            slot_desc.colName = "c" + std::to_string(i + 1);
            slot_desc.slotIdx = i + 1;
            slot_desc.isMaterialized = true;
            t_desc_table.slotDescriptors.push_back(slot_desc);
        }
        t_desc_table.__isset.slotDescriptors = true;

        // Tuple descriptor
        TTupleDescriptor t_tuple_desc;
        t_tuple_desc.id = 0;
        t_tuple_desc.byteSize = 3 * sizeof(StringRef);
        t_tuple_desc.numNullBytes = 0;
        t_tuple_desc.tableId = 0;
        t_tuple_desc.__isset.tableId = true;
        t_desc_table.tupleDescriptors.push_back(t_tuple_desc);

        auto st = DescriptorTbl::create(&_obj_pool, t_desc_table, &_desc_tbl);
        assert(st.ok());
    }

    ExecEnv* _env = nullptr;
    ObjectPool _obj_pool;
    RuntimeState _runtime_state;
    DescriptorTbl* _desc_tbl = nullptr;
    TPlanNode _tnode;
    TUniqueId _unique_id;
    TQueryOptions _query_options;
    TQueryGlobals _query_globals;
    TFileScanRange _scan_range;

    std::string _test_dir;
    std::string _test_file_path;
    std::unique_ptr<NewFileScanNode> _scan_node;
};

} // namespace doris::vectorized

int main(int argc, char** argv) {
    // A minimal ExecEnv setup
    // doris::ExecEnv exec_env;
    // doris::config::mem_limit = "80%";
    // doris::config::send_batch_thread_pool_thread_num = 2;
    // doris::config::send_batch_thread_pool_queue_size = 10;

    string conffile = string(getenv("DORIS_HOME")) + "/conf/be.conf";
    if (!doris::config::init(conffile.c_str(), true, true, true)) {
        fprintf(stderr, "error read config file. \n");
        return -1;
    }

    std::vector<doris::StorePath> paths;
    auto olap_res = doris::parse_conf_store_paths(doris::config::storage_root_path, &paths);
    if (!olap_res) {
        // LOG(ERROR) << "parse config storage path failed, path=" << doris::config::storage_root_path;
        // exit(-1);
        return -1;
    }

    // Doris own signal handler must be register after jvm is init.
    // Or our own sig-handler for SIGINT & SIGTERM will not be chained ...
    // https://www.oracle.com/java/technologies/javase/signals.html
    // doris::init_signals();

    // ATTN: MUST init before `ExecEnv`, `StorageEngine` and other daemon services
    //
    //       Daemon ───┬──► StorageEngine ──► ExecEnv ──► Disk/Mem/CpuInfo
    //                 │
    //                 │
    // BackendService ─┘
    doris::CpuInfo::init();
    doris::DiskInfo::init();
    doris::MemInfo::init();

    doris::ThreadLocalHandle::create_thread_local_if_not_exits();

    // doris::ExecEnv::init_mem_tracker();
    std::ignore = doris::ExecEnv::init(doris::ExecEnv::GetInstance(), paths, {}, {});
    // doris::ExecEnv::set_tracking_memory(true);
    // doris::Status st = exec_env.init({}, false);
    // assert(st.ok());

    // Run the test
    doris::vectorized::FileScanNodeTest test;
    test.run_test();

    return 0;
}

// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

#define BE_TEST 1

#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <filesystem>

// 核心头文件
#include "common/object_pool.h"
#include "common/sync_point.h"
#include "gen_cpp/Descriptors_types.h"
#include "gen_cpp/PlanNodes_types.h"
#include "io/fs/local_file_system.h"
#include "olap/wal/wal_manager.h"
#include "runtime/descriptors.h"
#include "runtime/memory/mem_tracker.h"
#include "runtime/runtime_state.h"
#include "runtime/user_function_cache.h"
#include "vec/exec/scan/new_file_scan_node.h"
#include "vec/exec/scan/vfile_scanner.h"
#include "vec/exec/format/format_common.h"
#include "util/debug_util.h"

#include "util/disk_info.h"
#include "vec/core/block.h"

namespace doris {
namespace vectorized {

// 这是一个用于测试的 SplitSourceConnector 实现。
// 它模拟了如何向 VFileScanner 提供文件扫描范围。
class TestSplitSourceConnector : public SplitSourceConnector {
private:
    std::mutex _range_lock; // 用于保护扫描范围访问的互斥锁
    TFileScanRange _scan_range; // 存储文件扫描范围
    int _range_index = 0; // 当前扫描范围的索引

public:
    // 构造函数，接收一个文件扫描范围
    TestSplitSourceConnector(const TFileScanRange& scan_range) : _scan_range(scan_range) {}

    // 获取下一个扫描范围
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

    // 获取扫描范围的总数
    int num_scan_ranges() override { return _scan_range.ranges.size(); }

    // 获取扫描范围的参数
    TFileScanRangeParams* get_params() override { return &_scan_range.params; }
};

// 初始化描述符表，用于定义表的元数据（如列类型、名称等）
static void init_desc_table(ObjectPool* obj_pool, DescriptorTbl** desc_tbl, RuntimeState* runtime_state) {
    TDescriptorTable t_desc_table;

    // 创建表描述符
    TTableDescriptor t_table_desc;
    t_table_desc.id = 0;
    t_table_desc.tableType = TTableType::OLAP_TABLE;
    t_table_desc.numCols = 0;
    t_table_desc.numClusteringCols = 0;
    t_desc_table.tableDescriptors.push_back(t_table_desc);
    t_desc_table.__isset.tableDescriptors = true;

    int next_slot_id = 1;
    // 定义 c1 列
    {
        TSlotDescriptor slot_desc;
        slot_desc.id = next_slot_id++;
        slot_desc.parent = 0;
        TTypeDesc type;
        {
            TTypeNode node;
            node.__set_type(TTypeNodeType::SCALAR);
            TScalarType scalar_type;
            scalar_type.__set_type(TPrimitiveType::VARCHAR);
            scalar_type.__set_len(32);
            node.__set_scalar_type(scalar_type);
            type.types.push_back(node);
        }
        slot_desc.slotType = type;
        slot_desc.columnPos = 0;
        slot_desc.byteOffset = 0;
        slot_desc.nullIndicatorByte = 0;
        slot_desc.nullIndicatorBit = -1;
        slot_desc.colName = "c1";
        slot_desc.slotIdx = 1;
        slot_desc.col_unique_id = 0;
        slot_desc.isMaterialized = true;
        t_desc_table.slotDescriptors.push_back(slot_desc);
    }
    // 定义 c2 列
    {
        TSlotDescriptor slot_desc;
        slot_desc.id = next_slot_id++;
        slot_desc.parent = 0;
        TTypeDesc type;
        {
            TTypeNode node;
            node.__set_type(TTypeNodeType::SCALAR);
            TScalarType scalar_type;
            scalar_type.__set_type(TPrimitiveType::VARCHAR);
            scalar_type.__set_len(32);
            node.__set_scalar_type(scalar_type);
            type.types.push_back(node);
        }
        slot_desc.slotType = type;
        slot_desc.columnPos = 1;
        slot_desc.byteOffset = 4;
        slot_desc.nullIndicatorByte = 0;
        slot_desc.nullIndicatorBit = -1;
        slot_desc.colName = "c2";
        slot_desc.slotIdx = 2;
        slot_desc.col_unique_id = 1;
        slot_desc.isMaterialized = true;
        t_desc_table.slotDescriptors.push_back(slot_desc);
    }
    // 定义 c3 列
    {
        TSlotDescriptor slot_desc;
        slot_desc.id = next_slot_id++;
        slot_desc.parent = 0;
        TTypeDesc type;
        {
            TTypeNode node;
            node.__set_type(TTypeNodeType::SCALAR);
            TScalarType scalar_type;
            scalar_type.__set_type(TPrimitiveType::VARCHAR);
            scalar_type.__set_len(32);
            node.__set_scalar_type(scalar_type);
            type.types.push_back(node);
        }
        slot_desc.slotType = type;
        slot_desc.columnPos = 2;
        slot_desc.byteOffset = 8;
        slot_desc.nullIndicatorByte = 0;
        slot_desc.nullIndicatorBit = -1;
        slot_desc.colName = "c3";
        slot_desc.slotIdx = 3;
        slot_desc.col_unique_id = 2;
        slot_desc.isMaterialized = true;
        t_desc_table.slotDescriptors.push_back(slot_desc);
    }

    t_desc_table.__isset.slotDescriptors = true;
    // 定义元组描述符
    {
        TTupleDescriptor t_tuple_desc;
        t_tuple_desc.id = 0;
        t_tuple_desc.byteSize = 12;
        t_tuple_desc.numNullBytes = 0;
        t_tuple_desc.tableId = 0;
        t_tuple_desc.__isset.tableId = true;
        t_desc_table.tupleDescriptors.push_back(t_tuple_desc);
    }

    // 创建描述符表
    auto st = DescriptorTbl::create(obj_pool, t_desc_table, desc_tbl);
    assert(st.ok());

    // 将描述符表设置到运行时状态中
    runtime_state->set_desc_tbl(*desc_tbl);
}

// 生成并准备一个 VFileScanner 实例
static void generate_scanner(std::shared_ptr<VFileScanner>& scanner, RuntimeState* runtime_state, NewFileScanNode* scan_node, 
                             const TFileScanRange& scan_range, RuntimeProfile* profile, ShardedKVCache* kv_cache) {
    // 使用测试用的 SplitSourceConnector
    auto split_source = std::make_shared<TestSplitSourceConnector>(scan_range);
    // 创建 VFileScanner
    scanner = std::make_shared<VFileScanner>(runtime_state, scan_node, -1, split_source,
                                             profile, kv_cache);
    scanner->_is_load = false;
    vectorized::VExprContextSPtrs conjuncts;
    std::unordered_map<std::string, ColumnValueRangeType> colname_to_value_range;
    std::unordered_map<std::string, int> colname_to_slot_id;
    // 准备 scanner
    WARN_IF_ERROR(scanner->prepare(conjuncts, &colname_to_value_range, &colname_to_slot_id),
                  "fail to prepare scanner");
}

} // namespace vectorized
} // namespace doris


using namespace doris;

int main(int argc, char** argv) {
    // 获取 DORIS_HOME 环境变量
    std::string doris_home = getenv("DORIS_HOME");
    // 设置 WAL 相关配置
    doris::config::group_commit_wal_max_disk_limit = "100M";
    
    // --- 变量设置 ---
    doris::ObjectPool obj_pool;
    doris::DescriptorTbl* desc_tbl = nullptr;
    doris::TUniqueId unique_id;
    doris::TQueryOptions query_options;
    doris::TQueryGlobals query_globals;

    // TODO
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
    std::string wal_dir = doris_home + "/wal_test_main";
    doris::config::group_commit_wal_path = wal_dir;
    doris::config::enable_memory_orphan_check = false; // why?

    std::ignore = doris::ExecEnv::init(doris::ExecEnv::GetInstance(), paths, {}, {});
    // doris::ExecEnv::set_tracking_memory(true);
    // doris::Status st = exec_env.init({}, false);
    // assert(st.ok());

    // 在ExecEnv::init 执行完再执行
    doris::RuntimeState runtime_state(query_globals);
    doris::ExecEnv* env = doris::ExecEnv::GetInstance();
    
    // 定义测试用的 WAL 目录、数据库ID、表ID等
    // std::string wal_dir = doris_home + "/wal_test_main";
    int64_t db_id = 1;
    int64_t tb_id = 2;
    int64_t txn_id_1 = 123;
    int64_t txn_id_2 = 456;
    uint32_t version_0 = 0;
    uint32_t version_1 = 1;
    int64_t backend_id = 1001;
    std::string label_1 = "test1";
    std::string label_2 = "test2";
    doris::TupleId dst_tuple_id = 0;

    // --- 初始化 ---
    // 初始化描述符表和运行时状态
    doris::vectorized::init_desc_table(&obj_pool, &desc_tbl, &runtime_state);
    auto profile = runtime_state.runtime_profile();
    WARN_IF_ERROR(runtime_state.init(unique_id, query_options, query_globals, env),
                  "fail to init runtime_state");

    // 创建用于测试的 WAL 目录
    WARN_IF_ERROR(doris::io::global_local_filesystem()->create_directory(
                      wal_dir + "/" + std::to_string(db_id) + "/" + std::to_string(tb_id)),
                  "fail to create directory");

    // --- 设置扫描节点 ---
    doris::TPlanNode tnode;
    tnode.node_id = 0;
    tnode.node_type = doris::TPlanNodeType::FILE_SCAN_NODE;
    tnode.num_children = 0;
    tnode.limit = -1;
    tnode.row_tuples.push_back(0);
    tnode.nullable_tuples.push_back(false);
    tnode.file_scan_node.tuple_id = 0;
    tnode.__isset.file_scan_node = true;

    // 创建并初始化 NewFileScanNode
    auto scan_node = std::make_shared<doris::vectorized::NewFileScanNode>(&obj_pool, tnode, *desc_tbl);
    scan_node->_output_tuple_desc = runtime_state.desc_tbl().get_tuple_descriptor(dst_tuple_id);
    WARN_IF_ERROR(scan_node->init(tnode, &runtime_state), "fail to init scan_node");
    WARN_IF_ERROR(scan_node->prepare(&runtime_state), "fail to prepare scan_node");

    // --- 设置扫描范围 ---
    doris::TFileRangeDesc range_desc;
    range_desc.start_offset = 0;
    range_desc.size = 1000;
    std::vector<doris::TFileRangeDesc> ranges;
    ranges.push_back(range_desc);
    doris::TFileScanRange scan_range;
    scan_range.ranges = ranges;
    scan_range.__isset.params = true;
    scan_range.params.format_type = doris::TFileFormatType::FORMAT_WAL;
    
    // --- 设置环境和 WAL 管理器 ---
    auto kv_cache = std::make_unique<doris::vectorized::ShardedKVCache>(48);
    auto master_info = std::make_unique<doris::TMasterInfo>();
    
    env->_master_info = master_info.get();
    env->_master_info->network_address.hostname = "host name";
    env->_master_info->network_address.port = backend_id;
    env->_master_info->backend_id = 1001;
    // env->_wal_manager = doris::WalManager::create_shared(env, wal_dir);
    
    // --- 准备测试数据 ---
    // 初始化 WAL 目录信息并创建 WAL 文件路径
    std::string base_path;
    auto st = env->_wal_manager->_init_wal_dirs_info();
    // assert(st.ok());
    if (!st) { std::cout << st.to_string(); }
    st = env->_wal_manager->create_wal_path(db_id, tb_id, txn_id_1, label_1, base_path, version_0);
    // assert(st.ok());
    if (!st) { std::cout << st.to_string(); }

    // 将预先准备好的 WAL 测试文件复制到测试目录
    std::string src1 = doris_home + "/be/test/exec/test_data/wal_scanner/wal_version0";
    std::string dst1 = wal_dir + "/" + std::to_string(db_id) + "/" + std::to_string(tb_id) + "/" +
                      std::to_string(version_0) + "_" + std::to_string(backend_id) + "_" +
                      std::to_string(txn_id_1) + "_" + label_1;
    std::filesystem::copy(src1, dst1, std::filesystem::copy_options::overwrite_existing);

    st = env->_wal_manager->create_wal_path(db_id, tb_id, txn_id_2, label_2, base_path, version_1);
    assert(st.ok());
    std::string src2 = doris_home + "/be/test/exec/test_data/wal_scanner/wal_version1";
    std::string dst2 = wal_dir + "/" + std::to_string(db_id) + "/" + std::to_string(tb_id) + "/" +
                      std::to_string(version_1) + "_" + std::to_string(backend_id) + "_" +
                      std::to_string(txn_id_2) + "_" + label_2;
    std::filesystem::copy(src2, dst2, std::filesystem::copy_options::overwrite_existing);

    // --- 测试逻辑 ---
    // 测试点 1: 读取版本为 0 的 WAL 文件
    std::cout << "Testing reading wal file with wal_version=0" << std::endl;
    runtime_state._wal_id = txn_id_1; // 设置要读取的 WAL 文件的事务ID
    std::shared_ptr<doris::vectorized::VFileScanner> scanner = nullptr;
    doris::vectorized::generate_scanner(scanner, &runtime_state, scan_node.get(), scan_range, profile, kv_cache.get());
    
    // auto block = std::make_unique<doris::vectorized::Block>();
    // std::unique_ptr<vectorized::Block> block(new vectorized::Block());
    auto block = doris::vectorized::Block::create_unique();
    bool eof = false;
    // 第一次读取，应该有数据
    st = scanner->get_block(&runtime_state, block.get(), &eof);
    // assert(st.ok());
    if (!st) { std::cout << st.to_string(); }
    assert(block->rows() == 3); // 验证读取到的行数
    std::cout << "Read " << block->rows() << " rows. OK." << std::endl;

    // Print block info
    std::cout << "Block structure:" << std::endl;
    std::cout << block->dump_structure() << std::endl;

    // std::cout << "Block data:" << std::endl;
    // std::cout << block->dump_data() << std::endl;
    // Block data:
    // F20250805 16:57:34.349085 1650245 assert_cast.h:59] Bad cast from type:doris::vectorized::ColumnNullable to doris::vectorized::ColumnStr<unsigned int>

    block->clear();
    
    // 第二次读取，应该到达文件末尾
    st = scanner->get_block(&runtime_state, block.get(), &eof);
    // assert(st.ok());
    if (!st) { std::cout << st.to_string(); }
    assert(block->rows() == 0);
    assert(eof);
    std::cout << "Read " << block->rows() << " rows and hit eof. OK." << std::endl;
    WARN_IF_ERROR(scanner->close(&runtime_state), "fail to close scanner");

    // 测试点 2: 读取版本为 1 的 WAL 文件
    std::cout << "Testing reading wal file with wal_version=1" << std::endl;
    eof = false;
    runtime_state._wal_id = txn_id_2; // 设置要读取的 WAL 文件的事务ID
    doris::vectorized::generate_scanner(scanner, &runtime_state, scan_node.get(), scan_range, profile, kv_cache.get());
    
    // 第一次读取
    st = scanner->get_block(&runtime_state, block.get(), &eof);
    // assert(st.ok());
    if (!st) { std::cout << st.to_string(); }
    assert(block->rows() == 3); // 验证读取到的行数
    std::cout << "Read " << block->rows() << " rows. OK." << std::endl;
    block->clear();

    // 第二次读取，到达文件末尾
    st = scanner->get_block(&runtime_state, block.get(), &eof);
    // assert(st.ok());
    if (!st) { std::cout << st.to_string(); }
    assert(block->rows() == 0);
    assert(eof);
    std::cout << "Read " << block->rows() << " rows and hit eof. OK." << std::endl;
    WARN_IF_ERROR(scanner->close(&runtime_state), "fail to close scanner");

    // --- 清理工作 ---
    // 关闭扫描节点
    WARN_IF_ERROR(scan_node->close(&runtime_state), "fail to close scan_node");
    // // 删除测试用的 WAL 目录
    // WARN_IF_ERROR(doris::io::global_local_filesystem()->delete_directory(wal_dir),
    //               fmt::format("fail to delete dir={}", wal_dir));
    // 停止 WAL 管理器
    // env->_wal_manager.stop();
    SAFE_STOP(env->_wal_manager);

    std::cout << "Test finished successfully." << std::endl;
    return 0; // 返回 0 表示测试成功
}

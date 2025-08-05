#include <iostream>
#include "vec/core/block.h"
#include "runtime/thread_context.h"
#include "vec/columns/column_vector.h"
#include "vec/columns/column_string.h"
#include "vec/data_types/data_type_number.h"
#include "vec/data_types/data_type_string.h"

#include "olap/wal/wal_manager.h"
#include "util/disk_info.h"

using namespace doris::vectorized;

int main() {
    // must call create_thread_local_if_not_exits() before use thread_context().
    string conffile = string(getenv("DORIS_HOME")) + "/conf/be.conf";
    if (!doris::config::init(conffile.c_str(), true, true, true)) {
        fprintf(stderr, "error read config file. \n");
        return -1;
    }
    std::vector<doris::StorePath> paths;
    std::ignore = doris::parse_conf_store_paths(doris::config::storage_root_path, &paths);
    doris::CpuInfo::init();
    doris::DiskInfo::init();
    doris::MemInfo::init();
    doris::ThreadLocalHandle::create_thread_local_if_not_exits();

    doris::config::enable_memory_orphan_check = false; // why?
    auto env = doris::ExecEnv::GetInstance();
    std::ignore = doris::ExecEnv::init(env, paths, {}, {});

    // Create a block
    Block block;

    // Create columns
    auto col1 = ColumnVector<Int32>::create();
    auto col2 = ColumnString::create();

    // Insert data
    col1->insert(1);
    col1->insert(2);
    col1->insert(3);

    col2->insert("apple");
    col2->insert("banana");
    col2->insert("cherry");

    // Create column info and add to block
    ColumnWithTypeAndName col1_with_name(std::move(col1), std::make_shared<DataTypeInt32>(), "ID");
    ColumnWithTypeAndName col2_with_name(std::move(col2), std::make_shared<DataTypeString>(), "Fruit");

    block.insert(col1_with_name);
    block.insert(col2_with_name);

    // Print block info
    std::cout << "Block structure:" << std::endl;
    std::cout << block.dump_structure() << std::endl;

    std::cout << "Block data:" << std::endl;
    std::cout << block.dump_data() << std::endl;

    // Assertions
    if (block.rows() != 3) {
        std::cerr << "Assertion failed: block.rows() != 3" << std::endl;
        return 1;
    }
    if (block.columns() != 2) {
        std::cerr << "Assertion failed: block.columns() != 2" << std::endl;
        return 1;
    }

    std::cout << "Block test passed!" << std::endl;

    env->_wal_manager->stop();
    return 0;
}

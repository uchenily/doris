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

#include "pipeline/exec/jdbc_scan_operator.h"

#include "common/object_pool.h"
#include "vec/exec/scan/jdbc_scanner.h"

namespace doris::pipeline {
#include "common/compile_check_begin.h"
std::string JDBCScanLocalState::name_suffix() const {
    return fmt::format("(nereids_id={} . table name = {})" + operator_name_suffix,
                       std::to_string(_parent->nereids_id()),
                       _parent->cast<JDBCScanOperatorX>()._table_name,
                       std::to_string(_parent->node_id()));
}

Status JDBCScanLocalState::_init_scanners(std::list<vectorized::ScannerSPtr>* scanners) {
    auto& p = _parent->cast<JDBCScanOperatorX>();
    std::unique_ptr<vectorized::JdbcScanner> scanner = vectorized::JdbcScanner::create_unique(
            state(), this, p._limit, p._tuple_id, p._query_string, p._table_type,
            _scanner_profile.get());
    RETURN_IF_ERROR(scanner->prepare(state(), _conjuncts));
    scanners->push_back(std::move(scanner));
    return Status::OK();
}

JDBCScanOperatorX::JDBCScanOperatorX(ObjectPool* pool, const TPlanNode& tnode, int operator_id,
                                     const DescriptorTbl& descs, int parallel_tasks)
        : ScanOperatorX<JDBCScanLocalState>(pool, tnode, operator_id, descs, parallel_tasks),
          _table_name(tnode.jdbc_scan_node.table_name),
          _tuple_id(tnode.jdbc_scan_node.tuple_id),
          _query_string(tnode.jdbc_scan_node.query_string),
          _table_type(tnode.jdbc_scan_node.table_type) {
    _output_tuple_id = tnode.jdbc_scan_node.tuple_id;
}

} // namespace doris::pipeline

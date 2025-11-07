#!/usr/bin/env python3
"""
反序列化 TPipelineFragmentParamsList 二进制文件
"""

# from PlanNodes.thrift
# enum TPlanNodeType {
#   OLAP_SCAN_NODE = 0,
#   MYSQL_SCAN_NODE = 1,
#   CSV_SCAN_NODE = 2, // deprecated
#   SCHEMA_SCAN_NODE = 3,
#   HASH_JOIN_NODE = 4,
#   MERGE_JOIN_NODE = 5, // deprecated
#   AGGREGATION_NODE = 6,
#   PRE_AGGREGATION_NODE = 7,
#   SORT_NODE = 8,
#   EXCHANGE_NODE = 9,
#   MERGE_NODE = 10,
#   SELECT_NODE = 11,
#   CROSS_JOIN_NODE = 12,
#   META_SCAN_NODE = 13,
#   ANALYTIC_EVAL_NODE = 14,
#   OLAP_REWRITE_NODE = 15, // deprecated
#   KUDU_SCAN_NODE = 16, // Deprecated
#   BROKER_SCAN_NODE = 17,
#   EMPTY_SET_NODE = 18, 
#   UNION_NODE = 19,
#   ES_SCAN_NODE = 20,
#   ES_HTTP_SCAN_NODE = 21,
#   REPEAT_NODE = 22,
#   ASSERT_NUM_ROWS_NODE = 23,
#   INTERSECT_NODE = 24,
#   EXCEPT_NODE = 25,
#   ODBC_SCAN_NODE = 26,
#   TABLE_FUNCTION_NODE = 27,
#   DATA_GEN_SCAN_NODE = 28,
#   FILE_SCAN_NODE = 29,
#   JDBC_SCAN_NODE = 30,
#   TEST_EXTERNAL_SCAN_NODE = 31,
#   PARTITION_SORT_NODE = 32,
#   GROUP_COMMIT_SCAN_NODE = 33,
#   MATERIALIZATION_NODE = 34
# }

import sys
import os
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol

# 添加当前目录到 Python 路径，以便导入生成的 Thrift 模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PaloInternalService import ttypes

# TPlanNodeType 枚举映射
NODE_TYPE_NAMES = {
    0: "OLAP_SCAN_NODE",
    1: "MYSQL_SCAN_NODE",
    2: "CSV_SCAN_NODE",
    3: "SCHEMA_SCAN_NODE",
    4: "HASH_JOIN_NODE",
    5: "MERGE_JOIN_NODE",
    6: "AGGREGATION_NODE",
    7: "PRE_AGGREGATION_NODE",
    8: "SORT_NODE",
    9: "EXCHANGE_NODE",
    10: "MERGE_NODE",
    11: "SELECT_NODE",
    12: "CROSS_JOIN_NODE",
    13: "META_SCAN_NODE",
    14: "ANALYTIC_EVAL_NODE",
    15: "OLAP_REWRITE_NODE",
    16: "KUDU_SCAN_NODE",
    17: "BROKER_SCAN_NODE",
    18: "EMPTY_SET_NODE",
    19: "UNION_NODE",
    20: "ES_SCAN_NODE",
    21: "ES_HTTP_SCAN_NODE",
    22: "REPEAT_NODE",
    23: "ASSERT_NUM_ROWS_NODE",
    24: "INTERSECT_NODE",
    25: "EXCEPT_NODE",
    26: "ODBC_SCAN_NODE",
    27: "TABLE_FUNCTION_NODE",
    28: "DATA_GEN_SCAN_NODE",
    29: "FILE_SCAN_NODE",
    30: "JDBC_SCAN_NODE",
    31: "TEST_EXTERNAL_SCAN_NODE",
    32: "PARTITION_SORT_NODE",
    33: "GROUP_COMMIT_SCAN_NODE",
    34: "MATERIALIZATION_NODE",
}

def deserialize_pipeline_fragment_params_list(binary_file_path):
    """
    反序列化 TPipelineFragmentParamsList 二进制文件
    
    Args:
        binary_file_path: 二进制文件路径
        
    Returns:
        TPipelineFragmentParamsList 对象
    """
    protocols_to_try = [
        # ("TBinaryProtocol", TBinaryProtocol.TBinaryProtocol),
        ("TCompactProtocol", TCompactProtocol.TCompactProtocol)
    ]
    
    for protocol_name, protocol_class in protocols_to_try:
        try:
            print(f"尝试使用 {protocol_name} 反序列化...")
            
            # 读取二进制文件
            with open(binary_file_path, 'rb') as f:
                binary_data = f.read()
            
            # 创建 Thrift transport 和 protocol
            transport = TTransport.TMemoryBuffer(binary_data)
            protocol = protocol_class(transport)
            
            # 创建 TPipelineFragmentParamsList 对象并反序列化
            params_list = ttypes.TPipelineFragmentParamsList()
            params_list.read(protocol)
            
            print(f"使用 {protocol_name} 反序列化成功!")
            return params_list
            
        except Exception as e:
            print(f"使用 {protocol_name} 反序列化失败: {e}")
            continue
    
    print("所有协议都尝试失败")
    return None

def print_params_list_info(params_list):
    """
    打印 TPipelineFragmentParamsList 的重要信息

    Args:
        params_list: TPipelineFragmentParamsList 对象
    """
    if params_list is None:
        print("TPipelineFragmentParamsList 对象为空")
        return

    print("=== TPipelineFragmentParamsList 基本信息 ===")
    print(f"params_list 长度: {len(params_list.params_list) if params_list.params_list else 0}")
    print(f"is_nereids: {params_list.is_nereids}")
    print(f"fragment_num_on_host: {params_list.fragment_num_on_host}")

    if params_list.query_id:
        print(f"query_id: hi={params_list.query_id.hi}, lo={params_list.query_id.lo}")

    # 收集所有文件路径
    file_paths = []

    # 打印所有 fragment 的信息
    if params_list.params_list:
        print(f"\n=== Fragment 信息 (共 {len(params_list.params_list)} 个) ===")
        for i, fragment in enumerate(params_list.params_list):
            print(f"\n--- Fragment {i+1} ---")
            print(f"fragment_id: {fragment.fragment_id}")
            print(f"backend_id: {fragment.backend_id}")
            print(f"total_instances: {fragment.total_instances}")

            if fragment.fragment and fragment.fragment.plan and fragment.fragment.plan.nodes:
                print(f"plan nodes 数量: {len(fragment.fragment.plan.nodes)}")
                for j, node in enumerate(fragment.fragment.plan.nodes):
                    node_type_name = NODE_TYPE_NAMES.get(node.node_type, f"UNKNOWN({node.node_type})")
                    print(f"  节点 {j+1}: node_id={node.node_id}, node_type={node_type_name}")

                    # 打印 conjuncts 中的表达式信息
                    if hasattr(node, 'conjuncts') and node.conjuncts:
                        for k, conjunct in enumerate(node.conjuncts):
                            print(f"    conjunct {k+1}:")
                            if hasattr(conjunct, 'nodes') and conjunct.nodes:
                                for m, expr_node in enumerate(conjunct.nodes):
                                    if hasattr(expr_node, 'label') and expr_node.label:
                                        print(f"      expr {m+1} label: {expr_node.label}")
                                    if hasattr(expr_node, 'fn') and expr_node.fn:
                                        if hasattr(expr_node.fn, 'name') and expr_node.fn.name:
                                            print(f"      expr {m+1} function: {expr_node.fn.name.function_name}")
                                        if hasattr(expr_node.fn, 'signature'):
                                            print(f"      expr {m+1} signature: {expr_node.fn.signature}")

                    # 打印 projections 中的表达式信息
                    if hasattr(node, 'projections') and node.projections:
                        for k, projection in enumerate(node.projections):
                            print(f"    projection {k+1}:")
                            if hasattr(projection, 'nodes') and projection.nodes:
                                for m, expr_node in enumerate(projection.nodes):
                                    if hasattr(expr_node, 'label') and expr_node.label:
                                        print(f"      expr {m+1} label: {expr_node.label}")

                    if hasattr(node, 'file_scan_node') and node.file_scan_node:
                        print(f"    scan table: {node.file_scan_node.table_name}")
                    if hasattr(node, 'hash_join_node') and node.hash_join_node:
                        print("    hash join node")
                    if hasattr(node, 'exchange_node') and node.exchange_node:
                        print("    exchange node")

            # 打印 scan 相关信息
            if hasattr(fragment, 'file_scan_params') and fragment.file_scan_params:
                print(f"file_scan_params 数量: {len(fragment.file_scan_params)}")
                for scan_id, scan_param in fragment.file_scan_params.items():
                    print(f"  scan_id {scan_id}:")
                    if hasattr(scan_param, 'file_attributes') and scan_param.file_attributes:
                        print("    file_attributes present")

            # 尝试打印 scan ranges - 在所有 fragment 中查找 local_params
            if hasattr(fragment, 'local_params') and fragment.local_params:
                for local_param in fragment.local_params:
                    if hasattr(local_param, 'per_node_scan_ranges') and local_param.per_node_scan_ranges:
                        for node_id, ranges in local_param.per_node_scan_ranges.items():
                            for range_param in ranges:
                                if hasattr(range_param, 'scan_range') and hasattr(range_param.scan_range, 'ext_scan_range'):
                                    ext_range = range_param.scan_range.ext_scan_range
                                    if hasattr(ext_range, 'file_scan_range') and ext_range.file_scan_range:
                                        for file_range in ext_range.file_scan_range.ranges:
                                            if hasattr(file_range, 'path'):
                                                print(f"    scan path: {file_range.path}")
                                                file_paths.append(file_range.path)
                                            if hasattr(file_range, 'size'):
                                                print(f"    scan size: {file_range.size}")
                                            if hasattr(file_range, 'file_size'):
                                                print(f"    file size: {file_range.file_size}")
                                            if hasattr(file_range, 'table_format_params') and file_range.table_format_params:
                                                print(f"    table format: {file_range.table_format_params.table_format_type}")

            # 打印 output_sink 信息
            if hasattr(fragment.fragment, 'output_sink') and fragment.fragment.output_sink:
                print(f"output_sink type: {fragment.fragment.output_sink.type}")
                if hasattr(fragment.fragment.output_sink, 'result_sink') and fragment.fragment.output_sink.result_sink:
                    print("  result_sink present")
                if hasattr(fragment.fragment.output_sink, 'stream_sink') and fragment.fragment.output_sink.stream_sink:
                    print("  stream_sink present")
                if hasattr(fragment.fragment.output_sink, 'export_sink') and fragment.fragment.output_sink.export_sink:
                    print("  export_sink present")
                if hasattr(fragment.fragment.output_sink, 'olap_table_sink') and fragment.fragment.output_sink.olap_table_sink:
                    print("  olap_table_sink present")

            # 打印 output_exprs 信息（列名和类型）
            if hasattr(fragment.fragment, 'output_exprs') and fragment.fragment.output_exprs:
                print(f"output_exprs 数量: {len(fragment.fragment.output_exprs)}")
                for idx, expr in enumerate(fragment.fragment.output_exprs):
                    print(f"  列 {idx+1}:")
                    if hasattr(expr, 'nodes') and expr.nodes:
                        for node in expr.nodes:
                            if hasattr(node, 'type') and node.type:
                                if hasattr(node.type, 'types') and node.type.types:
                                    type_info = node.type.types[0]
                                    if hasattr(type_info, 'scalar_type') and type_info.scalar_type:
                                        type_name = type_info.scalar_type.type
                                        print(f"    类型: {type_name}")
                            if hasattr(node, 'label') and node.label:
                                print(f"    列名: {node.label}")
                            if hasattr(node, 'slot_ref') and node.slot_ref:
                                if hasattr(node.slot_ref, 'col_name') and node.slot_ref.col_name:
                                    print(f"    列名: {node.slot_ref.col_name}")

def main():
    binary_file_path = sys.argv[1]

    # 获取绝对路径
    abs_path = os.path.abspath(binary_file_path)
    print(f"开始反序列化文件: {binary_file_path}")
    print(f"文件绝对路径: {abs_path}")

    # 检查文件是否存在
    if not os.path.exists(binary_file_path):
        print(f"错误: 文件 {binary_file_path} 不存在")
        return
    
    # 反序列化
    params_list = deserialize_pipeline_fragment_params_list(binary_file_path)
    
    if params_list:
        print("反序列化成功!")
        print_params_list_info(params_list)
        
        try:
            with open("output.txt", "w", encoding="utf-8") as f:
                f.write(str(params_list))
            print(f"\n完整的反序列化对象已保存到: output.txt")
        except Exception as e:
            print(f"保存对象到文件失败: {e}")
    else:
        print("反序列化失败")

if __name__ == "__main__":
    main()

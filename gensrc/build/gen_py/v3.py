#!/usr/bin/env python3

from Opcodes.ttypes import *
from FrontendService.ttypes import *
from Planner.ttypes import *
from Metrics.ttypes import *
from BackendService.ttypes import *
from DataSinks.ttypes import *
from PaloInternalService.ttypes import *
from Partitions.ttypes import *
from NetworkTest.ttypes import *
from Exprs.ttypes import *
from Status.ttypes import *
from Types.ttypes import *
from PlanNodes.ttypes import *
from Descriptors.ttypes import *
from PaloBrokerService.ttypes import *
from HeartbeatService.ttypes import *
from Data.ttypes import *
from DorisExternalService.ttypes import *
from RuntimeProfile.ttypes import *
from AgentService.ttypes import *
from PaloService.ttypes import *
from MasterService.ttypes import *

host = "172.24.2.69"

query_id = TUniqueId(hi=1199038286675263702, lo=-7586643826940453435)
fragment_instance_id0 = TUniqueId(hi=1199038286675263702, lo=-7586643826940453433)
fragment_instance_id1 = TUniqueId(hi=1199038286675263702, lo=-7586643826940453434)
dest_fragment_instance_id = fragment_instance_id0

desc_tbl = TDescriptorTable(
    slotDescriptors=[
        TSlotDescriptor(
            id=0,
            parent=0,
            slotType=TTypeDesc(
                types=[
                    TTypeNode(
                        type=0,
                        scalar_type=TScalarType(type=6),
                    )
                ],
                byte_size=-1,
            ),
            columnPos=-1,
            byteOffset=-1,
            nullIndicatorByte=0,
            nullIndicatorBit=-1,
            colName="user_id",
            slotIdx=1,
            isMaterialized=True,
            col_unique_id=0,
            is_key=True,
            need_materialize=True,
            is_auto_increment=False,
            primitive_type=6,
        ),
        TSlotDescriptor(
            id=1,
            parent=0,
            slotType=TTypeDesc(
                types=[
                    TTypeNode(
                        type=0,
                        scalar_type=TScalarType(type=15, len=20),
                    )
                ],
                byte_size=20,
            ),
            columnPos=-1,
            byteOffset=-1,
            nullIndicatorByte=0,
            nullIndicatorBit=0,
            colName="name",
            slotIdx=2,
            isMaterialized=True,
            col_unique_id=1,
            is_key=False,
            need_materialize=True,
            is_auto_increment=False,
            primitive_type=15,
        ),
        TSlotDescriptor(
            id=2,
            parent=0,
            slotType=TTypeDesc(
                types=[
                    TTypeNode(
                        type=0,
                        scalar_type=TScalarType(type=5),
                    )
                ],
                byte_size=-1,
            ),
            columnPos=-1,
            byteOffset=-1,
            nullIndicatorByte=0,
            nullIndicatorBit=0,
            colName="age",
            slotIdx=0,
            isMaterialized=True,
            col_unique_id=2,
            is_key=False,
            need_materialize=True,
            is_auto_increment=False,
            primitive_type=5,
        ),
    ],
    tupleDescriptors=[
        TTupleDescriptor(
            id=0,
            byteSize=0,
            numNullBytes=0,
            tableId=10107,
        )
    ],
    tableDescriptors=[
        TTableDescriptor(
            id=10107,
            tableType=1,
            numCols=3,
            numClusteringCols=0,
            tableName="test_streamload",
            dbName="",
        )
    ],
)

query_options = TQueryOptions(
    abort_on_error=False,
    max_errors=0,
    disable_codegen=True,
    batch_size=4064,
    num_nodes=0,
    max_scan_range_length=0,
    num_scanner_threads=0,
    max_io_buffers=0,
    allow_unsupported_formats=False,
    default_order_by_limit=-1,
    mem_limit=2147483648,
    abort_on_default_limit_exceeded=False,
    query_timeout=900,
    is_report_success=False,
    codegen_level=0,
    kudu_latest_observed_ts=9223372036854775807,
    query_type=0,
    min_reservation=0,
    max_reservation=2147483648,
    initial_reservation_total_claims=2147483648,
    buffer_pool_limit=2147483648,
    default_spillable_buffer_size=2097152,
    min_spillable_buffer_size=65536,
    max_row_size=524288,
    disable_stream_preaggregations=False,
    mt_dop=0,
    load_mem_limit=0,
    enable_spilling=False,
    enable_enable_exchange_node_parallel_merge=False,
    runtime_filter_wait_time_ms=1000,
    runtime_filter_max_in_num=1024,
    return_object_data_as_binary=False,
    trim_tailing_spaces_for_external_table_query=False,
    enable_function_pushdown=False,
    fragment_transmission_compression_codec="none",
    enable_local_exchange=True,
    skip_storage_engine_merge=False,
    skip_delete_predicate=False,
    be_exec_version=7,
    partitioned_hash_join_rows_threshold=0,
    enable_share_hash_table_for_broadcast_join=True,
    check_overflow_for_decimal=True,
    skip_delete_bitmap=False,
    enable_pipeline_engine=True,
    repeat_max_num=10000,
    external_sort_bytes_threshold=0,
    partitioned_hash_agg_rows_threshold=0,
    enable_file_cache=False,
    insert_timeout=14400,
    execution_timeout=900,
    dry_run_query=False,
    enable_common_expr_pushdown=True,
    parallel_instance=12,
    mysql_row_binary_format=False,
    external_agg_bytes_threshold=0,
    external_agg_partition_bits=5,
    file_cache_base_path="random",
    enable_parquet_lazy_mat=True,
    enable_orc_lazy_mat=True,
    scan_queue_mem_limit=107374182,
    enable_scan_node_run_serial=False,
    enable_insert_strict=False,
    enable_inverted_index_query=True,
    truncate_char_or_varchar_columns=False,
    enable_hash_join_early_start_probe=False,
    enable_pipeline_x_engine=True,
    enable_memtable_on_sink_node=True,
    enable_delete_sub_predicate_v2=True,
    fe_process_uuid=1755071852133,
    inverted_index_conjunction_opt_threshold=1000,
    enable_profile=False,
    enable_page_cache=True,
    analyze_timeout=43200,
    faster_float_convert=False,
    enable_decimal256=False,
    enable_local_shuffle=True,
    skip_missing_version=False,
    runtime_filter_wait_infinitely=False,
    wait_full_block_schedule_times=2,
    inverted_index_max_expansions=50,
    inverted_index_skip_threshold=50,
    enable_parallel_scan=True,
    parallel_scan_max_scanners_count=48,
    parallel_scan_min_rows_per_scanner=2097152,
    skip_bad_tablet=False,
    scanner_scale_up_ratio=0.0,
    enable_distinct_streaming_aggregation=True,
    enable_join_spill=False,
    enable_sort_spill=False,
    enable_agg_spill=False,
    min_revocable_mem=33554432,
    spill_streaming_agg_mem_limit=268435456,
    data_queue_max_blocks=1,
    local_exchange_free_blocks_limit=4,
    enable_parquet_filter_by_min_max=True,
    enable_orc_filter_by_min_max=True,
    max_column_reader_num=20000,
    enable_force_spill=False,
    enable_no_need_read_data_opt=True,
    read_csv_empty_line_as_null=False,
    serde_dialect=0,
    enable_match_without_inverted_index=True,
    enable_fallback_on_missing_inverted_index=True,
    keep_carriage_return=False,
    runtime_bloom_filter_min_size=1048576,
    hive_parquet_use_column_names=True,
    hive_orc_use_column_names=True,
    runtime_bloom_filter_max_size=16777216,
    in_list_value_count_threshold=10,
    enable_verbose_profile=False,
    rpc_verbose_profile_max_instance_count=5,
    enable_adaptive_pipeline_task_serial_read_on_limit=True,
    adaptive_pipeline_task_serial_read_on_limit=10000,
    parallel_prepare_threshold=32,
    partition_topn_max_partitions=1024,
    partition_topn_pre_partition_rows=1000,
    enable_auto_create_when_overwrite=False,
    orc_tiny_stripe_threshold_bytes=8388608,
    orc_once_max_read_bytes=8388608,
    orc_max_merge_distance_bytes=1048576,
    fuzzy_disable_runtime_filter_in_be=False,
    new_is_ip_address_in_range=True,
    disable_file_cache=False,
)


olap_scan_node = TOlapScanNode(
    tuple_id=0,
    key_column_name=["user_id"],
    key_column_type=[6],
    is_preaggregation=True,
    keyType=1,
    table_name="test_streamload(test_streamload)",
    columns_desc=[
        TColumn(
            column_name="user_id",
            column_type=TColumnType(
                type=6,
                len=65533,
                index_len=8,
                precision=0,
                scale=0,
            ),
            is_key=True,
            is_allow_null=False,
            visible=True,
            col_unique_id=0,
            has_bitmap_index=False,
            has_ngram_bf_index=False,
            is_auto_increment=False,
            cluster_key_id=-1,
        ),
        TColumn(
            column_name="name",
            column_type=TColumnType(
                type=15,
                len=20,
                index_len=20,
                precision=0,
                scale=0,
            ),
            aggregation_type=5,
            is_key=False,
            is_allow_null=True,
            visible=True,
            col_unique_id=1,
            has_bitmap_index=False,
            has_ngram_bf_index=False,
            is_auto_increment=False,
            cluster_key_id=-1,
        ),
        TColumn(
            column_name="age",
            column_type=TColumnType(
                type=5,
                len=65533,
                index_len=4,
                precision=0,
                scale=0,
            ),
            aggregation_type=5,
            is_key=False,
            is_allow_null=True,
            visible=True,
            col_unique_id=2,
            has_bitmap_index=False,
            has_ngram_bf_index=False,
            is_auto_increment=False,
            cluster_key_id=-1,
        ),
    ],
    enable_unique_key_merge_on_write=False,
    push_down_agg_type_opt=0,
    use_topn_opt=False,
    indexes_desc=[],
    output_column_unique_ids={0, 1, 2},
    distribute_column_ids=[0],
    schema_version=0,
)

pipeline_framgnet_params_list = TPipelineFragmentParamsList(
    params_list=[
        # fragment0: exchange -> sink
        TPipelineFragmentParams(
            protocol_version=0,
            query_id=query_id,
            fragment_id=1,
            per_exch_num_senders={1: 1},
            desc_tbl=desc_tbl,
            destinations=[],
            num_senders=1,
            send_query_statistics_with_every_batch=False,
            coord=TNetworkAddress(hostname=host, port=9020),
            query_globals=TQueryGlobals(
                now_string="2025-08-13 16:28:28",
                timestamp_ms=1755073708813,
                time_zone="Asia/Shanghai",
                load_zero_tolerance=False,
                nano_seconds=813000000,
            ),
            query_options=query_options,
            fragment_num_on_host=2,
            backend_id=10011,
            need_wait_execution_trigger=True,
            is_simplified_param=False,
            fragment=TPlanFragment(
                plan=TPlan(
                    nodes=[
                        TPlanNode(
                            node_id=1,
                            node_type=9,
                            num_children=0,
                            limit=1,
                            row_tuples=[0],
                            nullable_tuples=[False],
                            compact_data=False,
                            exchange_node=TExchangeNode(
                                input_row_tuples=[0],
                                offset=0,
                                partition_type=0,
                            ),
                            distribute_expr_lists=[
                                [
                                    TExpr(
                                        nodes=[
                                            TExprNode(
                                                node_type=16,
                                                type=TTypeDesc(
                                                    types=[
                                                        TTypeNode(
                                                            type=0,
                                                            scalar_type=TScalarType(
                                                                type=6,
                                                            ),
                                                        )
                                                    ],
                                                    byte_size=-1,
                                                ),
                                                num_children=0,
                                                slot_ref=TSlotRef(
                                                    slot_id=0,
                                                    tuple_id=0,
                                                    col_unique_id=0,
                                                ),
                                                output_scale=-1,
                                                is_nullable=False,
                                                label="user_id",
                                            )
                                        ]
                                    )
                                ]
                            ],
                        )
                    ]
                ),
                output_exprs=[
                    TExpr(
                        nodes=[
                            TExprNode(
                                node_type=16,
                                type=TTypeDesc(
                                    types=[
                                        TTypeNode(
                                            type=0,
                                            scalar_type=TScalarType(
                                                type=6,
                                            ),
                                        )
                                    ],
                                    byte_size=-1,
                                ),
                                num_children=0,
                                slot_ref=TSlotRef(slot_id=0, tuple_id=0, col_unique_id=0),
                                output_scale=-1,
                                is_nullable=False,
                                label="user_id",
                            )
                        ]
                    ),
                    TExpr(
                        nodes=[
                            TExprNode(
                                node_type=16,
                                type=TTypeDesc(
                                    types=[
                                        TTypeNode(
                                            type=0,
                                            scalar_type=TScalarType(
                                                type=15,
                                                len=20,
                                            ),
                                        )
                                    ],
                                    byte_size=20,
                                ),
                                num_children=0,
                                slot_ref=TSlotRef(slot_id=1, tuple_id=0, col_unique_id=1),
                                output_scale=-1,
                                label="name",
                            )
                        ]
                    ),
                    TExpr(
                        nodes=[
                            TExprNode(
                                node_type=16,
                                type=TTypeDesc(
                                    types=[
                                        TTypeNode(
                                            type=0,
                                            scalar_type=TScalarType(
                                                type=5,
                                            ),
                                        )
                                    ],
                                    byte_size=-1,
                                ),
                                num_children=0,
                                slot_ref=TSlotRef(slot_id=2, tuple_id=0, col_unique_id=2),
                                output_scale=-1,
                                is_nullable=True,
                                label="age",
                            )
                        ]
                    ),
                ],
                output_sink=TDataSink(
                    type=1,
                    result_sink=TResultSink(type=0),
                ),
                partition=TDataPartition(type=0, partition_exprs=[]),
                min_reservation_bytes=0,
                initial_reservation_total_claims=0,
            ),
            local_params=[
                TPipelineInstanceParams(
                    fragment_instance_id=fragment_instance_id0,
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=0,
                    runtime_filter_params=TRuntimeFilterParams(
                        runtime_filter_merge_addr=TNetworkAddress(hostname=host, port=8060),
                    ),
                    backend_num=0,
                    per_node_shared_scans={},
                )
            ],
            workload_groups=[TPipelineWorkloadGroup(id=1)],
            file_scan_params={},
            group_commit=False,
            num_buckets=0,
            bucket_seq_to_instance_idx={},
            per_node_shared_scans={},
            total_instances=1,
            shuffle_idx_to_instance_idx={0: 0},
            is_nereids=True,
            current_connect_fe=TNetworkAddress(hostname=host, port=9020),
        ),
        # fragment1: scan -> sink
        TPipelineFragmentParams(
            protocol_version=0,
            query_id=query_id,
            fragment_id=0,
            per_exch_num_senders={},
            destinations=[
                TPlanFragmentDestination(
                    fragment_instance_id=dest_fragment_instance_id,
                    server=TNetworkAddress(hostname=host, port=-1),
                    brpc_server=TNetworkAddress(hostname=host, port=8060),
                )
            ],
            num_senders=1,
            send_query_statistics_with_every_batch=False,
            query_options=query_options,
            fragment_num_on_host=2,
            backend_id=10011,
            need_wait_execution_trigger=True,
            is_simplified_param=True,
            fragment=TPlanFragment(
                plan=TPlan(
                    nodes=[
                        TPlanNode(
                            node_id=0,
                            node_type=0,
                            num_children=0,
                            limit=1,
                            row_tuples=[0],
                            nullable_tuples=[False],
                            compact_data=False,
                            olap_scan_node=olap_scan_node,
                            push_down_agg_type_opt=0,
                        )
                    ]
                ),
                output_sink=TDataSink(
                    type=0,
                    stream_sink=TDataStreamSink(
                        dest_node_id=1,
                        output_partition=TDataPartition(type=0, partition_exprs=[]),
                        tablet_sink_txn_id=-1,
                    ),
                ),
                partition=TDataPartition(
                    type=2,
                    partition_exprs=[
                        TExpr(
                            nodes=[
                                TExprNode(
                                    node_type=16,
                                    type=TTypeDesc(
                                        types=[
                                            TTypeNode(
                                                type=0,
                                                scalar_type=TScalarType(
                                                    type=6,
                                                ),
                                            )
                                        ],
                                        byte_size=-1,
                                    ),
                                    num_children=0,
                                    slot_ref=TSlotRef(slot_id=0, tuple_id=0, col_unique_id=0),
                                    output_scale=-1,
                                    is_nullable=False,
                                    label="user_id",
                                )
                            ]
                        )
                    ],
                ),
                min_reservation_bytes=0,
                initial_reservation_total_claims=0,
            ),
            local_params=[
                TPipelineInstanceParams(
                    fragment_instance_id=fragment_instance_id1,
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={
                        0: [
                            # 创建表时分桶数设置为3, 所以有三个
                            TScanRangeParams(
                                scan_range=TScanRange(
                                    palo_scan_range=TPaloScanRange(
                                        hosts=[TNetworkAddress(hostname=host, port=9060)],
                                        schema_hash="0",
                                        version="39",
                                        version_hash="",
                                        tablet_id=10109,
                                        db_name="",
                                    ),
                                ),
                                volume_id=-1,
                            ),
                            TScanRangeParams(
                                scan_range=TScanRange(
                                    palo_scan_range=TPaloScanRange(
                                        hosts=[TNetworkAddress(hostname=host, port=9060)],
                                        schema_hash="0",
                                        version="39",
                                        version_hash="",
                                        tablet_id=10111,
                                        db_name="",
                                    ),
                                ),
                                volume_id=-1,
                            ),
                            TScanRangeParams(
                                scan_range=TScanRange(
                                    palo_scan_range=TPaloScanRange(
                                        hosts=[TNetworkAddress(hostname=host, port=9060)],
                                        schema_hash="0",
                                        version="39",
                                        version_hash="",
                                        tablet_id=10113,
                                        db_name="",
                                    ),
                                ),
                                volume_id=-1,
                            ),
                        ]
                    },
                    sender_id=0,
                    runtime_filter_params=TRuntimeFilterParams(
                        runtime_filter_merge_addr=TNetworkAddress(hostname=host, port=8060),
                    ),
                    backend_num=1,
                    per_node_shared_scans={0: True},
                )
            ],
            workload_groups=[TPipelineWorkloadGroup(id=1)],
            group_commit=False,
            num_buckets=0,
            bucket_seq_to_instance_idx={},
            per_node_shared_scans={0: True},
            parallel_instances=1,
            total_instances=1,
            shuffle_idx_to_instance_idx={-1: 0},
            is_nereids=True,
            current_connect_fe=TNetworkAddress(hostname=host, port=9020),
        ),
    ]
)

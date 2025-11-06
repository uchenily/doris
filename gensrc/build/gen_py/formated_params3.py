from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from PaloInternalService import ttypes as PaloInternalService_ttypes

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
# from PaloService.ttypes import *
from MasterService.ttypes import *


query_id=TUniqueId(hi=-5832036630201351297, lo=-5310685785171005794)

pipeline_framgnet_params_list = TPipelineFragmentParamsList(
    params_list=[
        TPipelineFragmentParams(
            protocol_version=0,
            query_id=query_id,
            fragment_id=3,
            per_exch_num_senders={3: 56, 1: 56},
            desc_tbl=TDescriptorTable(
                slotDescriptors=[
                    TSlotDescriptor(
                        id=0,
                        parent=0,
                        slotType=TTypeDesc(
                            types=[
                                TTypeNode(
                                    type=0,
                                    scalar_type=TScalarType(
                                        type=5,
                                        len=None,
                                        precision=None,
                                        scale=None,
                                        variant_max_subcolumns_count=0,
                                    ),
                                    struct_fields=None,
                                    contains_null=None,
                                    contains_nulls=None,
                                )
                            ],
                            is_nullable=None,
                            byte_size=-1,
                            sub_types=None,
                            result_is_nullable=None,
                            function_name=None,
                            be_exec_version=None,
                        ),
                        columnPos=-1,
                        byteOffset=-1,
                        nullIndicatorByte=0,
                        nullIndicatorBit=0,
                        colName="id",
                        slotIdx=0,
                        isMaterialized=True,
                        col_unique_id=-1,
                        is_key=False,
                        need_materialize=True,
                        is_auto_increment=False,
                        column_paths=None,
                        col_default_value=None,
                        primitive_type=5,
                        virtual_column_expr=None,
                    ),
                    TSlotDescriptor(
                        id=1,
                        parent=0,
                        slotType=TTypeDesc(
                            types=[
                                TTypeNode(
                                    type=0,
                                    scalar_type=TScalarType(
                                        type=5,
                                        len=None,
                                        precision=None,
                                        scale=None,
                                        variant_max_subcolumns_count=0,
                                    ),
                                    struct_fields=None,
                                    contains_null=None,
                                    contains_nulls=None,
                                )
                            ],
                            is_nullable=None,
                            byte_size=-1,
                            sub_types=None,
                            result_is_nullable=None,
                            function_name=None,
                            be_exec_version=None,
                        ),
                        columnPos=-1,
                        byteOffset=-1,
                        nullIndicatorByte=0,
                        nullIndicatorBit=0,
                        colName="age",
                        slotIdx=1,
                        isMaterialized=True,
                        col_unique_id=-1,
                        is_key=False,
                        need_materialize=True,
                        is_auto_increment=False,
                        column_paths=None,
                        col_default_value=None,
                        primitive_type=5,
                        virtual_column_expr=None,
                    ),
                    TSlotDescriptor(
                        id=2,
                        parent=1,
                        slotType=TTypeDesc(
                            types=[
                                TTypeNode(
                                    type=0,
                                    scalar_type=TScalarType(
                                        type=5,
                                        len=None,
                                        precision=None,
                                        scale=None,
                                        variant_max_subcolumns_count=0,
                                    ),
                                    struct_fields=None,
                                    contains_null=None,
                                    contains_nulls=None,
                                )
                            ],
                            is_nullable=None,
                            byte_size=-1,
                            sub_types=None,
                            result_is_nullable=None,
                            function_name=None,
                            be_exec_version=None,
                        ),
                        columnPos=-1,
                        byteOffset=-1,
                        nullIndicatorByte=0,
                        nullIndicatorBit=0,
                        colName="id",
                        slotIdx=0,
                        isMaterialized=True,
                        col_unique_id=-1,
                        is_key=False,
                        need_materialize=True,
                        is_auto_increment=False,
                        column_paths=None,
                        col_default_value=None,
                        primitive_type=5,
                        virtual_column_expr=None,
                    ),
                    TSlotDescriptor(
                        id=3,
                        parent=1,
                        slotType=TTypeDesc(
                            types=[
                                TTypeNode(
                                    type=0,
                                    scalar_type=TScalarType(
                                        type=23,
                                        len=2147483643,
                                        precision=None,
                                        scale=None,
                                        variant_max_subcolumns_count=0,
                                    ),
                                    struct_fields=None,
                                    contains_null=None,
                                    contains_nulls=None,
                                )
                            ],
                            is_nullable=None,
                            byte_size=-1,
                            sub_types=None,
                            result_is_nullable=None,
                            function_name=None,
                            be_exec_version=None,
                        ),
                        columnPos=-1,
                        byteOffset=-1,
                        nullIndicatorByte=0,
                        nullIndicatorBit=0,
                        colName="name",
                        slotIdx=1,
                        isMaterialized=True,
                        col_unique_id=-1,
                        is_key=False,
                        need_materialize=True,
                        is_auto_increment=False,
                        column_paths=None,
                        col_default_value=None,
                        primitive_type=23,
                        virtual_column_expr=None,
                    ),
                    TSlotDescriptor(
                        id=4,
                        parent=2,
                        slotType=TTypeDesc(
                            types=[
                                TTypeNode(
                                    type=0,
                                    scalar_type=TScalarType(
                                        type=5,
                                        len=None,
                                        precision=None,
                                        scale=None,
                                        variant_max_subcolumns_count=0,
                                    ),
                                    struct_fields=None,
                                    contains_null=None,
                                    contains_nulls=None,
                                )
                            ],
                            is_nullable=None,
                            byte_size=-1,
                            sub_types=None,
                            result_is_nullable=None,
                            function_name=None,
                            be_exec_version=None,
                        ),
                        columnPos=-1,
                        byteOffset=-1,
                        nullIndicatorByte=0,
                        nullIndicatorBit=0,
                        colName="id",
                        slotIdx=0,
                        isMaterialized=True,
                        col_unique_id=-1,
                        is_key=False,
                        need_materialize=True,
                        is_auto_increment=False,
                        column_paths=None,
                        col_default_value=None,
                        primitive_type=5,
                        virtual_column_expr=None,
                    ),
                    TSlotDescriptor(
                        id=5,
                        parent=2,
                        slotType=TTypeDesc(
                            types=[
                                TTypeNode(
                                    type=0,
                                    scalar_type=TScalarType(
                                        type=23,
                                        len=2147483643,
                                        precision=None,
                                        scale=None,
                                        variant_max_subcolumns_count=0,
                                    ),
                                    struct_fields=None,
                                    contains_null=None,
                                    contains_nulls=None,
                                )
                            ],
                            is_nullable=None,
                            byte_size=-1,
                            sub_types=None,
                            result_is_nullable=None,
                            function_name=None,
                            be_exec_version=None,
                        ),
                        columnPos=-1,
                        byteOffset=-1,
                        nullIndicatorByte=0,
                        nullIndicatorBit=0,
                        colName="name",
                        slotIdx=3,
                        isMaterialized=True,
                        col_unique_id=-1,
                        is_key=False,
                        need_materialize=True,
                        is_auto_increment=False,
                        column_paths=None,
                        col_default_value=None,
                        primitive_type=23,
                        virtual_column_expr=None,
                    ),
                    TSlotDescriptor(
                        id=6,
                        parent=2,
                        slotType=TTypeDesc(
                            types=[
                                TTypeNode(
                                    type=0,
                                    scalar_type=TScalarType(
                                        type=5,
                                        len=None,
                                        precision=None,
                                        scale=None,
                                        variant_max_subcolumns_count=0,
                                    ),
                                    struct_fields=None,
                                    contains_null=None,
                                    contains_nulls=None,
                                )
                            ],
                            is_nullable=None,
                            byte_size=-1,
                            sub_types=None,
                            result_is_nullable=None,
                            function_name=None,
                            be_exec_version=None,
                        ),
                        columnPos=-1,
                        byteOffset=-1,
                        nullIndicatorByte=0,
                        nullIndicatorBit=0,
                        colName="id",
                        slotIdx=1,
                        isMaterialized=True,
                        col_unique_id=-1,
                        is_key=False,
                        need_materialize=True,
                        is_auto_increment=False,
                        column_paths=None,
                        col_default_value=None,
                        primitive_type=5,
                        virtual_column_expr=None,
                    ),
                    TSlotDescriptor(
                        id=7,
                        parent=2,
                        slotType=TTypeDesc(
                            types=[
                                TTypeNode(
                                    type=0,
                                    scalar_type=TScalarType(
                                        type=5,
                                        len=None,
                                        precision=None,
                                        scale=None,
                                        variant_max_subcolumns_count=0,
                                    ),
                                    struct_fields=None,
                                    contains_null=None,
                                    contains_nulls=None,
                                )
                            ],
                            is_nullable=None,
                            byte_size=-1,
                            sub_types=None,
                            result_is_nullable=None,
                            function_name=None,
                            be_exec_version=None,
                        ),
                        columnPos=-1,
                        byteOffset=-1,
                        nullIndicatorByte=0,
                        nullIndicatorBit=0,
                        colName="age",
                        slotIdx=2,
                        isMaterialized=True,
                        col_unique_id=-1,
                        is_key=False,
                        need_materialize=True,
                        is_auto_increment=False,
                        column_paths=None,
                        col_default_value=None,
                        primitive_type=5,
                        virtual_column_expr=None,
                    ),
                    TSlotDescriptor(
                        id=8,
                        parent=3,
                        slotType=TTypeDesc(
                            types=[
                                TTypeNode(
                                    type=0,
                                    scalar_type=TScalarType(
                                        type=23,
                                        len=2147483643,
                                        precision=None,
                                        scale=None,
                                        variant_max_subcolumns_count=0,
                                    ),
                                    struct_fields=None,
                                    contains_null=None,
                                    contains_nulls=None,
                                )
                            ],
                            is_nullable=None,
                            byte_size=-1,
                            sub_types=None,
                            result_is_nullable=None,
                            function_name=None,
                            be_exec_version=None,
                        ),
                        columnPos=-1,
                        byteOffset=-1,
                        nullIndicatorByte=0,
                        nullIndicatorBit=0,
                        colName="name",
                        slotIdx=1,
                        isMaterialized=True,
                        col_unique_id=-1,
                        is_key=False,
                        need_materialize=True,
                        is_auto_increment=False,
                        column_paths=None,
                        col_default_value=None,
                        primitive_type=23,
                        virtual_column_expr=None,
                    ),
                    TSlotDescriptor(
                        id=9,
                        parent=3,
                        slotType=TTypeDesc(
                            types=[
                                TTypeNode(
                                    type=0,
                                    scalar_type=TScalarType(
                                        type=5,
                                        len=None,
                                        precision=None,
                                        scale=None,
                                        variant_max_subcolumns_count=0,
                                    ),
                                    struct_fields=None,
                                    contains_null=None,
                                    contains_nulls=None,
                                )
                            ],
                            is_nullable=None,
                            byte_size=-1,
                            sub_types=None,
                            result_is_nullable=None,
                            function_name=None,
                            be_exec_version=None,
                        ),
                        columnPos=-1,
                        byteOffset=-1,
                        nullIndicatorByte=0,
                        nullIndicatorBit=0,
                        colName="age",
                        slotIdx=0,
                        isMaterialized=True,
                        col_unique_id=-1,
                        is_key=False,
                        need_materialize=True,
                        is_auto_increment=False,
                        column_paths=None,
                        col_default_value=None,
                        primitive_type=5,
                        virtual_column_expr=None,
                    ),
                ],
                tupleDescriptors=[
                    TTupleDescriptor(
                        id=0,
                        byteSize=0,
                        numNullBytes=0,
                        tableId=None,
                        numNullSlots=None,
                    ),
                    TTupleDescriptor(
                        id=1,
                        byteSize=0,
                        numNullBytes=0,
                        tableId=None,
                        numNullSlots=None,
                    ),
                    TTupleDescriptor(
                        id=2,
                        byteSize=0,
                        numNullBytes=0,
                        tableId=None,
                        numNullSlots=None,
                    ),
                    TTupleDescriptor(
                        id=3,
                        byteSize=0,
                        numNullBytes=0,
                        tableId=None,
                        numNullSlots=None,
                    ),
                ],
                tableDescriptors=None,
            ),
            resource_info=None,
            destinations=[],
            num_senders=56,
            send_query_statistics_with_every_batch=False,
            coord=TNetworkAddress(hostname="192.168.30.126", port=9020),
            query_globals=TQueryGlobals(
                now_string="2025-11-06 23:58:01",
                timestamp_ms=1762444681758,
                time_zone="Asia/Shanghai",
                load_zero_tolerance=False,
                nano_seconds=758576956,
                lc_time_names=None,
            ),
            query_options=TQueryOptions(
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
                mem_limit=100147483648,
                abort_on_default_limit_exceeded=False,
                query_timeout=900,
                is_report_success=True,
                codegen_level=0,
                kudu_latest_observed_ts=9223372036854775807,
                query_type=0,
                min_reservation=0,
                max_reservation=107374182400,
                initial_reservation_total_claims=2147483647,
                buffer_pool_limit=2147483648,
                default_spillable_buffer_size=2097152,
                min_spillable_buffer_size=65536,
                max_row_size=524288,
                disable_stream_preaggregations=False,
                mt_dop=0,
                load_mem_limit=0,
                max_scan_key_num=48,
                max_pushdown_conditions_per_column=1024,
                enable_spilling=False,
                enable_enable_exchange_node_parallel_merge=False,
                runtime_filter_wait_time_ms=1000,
                runtime_filter_max_in_num=40960,
                resource_limit=None,
                return_object_data_as_binary=False,
                trim_tailing_spaces_for_external_table_query=False,
                enable_function_pushdown=False,
                fragment_transmission_compression_codec="none",
                enable_local_exchange=True,
                skip_storage_engine_merge=False,
                skip_delete_predicate=False,
                enable_new_shuffle_hash_method=None,
                be_exec_version=8,
                partitioned_hash_join_rows_threshold=0,
                enable_share_hash_table_for_broadcast_join=True,
                check_overflow_for_decimal=True,
                skip_delete_bitmap=False,
                enable_pipeline_engine=True,
                repeat_max_num=0,
                external_sort_bytes_threshold=0,
                partitioned_hash_agg_rows_threshold=0,
                enable_file_cache=False,
                insert_timeout=14400,
                execution_timeout=3,
                dry_run_query=False,
                enable_common_expr_pushdown=True,
                parallel_instance=56,
                mysql_row_binary_format=False,
                external_agg_bytes_threshold=0,
                external_agg_partition_bits=4,
                file_cache_base_path="random",
                enable_parquet_lazy_mat=True,
                enable_orc_lazy_mat=True,
                scan_queue_mem_limit=107374182,
                enable_scan_node_run_serial=False,
                enable_insert_strict=True,
                enable_inverted_index_query=True,
                truncate_char_or_varchar_columns=False,
                enable_hash_join_early_start_probe=False,
                enable_pipeline_x_engine=True,
                enable_memtable_on_sink_node=True,
                enable_delete_sub_predicate_v2=False,
                fe_process_uuid=1762444564496,
                inverted_index_conjunction_opt_threshold=1000,
                enable_profile=True,
                enable_page_cache=True,
                analyze_timeout=43200,
                faster_float_convert=False,
                enable_decimal256=False,
                enable_local_shuffle=True,
                skip_missing_version=False,
                runtime_filter_wait_infinitely=False,
                condition_cache_digest=0,
                inverted_index_max_expansions=50,
                inverted_index_skip_threshold=50,
                enable_parallel_scan=True,
                parallel_scan_max_scanners_count=0,
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
                enable_common_expr_pushdown_for_inverted_index=True,
                local_exchange_free_blocks_limit=4,
                enable_force_spill=False,
                enable_parquet_filter_by_min_max=True,
                enable_orc_filter_by_min_max=True,
                max_column_reader_num=20000,
                enable_local_merge_sort=False,
                enable_parallel_result_sink=True,
                enable_short_circuit_query_access_column_store=True,
                enable_no_need_read_data_opt=True,
                read_csv_empty_line_as_null=False,
                serde_dialect=0,
                enable_match_without_inverted_index=True,
                enable_fallback_on_missing_inverted_index=True,
                keep_carriage_return=False,
                runtime_bloom_filter_min_size=1048576,
                hive_parquet_use_column_names=True,
                hive_orc_use_column_names=True,
                enable_segment_cache=True,
                runtime_bloom_filter_max_size=67108864,
                in_list_value_count_threshold=10,
                enable_verbose_profile=False,
                rpc_verbose_profile_max_instance_count=5,
                enable_adaptive_pipeline_task_serial_read_on_limit=True,
                adaptive_pipeline_task_serial_read_on_limit=10000,
                parallel_prepare_threshold=32,
                partition_topn_max_partitions=1024,
                partition_topn_pre_partition_rows=1000,
                enable_parallel_outfile=False,
                enable_phrase_query_sequential_opt=True,
                enable_auto_create_when_overwrite=False,
                orc_tiny_stripe_threshold_bytes=8388608,
                orc_once_max_read_bytes=8388608,
                orc_max_merge_distance_bytes=1048576,
                ignore_runtime_filter_error=False,
                enable_fixed_len_to_uint32_v2=False,
                enable_shared_exchange_sink_buffer=True,
                enable_inverted_index_searcher_cache=True,
                enable_inverted_index_query_cache=True,
                enable_condition_cache=False,
                profile_level=1,
                min_scanner_concurrency=1,
                min_scan_scheduler_concurrency=0,
                enable_runtime_filter_partition_prune=True,
                minimum_operator_memory_required_kb=1000,
                enable_mem_overcommit=True,
                query_slot_count=1,
                enable_spill=False,
                enable_reserve_memory=True,
                revocable_memory_high_watermark_percent=-1,
                spill_sort_mem_limit=134217728,
                spill_sort_batch_bytes=8388608,
                spill_aggregation_partition_count=32,
                spill_hash_join_partition_count=32,
                low_memory_mode_buffer_limit=33554432,
                dump_heap_profile_when_mem_limit_exceeded=False,
                inverted_index_compatible_read=False,
                check_orc_init_sargs_success=False,
                exchange_multi_blocks_byte_size=262144,
                enable_strict_cast=False,
                new_version_unix_timestamp=True,
                hnsw_ef_search=32,
                hnsw_check_relative_distance=True,
                hnsw_bounded_queue=True,
                optimize_index_scan_parallelism=True,
                enable_prefer_cached_rowset=False,
                query_freshness_tolerance_ms=-1,
                merge_read_slice_size=8388608,
                enable_fuzzy_blockable_task=False,
                shuffled_agg_ids=[],
                disable_file_cache=False,
            ),
            import_label=None,
            db_name=None,
            load_job_id=None,
            load_error_hub_info=None,
            fragment_num_on_host=168,
            backend_id=1761898803229,
            need_wait_execution_trigger=True,
            instances_sharing_hash_table=None,
            is_simplified_param=False,
            global_dict=None,
            fragment=TPlanFragment(
                plan=TPlan(
                    nodes=[
                        TPlanNode(
                            node_id=4,
                            node_type=4,
                            num_children=2,
                            limit=-1,
                            row_tuples=[1, 0],
                            nullable_tuples=[False, False],
                            conjuncts=None,
                            compact_data=False,
                            hash_join_node=THashJoinNode(
                                join_op=0,
                                eq_join_conjuncts=[
                                    TEqJoinCondition(
                                        left=TExpr(
                                            nodes=[
                                                TExprNode(
                                                    node_type=16,
                                                    type=TTypeDesc(
                                                        types=[
                                                            TTypeNode(
                                                                type=0,
                                                                scalar_type=TScalarType(
                                                                    type=5,
                                                                    len=None,
                                                                    precision=None,
                                                                    scale=None,
                                                                    variant_max_subcolumns_count=0,
                                                                ),
                                                                struct_fields=None,
                                                                contains_null=None,
                                                                contains_nulls=None,
                                                            )
                                                        ],
                                                        is_nullable=None,
                                                        byte_size=-1,
                                                        sub_types=None,
                                                        result_is_nullable=None,
                                                        function_name=None,
                                                        be_exec_version=None,
                                                    ),
                                                    opcode=None,
                                                    num_children=0,
                                                    agg_expr=None,
                                                    bool_literal=None,
                                                    case_expr=None,
                                                    date_literal=None,
                                                    float_literal=None,
                                                    int_literal=None,
                                                    in_predicate=None,
                                                    is_null_pred=None,
                                                    like_pred=None,
                                                    literal_pred=None,
                                                    slot_ref=TSlotRef(
                                                        slot_id=2,
                                                        tuple_id=1,
                                                        col_unique_id=-1,
                                                        is_virtual_slot=False,
                                                    ),
                                                    string_literal=None,
                                                    tuple_is_null_pred=None,
                                                    info_func=None,
                                                    decimal_literal=None,
                                                    output_scale=-1,
                                                    fn_call_expr=None,
                                                    large_int_literal=None,
                                                    output_column=None,
                                                    output_type=None,
                                                    vector_opcode=None,
                                                    fn=None,
                                                    vararg_start_idx=None,
                                                    child_type=None,
                                                    is_nullable=True,
                                                    json_literal=None,
                                                    schema_change_expr=None,
                                                    column_ref=None,
                                                    match_predicate=None,
                                                    ipv4_literal=None,
                                                    ipv6_literal=None,
                                                    label="_table_valued_function_file.id",
                                                    timev2_literal=None,
                                                    varbinary_literal=None,
                                                    is_cast_nullable=None,
                                                    search_param=None,
                                                )
                                            ]
                                        ),
                                        right=TExpr(
                                            nodes=[
                                                TExprNode(
                                                    node_type=16,
                                                    type=TTypeDesc(
                                                        types=[
                                                            TTypeNode(
                                                                type=0,
                                                                scalar_type=TScalarType(
                                                                    type=5,
                                                                    len=None,
                                                                    precision=None,
                                                                    scale=None,
                                                                    variant_max_subcolumns_count=0,
                                                                ),
                                                                struct_fields=None,
                                                                contains_null=None,
                                                                contains_nulls=None,
                                                            )
                                                        ],
                                                        is_nullable=None,
                                                        byte_size=-1,
                                                        sub_types=None,
                                                        result_is_nullable=None,
                                                        function_name=None,
                                                        be_exec_version=None,
                                                    ),
                                                    opcode=None,
                                                    num_children=0,
                                                    agg_expr=None,
                                                    bool_literal=None,
                                                    case_expr=None,
                                                    date_literal=None,
                                                    float_literal=None,
                                                    int_literal=None,
                                                    in_predicate=None,
                                                    is_null_pred=None,
                                                    like_pred=None,
                                                    literal_pred=None,
                                                    slot_ref=TSlotRef(
                                                        slot_id=0,
                                                        tuple_id=0,
                                                        col_unique_id=-1,
                                                        is_virtual_slot=False,
                                                    ),
                                                    string_literal=None,
                                                    tuple_is_null_pred=None,
                                                    info_func=None,
                                                    decimal_literal=None,
                                                    output_scale=-1,
                                                    fn_call_expr=None,
                                                    large_int_literal=None,
                                                    output_column=None,
                                                    output_type=None,
                                                    vector_opcode=None,
                                                    fn=None,
                                                    vararg_start_idx=None,
                                                    child_type=None,
                                                    is_nullable=True,
                                                    json_literal=None,
                                                    schema_change_expr=None,
                                                    column_ref=None,
                                                    match_predicate=None,
                                                    ipv4_literal=None,
                                                    ipv6_literal=None,
                                                    label="_table_valued_function_file.id",
                                                    timev2_literal=None,
                                                    varbinary_literal=None,
                                                    is_cast_nullable=None,
                                                    search_param=None,
                                                )
                                            ]
                                        ),
                                        opcode=9,
                                    )
                                ],
                                other_join_conjuncts=None,
                                add_probe_filters=None,
                                vother_join_conjunct=None,
                                hash_output_slot_ids=[1, 3],
                                srcExprList=None,
                                voutput_tuple_id=None,
                                vintermediate_tuple_id_list=[2],
                                is_broadcast_join=False,
                                is_mark=False,
                                dist_type=2,
                                mark_join_conjuncts=None,
                                use_specific_projections=None,
                            ),
                            agg_node=None,
                            sort_node=None,
                            merge_node=None,
                            exchange_node=None,
                            mysql_scan_node=None,
                            olap_scan_node=None,
                            csv_scan_node=None,
                            broker_scan_node=None,
                            pre_agg_node=None,
                            schema_scan_node=None,
                            merge_join_node=None,
                            meta_scan_node=None,
                            analytic_node=None,
                            olap_rewrite_node=None,
                            union_node=None,
                            resource_profile=None,
                            es_scan_node=None,
                            repeat_node=None,
                            assert_num_rows_node=None,
                            intersect_node=None,
                            except_node=None,
                            odbc_scan_node=None,
                            runtime_filters=None,
                            group_commit_scan_node=None,
                            materialization_node=None,
                            vconjunct=None,
                            table_function_node=None,
                            output_slot_ids=None,
                            data_gen_scan_node=None,
                            file_scan_node=None,
                            jdbc_scan_node=None,
                            nested_loop_join_node=None,
                            test_external_scan_node=None,
                            push_down_agg_type_opt=None,
                            push_down_count=None,
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
                                                                type=5,
                                                                len=None,
                                                                precision=None,
                                                                scale=None,
                                                                variant_max_subcolumns_count=0,
                                                            ),
                                                            struct_fields=None,
                                                            contains_null=None,
                                                            contains_nulls=None,
                                                        )
                                                    ],
                                                    is_nullable=None,
                                                    byte_size=-1,
                                                    sub_types=None,
                                                    result_is_nullable=None,
                                                    function_name=None,
                                                    be_exec_version=None,
                                                ),
                                                opcode=None,
                                                num_children=0,
                                                agg_expr=None,
                                                bool_literal=None,
                                                case_expr=None,
                                                date_literal=None,
                                                float_literal=None,
                                                int_literal=None,
                                                in_predicate=None,
                                                is_null_pred=None,
                                                like_pred=None,
                                                literal_pred=None,
                                                slot_ref=TSlotRef(
                                                    slot_id=2,
                                                    tuple_id=1,
                                                    col_unique_id=-1,
                                                    is_virtual_slot=False,
                                                ),
                                                string_literal=None,
                                                tuple_is_null_pred=None,
                                                info_func=None,
                                                decimal_literal=None,
                                                output_scale=-1,
                                                fn_call_expr=None,
                                                large_int_literal=None,
                                                output_column=None,
                                                output_type=None,
                                                vector_opcode=None,
                                                fn=None,
                                                vararg_start_idx=None,
                                                child_type=None,
                                                is_nullable=True,
                                                json_literal=None,
                                                schema_change_expr=None,
                                                column_ref=None,
                                                match_predicate=None,
                                                ipv4_literal=None,
                                                ipv6_literal=None,
                                                label="_table_valued_function_file.id",
                                                timev2_literal=None,
                                                varbinary_literal=None,
                                                is_cast_nullable=None,
                                                search_param=None,
                                            )
                                        ]
                                    )
                                ],
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
                                                                type=5,
                                                                len=None,
                                                                precision=None,
                                                                scale=None,
                                                                variant_max_subcolumns_count=0,
                                                            ),
                                                            struct_fields=None,
                                                            contains_null=None,
                                                            contains_nulls=None,
                                                        )
                                                    ],
                                                    is_nullable=None,
                                                    byte_size=-1,
                                                    sub_types=None,
                                                    result_is_nullable=None,
                                                    function_name=None,
                                                    be_exec_version=None,
                                                ),
                                                opcode=None,
                                                num_children=0,
                                                agg_expr=None,
                                                bool_literal=None,
                                                case_expr=None,
                                                date_literal=None,
                                                float_literal=None,
                                                int_literal=None,
                                                in_predicate=None,
                                                is_null_pred=None,
                                                like_pred=None,
                                                literal_pred=None,
                                                slot_ref=TSlotRef(
                                                    slot_id=0,
                                                    tuple_id=0,
                                                    col_unique_id=-1,
                                                    is_virtual_slot=False,
                                                ),
                                                string_literal=None,
                                                tuple_is_null_pred=None,
                                                info_func=None,
                                                decimal_literal=None,
                                                output_scale=-1,
                                                fn_call_expr=None,
                                                large_int_literal=None,
                                                output_column=None,
                                                output_type=None,
                                                vector_opcode=None,
                                                fn=None,
                                                vararg_start_idx=None,
                                                child_type=None,
                                                is_nullable=True,
                                                json_literal=None,
                                                schema_change_expr=None,
                                                column_ref=None,
                                                match_predicate=None,
                                                ipv4_literal=None,
                                                ipv6_literal=None,
                                                label="_table_valued_function_file.id",
                                                timev2_literal=None,
                                                varbinary_literal=None,
                                                is_cast_nullable=None,
                                                search_param=None,
                                            )
                                        ]
                                    )
                                ],
                            ],
                            is_serial_operator=False,
                            projections=[
                                TExpr(
                                    nodes=[
                                        TExprNode(
                                            node_type=16,
                                            type=TTypeDesc(
                                                types=[
                                                    TTypeNode(
                                                        type=0,
                                                        scalar_type=TScalarType(
                                                            type=23,
                                                            len=2147483643,
                                                            precision=None,
                                                            scale=None,
                                                            variant_max_subcolumns_count=0,
                                                        ),
                                                        struct_fields=None,
                                                        contains_null=None,
                                                        contains_nulls=None,
                                                    )
                                                ],
                                                is_nullable=None,
                                                byte_size=-1,
                                                sub_types=None,
                                                result_is_nullable=None,
                                                function_name=None,
                                                be_exec_version=None,
                                            ),
                                            opcode=None,
                                            num_children=0,
                                            agg_expr=None,
                                            bool_literal=None,
                                            case_expr=None,
                                            date_literal=None,
                                            float_literal=None,
                                            int_literal=None,
                                            in_predicate=None,
                                            is_null_pred=None,
                                            like_pred=None,
                                            literal_pred=None,
                                            slot_ref=TSlotRef(
                                                slot_id=5,
                                                tuple_id=2,
                                                col_unique_id=-1,
                                                is_virtual_slot=False,
                                            ),
                                            string_literal=None,
                                            tuple_is_null_pred=None,
                                            info_func=None,
                                            decimal_literal=None,
                                            output_scale=-1,
                                            fn_call_expr=None,
                                            large_int_literal=None,
                                            output_column=None,
                                            output_type=None,
                                            vector_opcode=None,
                                            fn=None,
                                            vararg_start_idx=None,
                                            child_type=None,
                                            is_nullable=True,
                                            json_literal=None,
                                            schema_change_expr=None,
                                            column_ref=None,
                                            match_predicate=None,
                                            ipv4_literal=None,
                                            ipv6_literal=None,
                                            label="name",
                                            timev2_literal=None,
                                            varbinary_literal=None,
                                            is_cast_nullable=None,
                                            search_param=None,
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
                                                            len=None,
                                                            precision=None,
                                                            scale=None,
                                                            variant_max_subcolumns_count=0,
                                                        ),
                                                        struct_fields=None,
                                                        contains_null=None,
                                                        contains_nulls=None,
                                                    )
                                                ],
                                                is_nullable=None,
                                                byte_size=-1,
                                                sub_types=None,
                                                result_is_nullable=None,
                                                function_name=None,
                                                be_exec_version=None,
                                            ),
                                            opcode=None,
                                            num_children=0,
                                            agg_expr=None,
                                            bool_literal=None,
                                            case_expr=None,
                                            date_literal=None,
                                            float_literal=None,
                                            int_literal=None,
                                            in_predicate=None,
                                            is_null_pred=None,
                                            like_pred=None,
                                            literal_pred=None,
                                            slot_ref=TSlotRef(
                                                slot_id=7,
                                                tuple_id=2,
                                                col_unique_id=-1,
                                                is_virtual_slot=False,
                                            ),
                                            string_literal=None,
                                            tuple_is_null_pred=None,
                                            info_func=None,
                                            decimal_literal=None,
                                            output_scale=-1,
                                            fn_call_expr=None,
                                            large_int_literal=None,
                                            output_column=None,
                                            output_type=None,
                                            vector_opcode=None,
                                            fn=None,
                                            vararg_start_idx=None,
                                            child_type=None,
                                            is_nullable=True,
                                            json_literal=None,
                                            schema_change_expr=None,
                                            column_ref=None,
                                            match_predicate=None,
                                            ipv4_literal=None,
                                            ipv6_literal=None,
                                            label="age",
                                            timev2_literal=None,
                                            varbinary_literal=None,
                                            is_cast_nullable=None,
                                            search_param=None,
                                        )
                                    ]
                                ),
                            ],
                            output_tuple_id=3,
                            partition_sort_node=None,
                            intermediate_projections_list=None,
                            intermediate_output_tuple_id_list=None,
                            topn_filter_source_node_ids=None,
                            nereids_id=179,
                        ),
                        TPlanNode(
                            node_id=3,
                            node_type=9,
                            num_children=0,
                            limit=-1,
                            row_tuples=[1],
                            nullable_tuples=[False],
                            conjuncts=None,
                            compact_data=False,
                            hash_join_node=None,
                            agg_node=None,
                            sort_node=None,
                            merge_node=None,
                            exchange_node=TExchangeNode(
                                input_row_tuples=[1],
                                sort_info=None,
                                offset=0,
                                partition_type=2,
                            ),
                            mysql_scan_node=None,
                            olap_scan_node=None,
                            csv_scan_node=None,
                            broker_scan_node=None,
                            pre_agg_node=None,
                            schema_scan_node=None,
                            merge_join_node=None,
                            meta_scan_node=None,
                            analytic_node=None,
                            olap_rewrite_node=None,
                            union_node=None,
                            resource_profile=None,
                            es_scan_node=None,
                            repeat_node=None,
                            assert_num_rows_node=None,
                            intersect_node=None,
                            except_node=None,
                            odbc_scan_node=None,
                            runtime_filters=None,
                            group_commit_scan_node=None,
                            materialization_node=None,
                            vconjunct=None,
                            table_function_node=None,
                            output_slot_ids=None,
                            data_gen_scan_node=None,
                            file_scan_node=None,
                            jdbc_scan_node=None,
                            nested_loop_join_node=None,
                            test_external_scan_node=None,
                            push_down_agg_type_opt=None,
                            push_down_count=None,
                            distribute_expr_lists=[[]],
                            is_serial_operator=False,
                            projections=None,
                            output_tuple_id=None,
                            partition_sort_node=None,
                            intermediate_projections_list=None,
                            intermediate_output_tuple_id_list=None,
                            topn_filter_source_node_ids=None,
                            nereids_id=-1,
                        ),
                        TPlanNode(
                            node_id=1,
                            node_type=9,
                            num_children=0,
                            limit=-1,
                            row_tuples=[0],
                            nullable_tuples=[False],
                            conjuncts=None,
                            compact_data=False,
                            hash_join_node=None,
                            agg_node=None,
                            sort_node=None,
                            merge_node=None,
                            exchange_node=TExchangeNode(
                                input_row_tuples=[0],
                                sort_info=None,
                                offset=0,
                                partition_type=2,
                            ),
                            mysql_scan_node=None,
                            olap_scan_node=None,
                            csv_scan_node=None,
                            broker_scan_node=None,
                            pre_agg_node=None,
                            schema_scan_node=None,
                            merge_join_node=None,
                            meta_scan_node=None,
                            analytic_node=None,
                            olap_rewrite_node=None,
                            union_node=None,
                            resource_profile=None,
                            es_scan_node=None,
                            repeat_node=None,
                            assert_num_rows_node=None,
                            intersect_node=None,
                            except_node=None,
                            odbc_scan_node=None,
                            runtime_filters=None,
                            group_commit_scan_node=None,
                            materialization_node=None,
                            vconjunct=None,
                            table_function_node=None,
                            output_slot_ids=None,
                            data_gen_scan_node=None,
                            file_scan_node=None,
                            jdbc_scan_node=None,
                            nested_loop_join_node=None,
                            test_external_scan_node=None,
                            push_down_agg_type_opt=None,
                            push_down_count=None,
                            distribute_expr_lists=[[]],
                            is_serial_operator=False,
                            projections=None,
                            output_tuple_id=None,
                            partition_sort_node=None,
                            intermediate_projections_list=None,
                            intermediate_output_tuple_id_list=None,
                            topn_filter_source_node_ids=None,
                            nereids_id=-1,
                        ),
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
                                                type=23,
                                                len=2147483643,
                                                precision=None,
                                                scale=None,
                                                variant_max_subcolumns_count=0,
                                            ),
                                            struct_fields=None,
                                            contains_null=None,
                                            contains_nulls=None,
                                        )
                                    ],
                                    is_nullable=None,
                                    byte_size=-1,
                                    sub_types=None,
                                    result_is_nullable=None,
                                    function_name=None,
                                    be_exec_version=None,
                                ),
                                opcode=None,
                                num_children=0,
                                agg_expr=None,
                                bool_literal=None,
                                case_expr=None,
                                date_literal=None,
                                float_literal=None,
                                int_literal=None,
                                in_predicate=None,
                                is_null_pred=None,
                                like_pred=None,
                                literal_pred=None,
                                slot_ref=TSlotRef(
                                    slot_id=8,
                                    tuple_id=3,
                                    col_unique_id=-1,
                                    is_virtual_slot=False,
                                ),
                                string_literal=None,
                                tuple_is_null_pred=None,
                                info_func=None,
                                decimal_literal=None,
                                output_scale=-1,
                                fn_call_expr=None,
                                large_int_literal=None,
                                output_column=None,
                                output_type=None,
                                vector_opcode=None,
                                fn=None,
                                vararg_start_idx=None,
                                child_type=None,
                                is_nullable=True,
                                json_literal=None,
                                schema_change_expr=None,
                                column_ref=None,
                                match_predicate=None,
                                ipv4_literal=None,
                                ipv6_literal=None,
                                label="name",
                                timev2_literal=None,
                                varbinary_literal=None,
                                is_cast_nullable=None,
                                search_param=None,
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
                                                len=None,
                                                precision=None,
                                                scale=None,
                                                variant_max_subcolumns_count=0,
                                            ),
                                            struct_fields=None,
                                            contains_null=None,
                                            contains_nulls=None,
                                        )
                                    ],
                                    is_nullable=None,
                                    byte_size=-1,
                                    sub_types=None,
                                    result_is_nullable=None,
                                    function_name=None,
                                    be_exec_version=None,
                                ),
                                opcode=None,
                                num_children=0,
                                agg_expr=None,
                                bool_literal=None,
                                case_expr=None,
                                date_literal=None,
                                float_literal=None,
                                int_literal=None,
                                in_predicate=None,
                                is_null_pred=None,
                                like_pred=None,
                                literal_pred=None,
                                slot_ref=TSlotRef(
                                    slot_id=9,
                                    tuple_id=3,
                                    col_unique_id=-1,
                                    is_virtual_slot=False,
                                ),
                                string_literal=None,
                                tuple_is_null_pred=None,
                                info_func=None,
                                decimal_literal=None,
                                output_scale=-1,
                                fn_call_expr=None,
                                large_int_literal=None,
                                output_column=None,
                                output_type=None,
                                vector_opcode=None,
                                fn=None,
                                vararg_start_idx=None,
                                child_type=None,
                                is_nullable=True,
                                json_literal=None,
                                schema_change_expr=None,
                                column_ref=None,
                                match_predicate=None,
                                ipv4_literal=None,
                                ipv6_literal=None,
                                label="age",
                                timev2_literal=None,
                                varbinary_literal=None,
                                is_cast_nullable=None,
                                search_param=None,
                            )
                        ]
                    ),
                ],
                output_sink=TDataSink(
                    type=1,
                    stream_sink=None,
                    result_sink=TResultSink(
                        type=0, file_options=None, fetch_option=None
                    ),
                    mysql_table_sink=None,
                    export_sink=None,
                    olap_table_sink=None,
                    memory_scratch_sink=None,
                    odbc_table_sink=None,
                    result_file_sink=None,
                    jdbc_table_sink=None,
                    multi_cast_stream_sink=None,
                    hive_table_sink=None,
                    iceberg_table_sink=None,
                    dictionary_sink=None,
                    blackhole_sink=None,
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
                                                    type=5,
                                                    len=None,
                                                    precision=None,
                                                    scale=None,
                                                    variant_max_subcolumns_count=0,
                                                ),
                                                struct_fields=None,
                                                contains_null=None,
                                                contains_nulls=None,
                                            )
                                        ],
                                        is_nullable=None,
                                        byte_size=-1,
                                        sub_types=None,
                                        result_is_nullable=None,
                                        function_name=None,
                                        be_exec_version=None,
                                    ),
                                    opcode=None,
                                    num_children=0,
                                    agg_expr=None,
                                    bool_literal=None,
                                    case_expr=None,
                                    date_literal=None,
                                    float_literal=None,
                                    int_literal=None,
                                    in_predicate=None,
                                    is_null_pred=None,
                                    like_pred=None,
                                    literal_pred=None,
                                    slot_ref=TSlotRef(
                                        slot_id=2,
                                        tuple_id=1,
                                        col_unique_id=-1,
                                        is_virtual_slot=False,
                                    ),
                                    string_literal=None,
                                    tuple_is_null_pred=None,
                                    info_func=None,
                                    decimal_literal=None,
                                    output_scale=-1,
                                    fn_call_expr=None,
                                    large_int_literal=None,
                                    output_column=None,
                                    output_type=None,
                                    vector_opcode=None,
                                    fn=None,
                                    vararg_start_idx=None,
                                    child_type=None,
                                    is_nullable=True,
                                    json_literal=None,
                                    schema_change_expr=None,
                                    column_ref=None,
                                    match_predicate=None,
                                    ipv4_literal=None,
                                    ipv6_literal=None,
                                    label="_table_valued_function_file.id",
                                    timev2_literal=None,
                                    varbinary_literal=None,
                                    is_cast_nullable=None,
                                    search_param=None,
                                )
                            ]
                        )
                    ],
                    partition_infos=None,
                ),
                min_reservation_bytes=0,
                initial_reservation_total_claims=0,
                query_cache_param=None,
            ),
            local_params=[
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349334
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=0,
                    runtime_filter_params=None,
                    backend_num=112,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349333
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=1,
                    runtime_filter_params=None,
                    backend_num=113,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349332
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=2,
                    runtime_filter_params=None,
                    backend_num=114,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349331
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=3,
                    runtime_filter_params=None,
                    backend_num=115,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349330
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=4,
                    runtime_filter_params=None,
                    backend_num=116,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349329
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=5,
                    runtime_filter_params=None,
                    backend_num=117,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349328
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=6,
                    runtime_filter_params=None,
                    backend_num=118,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349327
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=7,
                    runtime_filter_params=None,
                    backend_num=119,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349326
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=8,
                    runtime_filter_params=None,
                    backend_num=120,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349325
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=9,
                    runtime_filter_params=None,
                    backend_num=121,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349324
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=10,
                    runtime_filter_params=None,
                    backend_num=122,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349323
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=11,
                    runtime_filter_params=None,
                    backend_num=123,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349322
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=12,
                    runtime_filter_params=None,
                    backend_num=124,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349321
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=13,
                    runtime_filter_params=None,
                    backend_num=125,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349320
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=14,
                    runtime_filter_params=None,
                    backend_num=126,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349319
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=15,
                    runtime_filter_params=None,
                    backend_num=127,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349318
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=16,
                    runtime_filter_params=None,
                    backend_num=128,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349317
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=17,
                    runtime_filter_params=None,
                    backend_num=129,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349316
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=18,
                    runtime_filter_params=None,
                    backend_num=130,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349315
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=19,
                    runtime_filter_params=None,
                    backend_num=131,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349314
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=20,
                    runtime_filter_params=None,
                    backend_num=132,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349313
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=21,
                    runtime_filter_params=None,
                    backend_num=133,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349312
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=22,
                    runtime_filter_params=None,
                    backend_num=134,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349311
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=23,
                    runtime_filter_params=None,
                    backend_num=135,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349310
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=24,
                    runtime_filter_params=None,
                    backend_num=136,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349309
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=25,
                    runtime_filter_params=None,
                    backend_num=137,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349308
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=26,
                    runtime_filter_params=None,
                    backend_num=138,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349307
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=27,
                    runtime_filter_params=None,
                    backend_num=139,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349306
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=28,
                    runtime_filter_params=None,
                    backend_num=140,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349305
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=29,
                    runtime_filter_params=None,
                    backend_num=141,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349304
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=30,
                    runtime_filter_params=None,
                    backend_num=142,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349303
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=31,
                    runtime_filter_params=None,
                    backend_num=143,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349302
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=32,
                    runtime_filter_params=None,
                    backend_num=144,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349301
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=33,
                    runtime_filter_params=None,
                    backend_num=145,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349300
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=34,
                    runtime_filter_params=None,
                    backend_num=146,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349299
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=35,
                    runtime_filter_params=None,
                    backend_num=147,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349298
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=36,
                    runtime_filter_params=None,
                    backend_num=148,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349297
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=37,
                    runtime_filter_params=None,
                    backend_num=149,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349296
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=38,
                    runtime_filter_params=None,
                    backend_num=150,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349295
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=39,
                    runtime_filter_params=None,
                    backend_num=151,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349294
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=40,
                    runtime_filter_params=None,
                    backend_num=152,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349293
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=41,
                    runtime_filter_params=None,
                    backend_num=153,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349292
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=42,
                    runtime_filter_params=None,
                    backend_num=154,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349291
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=43,
                    runtime_filter_params=None,
                    backend_num=155,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349290
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=44,
                    runtime_filter_params=None,
                    backend_num=156,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349289
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=45,
                    runtime_filter_params=None,
                    backend_num=157,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349288
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=46,
                    runtime_filter_params=None,
                    backend_num=158,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349287
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=47,
                    runtime_filter_params=None,
                    backend_num=159,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349286
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=48,
                    runtime_filter_params=None,
                    backend_num=160,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349285
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=49,
                    runtime_filter_params=None,
                    backend_num=161,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349284
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=50,
                    runtime_filter_params=None,
                    backend_num=162,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349283
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=51,
                    runtime_filter_params=None,
                    backend_num=163,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349282
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=52,
                    runtime_filter_params=None,
                    backend_num=164,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349281
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=53,
                    runtime_filter_params=None,
                    backend_num=165,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349280
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=54,
                    runtime_filter_params=None,
                    backend_num=166,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349279
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=55,
                    runtime_filter_params=None,
                    backend_num=167,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
            ],
            workload_groups=[
                TPipelineWorkloadGroup(
                    id=1761898803267, name=None, properties=None, version=None
                )
            ],
            txn_conf=None,
            table_name=None,
            file_scan_params={
                0: TFileScanRangeParams(
                    file_type=None,
                    format_type=0,
                    compress_type=None,
                    src_tuple_id=-1,
                    dest_tuple_id=0,
                    num_of_columns_from_file=2,
                    required_slots=[
                        TFileScanSlotInfo(slot_id=0, is_file_slot=True),
                        TFileScanSlotInfo(slot_id=1, is_file_slot=True),
                    ],
                    hdfs_params=None,
                    properties=None,
                    expr_of_dest_slot=None,
                    default_value_of_src_slot={
                        0: TExpr(
                            nodes=[
                                TExprNode(
                                    node_type=15,
                                    type=TTypeDesc(
                                        types=[
                                            TTypeNode(
                                                type=0,
                                                scalar_type=TScalarType(
                                                    type=5,
                                                    len=None,
                                                    precision=None,
                                                    scale=None,
                                                    variant_max_subcolumns_count=0,
                                                ),
                                                struct_fields=None,
                                                contains_null=None,
                                                contains_nulls=None,
                                            )
                                        ],
                                        is_nullable=None,
                                        byte_size=-1,
                                        sub_types=None,
                                        result_is_nullable=None,
                                        function_name=None,
                                        be_exec_version=None,
                                    ),
                                    opcode=None,
                                    num_children=0,
                                    agg_expr=None,
                                    bool_literal=None,
                                    case_expr=None,
                                    date_literal=None,
                                    float_literal=None,
                                    int_literal=None,
                                    in_predicate=None,
                                    is_null_pred=None,
                                    like_pred=None,
                                    literal_pred=None,
                                    slot_ref=None,
                                    string_literal=None,
                                    tuple_is_null_pred=None,
                                    info_func=None,
                                    decimal_literal=None,
                                    output_scale=-1,
                                    fn_call_expr=None,
                                    large_int_literal=None,
                                    output_column=None,
                                    output_type=None,
                                    vector_opcode=None,
                                    fn=None,
                                    vararg_start_idx=None,
                                    child_type=None,
                                    is_nullable=True,
                                    json_literal=None,
                                    schema_change_expr=None,
                                    column_ref=None,
                                    match_predicate=None,
                                    ipv4_literal=None,
                                    ipv6_literal=None,
                                    label=None,
                                    timev2_literal=None,
                                    varbinary_literal=None,
                                    is_cast_nullable=None,
                                    search_param=None,
                                )
                            ]
                        ),
                        1: TExpr(
                            nodes=[
                                TExprNode(
                                    node_type=15,
                                    type=TTypeDesc(
                                        types=[
                                            TTypeNode(
                                                type=0,
                                                scalar_type=TScalarType(
                                                    type=5,
                                                    len=None,
                                                    precision=None,
                                                    scale=None,
                                                    variant_max_subcolumns_count=0,
                                                ),
                                                struct_fields=None,
                                                contains_null=None,
                                                contains_nulls=None,
                                            )
                                        ],
                                        is_nullable=None,
                                        byte_size=-1,
                                        sub_types=None,
                                        result_is_nullable=None,
                                        function_name=None,
                                        be_exec_version=None,
                                    ),
                                    opcode=None,
                                    num_children=0,
                                    agg_expr=None,
                                    bool_literal=None,
                                    case_expr=None,
                                    date_literal=None,
                                    float_literal=None,
                                    int_literal=None,
                                    in_predicate=None,
                                    is_null_pred=None,
                                    like_pred=None,
                                    literal_pred=None,
                                    slot_ref=None,
                                    string_literal=None,
                                    tuple_is_null_pred=None,
                                    info_func=None,
                                    decimal_literal=None,
                                    output_scale=-1,
                                    fn_call_expr=None,
                                    large_int_literal=None,
                                    output_column=None,
                                    output_type=None,
                                    vector_opcode=None,
                                    fn=None,
                                    vararg_start_idx=None,
                                    child_type=None,
                                    is_nullable=True,
                                    json_literal=None,
                                    schema_change_expr=None,
                                    column_ref=None,
                                    match_predicate=None,
                                    ipv4_literal=None,
                                    ipv6_literal=None,
                                    label=None,
                                    timev2_literal=None,
                                    varbinary_literal=None,
                                    is_cast_nullable=None,
                                    search_param=None,
                                )
                            ]
                        ),
                    },
                    dest_sid_to_src_sid_without_trans=None,
                    strict_mode=None,
                    broker_addresses=None,
                    file_attributes=TFileAttributes(
                        text_params=TFileTextScanRangeParams(
                            column_separator=",",
                            line_delimiter="\n",
                            collection_delimiter=None,
                            mapkv_delimiter=None,
                            enclose=0,
                            escape=0,
                            null_format=None,
                            empty_field_as_null=False,
                        ),
                        strip_outer_array=None,
                        jsonpaths=None,
                        json_root=None,
                        num_as_string=None,
                        fuzzy_parse=None,
                        read_json_by_line=None,
                        read_by_column_def=None,
                        header_type="",
                        trim_double_quotes=False,
                        skip_lines=0,
                        enable_text_validate_utf8=True,
                        openx_json_ignore_malformed=False,
                        ignore_csv_redundant_col=None,
                    ),
                    pre_filter_exprs=None,
                    table_format_params=None,
                    column_idxs=[0, 1],
                    slot_name_to_schema_pos=None,
                    pre_filter_exprs_list=None,
                    load_id=None,
                    text_serde_type=None,
                    sequence_map_col=None,
                    serialized_table=None,
                    current_schema_id=None,
                    history_schema_info=None,
                ),
                2: TFileScanRangeParams(
                    file_type=None,
                    format_type=0,
                    compress_type=None,
                    src_tuple_id=-1,
                    dest_tuple_id=1,
                    num_of_columns_from_file=2,
                    required_slots=[
                        TFileScanSlotInfo(slot_id=2, is_file_slot=True),
                        TFileScanSlotInfo(slot_id=3, is_file_slot=True),
                    ],
                    hdfs_params=None,
                    properties=None,
                    expr_of_dest_slot=None,
                    default_value_of_src_slot={
                        2: TExpr(
                            nodes=[
                                TExprNode(
                                    node_type=15,
                                    type=TTypeDesc(
                                        types=[
                                            TTypeNode(
                                                type=0,
                                                scalar_type=TScalarType(
                                                    type=5,
                                                    len=None,
                                                    precision=None,
                                                    scale=None,
                                                    variant_max_subcolumns_count=0,
                                                ),
                                                struct_fields=None,
                                                contains_null=None,
                                                contains_nulls=None,
                                            )
                                        ],
                                        is_nullable=None,
                                        byte_size=-1,
                                        sub_types=None,
                                        result_is_nullable=None,
                                        function_name=None,
                                        be_exec_version=None,
                                    ),
                                    opcode=None,
                                    num_children=0,
                                    agg_expr=None,
                                    bool_literal=None,
                                    case_expr=None,
                                    date_literal=None,
                                    float_literal=None,
                                    int_literal=None,
                                    in_predicate=None,
                                    is_null_pred=None,
                                    like_pred=None,
                                    literal_pred=None,
                                    slot_ref=None,
                                    string_literal=None,
                                    tuple_is_null_pred=None,
                                    info_func=None,
                                    decimal_literal=None,
                                    output_scale=-1,
                                    fn_call_expr=None,
                                    large_int_literal=None,
                                    output_column=None,
                                    output_type=None,
                                    vector_opcode=None,
                                    fn=None,
                                    vararg_start_idx=None,
                                    child_type=None,
                                    is_nullable=True,
                                    json_literal=None,
                                    schema_change_expr=None,
                                    column_ref=None,
                                    match_predicate=None,
                                    ipv4_literal=None,
                                    ipv6_literal=None,
                                    label=None,
                                    timev2_literal=None,
                                    varbinary_literal=None,
                                    is_cast_nullable=None,
                                    search_param=None,
                                )
                            ]
                        ),
                        3: TExpr(
                            nodes=[
                                TExprNode(
                                    node_type=15,
                                    type=TTypeDesc(
                                        types=[
                                            TTypeNode(
                                                type=0,
                                                scalar_type=TScalarType(
                                                    type=23,
                                                    len=2147483643,
                                                    precision=None,
                                                    scale=None,
                                                    variant_max_subcolumns_count=0,
                                                ),
                                                struct_fields=None,
                                                contains_null=None,
                                                contains_nulls=None,
                                            )
                                        ],
                                        is_nullable=None,
                                        byte_size=-1,
                                        sub_types=None,
                                        result_is_nullable=None,
                                        function_name=None,
                                        be_exec_version=None,
                                    ),
                                    opcode=None,
                                    num_children=0,
                                    agg_expr=None,
                                    bool_literal=None,
                                    case_expr=None,
                                    date_literal=None,
                                    float_literal=None,
                                    int_literal=None,
                                    in_predicate=None,
                                    is_null_pred=None,
                                    like_pred=None,
                                    literal_pred=None,
                                    slot_ref=None,
                                    string_literal=None,
                                    tuple_is_null_pred=None,
                                    info_func=None,
                                    decimal_literal=None,
                                    output_scale=-1,
                                    fn_call_expr=None,
                                    large_int_literal=None,
                                    output_column=None,
                                    output_type=None,
                                    vector_opcode=None,
                                    fn=None,
                                    vararg_start_idx=None,
                                    child_type=None,
                                    is_nullable=True,
                                    json_literal=None,
                                    schema_change_expr=None,
                                    column_ref=None,
                                    match_predicate=None,
                                    ipv4_literal=None,
                                    ipv6_literal=None,
                                    label=None,
                                    timev2_literal=None,
                                    varbinary_literal=None,
                                    is_cast_nullable=None,
                                    search_param=None,
                                )
                            ]
                        ),
                    },
                    dest_sid_to_src_sid_without_trans=None,
                    strict_mode=None,
                    broker_addresses=None,
                    file_attributes=TFileAttributes(
                        text_params=TFileTextScanRangeParams(
                            column_separator=",",
                            line_delimiter="\n",
                            collection_delimiter=None,
                            mapkv_delimiter=None,
                            enclose=0,
                            escape=0,
                            null_format=None,
                            empty_field_as_null=False,
                        ),
                        strip_outer_array=None,
                        jsonpaths=None,
                        json_root=None,
                        num_as_string=None,
                        fuzzy_parse=None,
                        read_json_by_line=None,
                        read_by_column_def=None,
                        header_type="",
                        trim_double_quotes=False,
                        skip_lines=0,
                        enable_text_validate_utf8=True,
                        openx_json_ignore_malformed=False,
                        ignore_csv_redundant_col=None,
                    ),
                    pre_filter_exprs=None,
                    table_format_params=None,
                    column_idxs=[0, 1],
                    slot_name_to_schema_pos=None,
                    pre_filter_exprs_list=None,
                    load_id=None,
                    text_serde_type=None,
                    sequence_map_col=None,
                    serialized_table=None,
                    current_schema_id=None,
                    history_schema_info=None,
                ),
            },
            group_commit=False,
            load_stream_per_node=None,
            total_load_streams=None,
            num_local_sink=None,
            num_buckets=None,
            bucket_seq_to_instance_idx=None,
            per_node_shared_scans=None,
            parallel_instances=None,
            total_instances=56,
            shuffle_idx_to_instance_idx={
                0: 0,
                1: 1,
                2: 2,
                3: 3,
                4: 4,
                5: 5,
                6: 6,
                7: 7,
                8: 8,
                9: 9,
                10: 10,
                11: 11,
                12: 12,
                13: 13,
                14: 14,
                15: 15,
                16: 16,
                17: 17,
                18: 18,
                19: 19,
                20: 20,
                21: 21,
                22: 22,
                23: 23,
                24: 24,
                25: 25,
                26: 26,
                27: 27,
                28: 28,
                29: 29,
                30: 30,
                31: 31,
                32: 32,
                33: 33,
                34: 34,
                35: 35,
                36: 36,
                37: 37,
                38: 38,
                39: 39,
                40: 40,
                41: 41,
                42: 42,
                43: 43,
                44: 44,
                45: 45,
                46: 46,
                47: 47,
                48: 48,
                49: 49,
                50: 50,
                51: 51,
                52: 52,
                53: 53,
                54: 54,
                55: 55,
            },
            is_nereids=True,
            wal_id=None,
            content_length=None,
            current_connect_fe=TNetworkAddress(hostname="192.168.30.126", port=9020),
            topn_filter_source_node_ids=None,
            ai_resources={},
            is_mow_table=None,
        ),
        TPipelineFragmentParams(
            protocol_version=0,
            query_id=query_id,
            fragment_id=2,
            per_exch_num_senders={},
            desc_tbl=None,
            resource_info=None,
            destinations=[
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349334
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349333
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349332
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349331
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349330
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349329
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349328
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349327
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349326
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349325
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349324
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349323
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349322
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349321
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349320
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349319
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349318
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349317
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349316
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349315
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349314
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349313
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349312
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349311
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349310
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349309
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349308
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349307
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349306
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349305
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349304
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349303
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349302
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349301
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349300
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349299
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349298
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349297
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349296
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349295
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349294
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349293
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349292
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349291
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349290
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349289
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349288
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349287
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349286
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349285
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349284
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349283
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349282
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349281
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349280
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349279
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
            ],
            num_senders=56,
            send_query_statistics_with_every_batch=False,
            coord=None,
            query_globals=None,
            query_options=TQueryOptions(
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
                mem_limit=100147483648,
                abort_on_default_limit_exceeded=False,
                query_timeout=900,
                is_report_success=True,
                codegen_level=0,
                kudu_latest_observed_ts=9223372036854775807,
                query_type=0,
                min_reservation=0,
                max_reservation=107374182400,
                initial_reservation_total_claims=2147483647,
                buffer_pool_limit=2147483648,
                default_spillable_buffer_size=2097152,
                min_spillable_buffer_size=65536,
                max_row_size=524288,
                disable_stream_preaggregations=False,
                mt_dop=0,
                load_mem_limit=0,
                max_scan_key_num=48,
                max_pushdown_conditions_per_column=1024,
                enable_spilling=False,
                enable_enable_exchange_node_parallel_merge=False,
                runtime_filter_wait_time_ms=1000,
                runtime_filter_max_in_num=40960,
                resource_limit=None,
                return_object_data_as_binary=False,
                trim_tailing_spaces_for_external_table_query=False,
                enable_function_pushdown=False,
                fragment_transmission_compression_codec="none",
                enable_local_exchange=True,
                skip_storage_engine_merge=False,
                skip_delete_predicate=False,
                enable_new_shuffle_hash_method=None,
                be_exec_version=8,
                partitioned_hash_join_rows_threshold=0,
                enable_share_hash_table_for_broadcast_join=True,
                check_overflow_for_decimal=True,
                skip_delete_bitmap=False,
                enable_pipeline_engine=True,
                repeat_max_num=0,
                external_sort_bytes_threshold=0,
                partitioned_hash_agg_rows_threshold=0,
                enable_file_cache=False,
                insert_timeout=14400,
                execution_timeout=900,
                dry_run_query=False,
                enable_common_expr_pushdown=True,
                parallel_instance=56,
                mysql_row_binary_format=False,
                external_agg_bytes_threshold=0,
                external_agg_partition_bits=4,
                file_cache_base_path="random",
                enable_parquet_lazy_mat=True,
                enable_orc_lazy_mat=True,
                scan_queue_mem_limit=107374182,
                enable_scan_node_run_serial=False,
                enable_insert_strict=True,
                enable_inverted_index_query=True,
                truncate_char_or_varchar_columns=False,
                enable_hash_join_early_start_probe=False,
                enable_pipeline_x_engine=True,
                enable_memtable_on_sink_node=True,
                enable_delete_sub_predicate_v2=False,
                fe_process_uuid=1762444564496,
                inverted_index_conjunction_opt_threshold=1000,
                enable_profile=True,
                enable_page_cache=True,
                analyze_timeout=43200,
                faster_float_convert=False,
                enable_decimal256=False,
                enable_local_shuffle=True,
                skip_missing_version=False,
                runtime_filter_wait_infinitely=False,
                condition_cache_digest=0,
                inverted_index_max_expansions=50,
                inverted_index_skip_threshold=50,
                enable_parallel_scan=True,
                parallel_scan_max_scanners_count=0,
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
                enable_common_expr_pushdown_for_inverted_index=True,
                local_exchange_free_blocks_limit=4,
                enable_force_spill=False,
                enable_parquet_filter_by_min_max=True,
                enable_orc_filter_by_min_max=True,
                max_column_reader_num=20000,
                enable_local_merge_sort=False,
                enable_parallel_result_sink=True,
                enable_short_circuit_query_access_column_store=True,
                enable_no_need_read_data_opt=True,
                read_csv_empty_line_as_null=False,
                serde_dialect=0,
                enable_match_without_inverted_index=True,
                enable_fallback_on_missing_inverted_index=True,
                keep_carriage_return=False,
                runtime_bloom_filter_min_size=1048576,
                hive_parquet_use_column_names=True,
                hive_orc_use_column_names=True,
                enable_segment_cache=True,
                runtime_bloom_filter_max_size=67108864,
                in_list_value_count_threshold=10,
                enable_verbose_profile=False,
                rpc_verbose_profile_max_instance_count=5,
                enable_adaptive_pipeline_task_serial_read_on_limit=True,
                adaptive_pipeline_task_serial_read_on_limit=10000,
                parallel_prepare_threshold=32,
                partition_topn_max_partitions=1024,
                partition_topn_pre_partition_rows=1000,
                enable_parallel_outfile=False,
                enable_phrase_query_sequential_opt=True,
                enable_auto_create_when_overwrite=False,
                orc_tiny_stripe_threshold_bytes=8388608,
                orc_once_max_read_bytes=8388608,
                orc_max_merge_distance_bytes=1048576,
                ignore_runtime_filter_error=False,
                enable_fixed_len_to_uint32_v2=False,
                enable_shared_exchange_sink_buffer=True,
                enable_inverted_index_searcher_cache=True,
                enable_inverted_index_query_cache=True,
                enable_condition_cache=False,
                profile_level=1,
                min_scanner_concurrency=1,
                min_scan_scheduler_concurrency=0,
                enable_runtime_filter_partition_prune=True,
                minimum_operator_memory_required_kb=1000,
                enable_mem_overcommit=True,
                query_slot_count=1,
                enable_spill=False,
                enable_reserve_memory=True,
                revocable_memory_high_watermark_percent=-1,
                spill_sort_mem_limit=134217728,
                spill_sort_batch_bytes=8388608,
                spill_aggregation_partition_count=32,
                spill_hash_join_partition_count=32,
                low_memory_mode_buffer_limit=33554432,
                dump_heap_profile_when_mem_limit_exceeded=False,
                inverted_index_compatible_read=False,
                check_orc_init_sargs_success=False,
                exchange_multi_blocks_byte_size=262144,
                enable_strict_cast=False,
                new_version_unix_timestamp=True,
                hnsw_ef_search=32,
                hnsw_check_relative_distance=True,
                hnsw_bounded_queue=True,
                optimize_index_scan_parallelism=True,
                enable_prefer_cached_rowset=False,
                query_freshness_tolerance_ms=-1,
                merge_read_slice_size=8388608,
                enable_fuzzy_blockable_task=False,
                shuffled_agg_ids=[],
                disable_file_cache=False,
            ),
            import_label=None,
            db_name=None,
            load_job_id=None,
            load_error_hub_info=None,
            fragment_num_on_host=168,
            backend_id=1761898803229,
            need_wait_execution_trigger=True,
            instances_sharing_hash_table=None,
            is_simplified_param=True,
            global_dict=None,
            fragment=TPlanFragment(
                plan=TPlan(
                    nodes=[
                        TPlanNode(
                            node_id=2,
                            node_type=29,
                            num_children=0,
                            limit=-1,
                            row_tuples=[1],
                            nullable_tuples=[False],
                            conjuncts=None,
                            compact_data=False,
                            hash_join_node=None,
                            agg_node=None,
                            sort_node=None,
                            merge_node=None,
                            exchange_node=None,
                            mysql_scan_node=None,
                            olap_scan_node=None,
                            csv_scan_node=None,
                            broker_scan_node=None,
                            pre_agg_node=None,
                            schema_scan_node=None,
                            merge_join_node=None,
                            meta_scan_node=None,
                            analytic_node=None,
                            olap_rewrite_node=None,
                            union_node=None,
                            resource_profile=None,
                            es_scan_node=None,
                            repeat_node=None,
                            assert_num_rows_node=None,
                            intersect_node=None,
                            except_node=None,
                            odbc_scan_node=None,
                            runtime_filters=None,
                            group_commit_scan_node=None,
                            materialization_node=None,
                            vconjunct=None,
                            table_function_node=None,
                            output_slot_ids=None,
                            data_gen_scan_node=None,
                            file_scan_node=TFileScanNode(
                                tuple_id=1, table_name="LocalTableValuedFunction"
                            ),
                            jdbc_scan_node=None,
                            nested_loop_join_node=None,
                            test_external_scan_node=None,
                            push_down_agg_type_opt=0,
                            push_down_count=None,
                            distribute_expr_lists=None,
                            is_serial_operator=True,
                            projections=None,
                            output_tuple_id=None,
                            partition_sort_node=None,
                            intermediate_projections_list=None,
                            intermediate_output_tuple_id_list=None,
                            topn_filter_source_node_ids=None,
                            nereids_id=166,
                        )
                    ]
                ),
                output_exprs=None,
                output_sink=TDataSink(
                    type=0,
                    stream_sink=TDataStreamSink(
                        dest_node_id=3,
                        output_partition=TDataPartition(
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
                                                            type=5,
                                                            len=None,
                                                            precision=None,
                                                            scale=None,
                                                            variant_max_subcolumns_count=0,
                                                        ),
                                                        struct_fields=None,
                                                        contains_null=None,
                                                        contains_nulls=None,
                                                    )
                                                ],
                                                is_nullable=None,
                                                byte_size=-1,
                                                sub_types=None,
                                                result_is_nullable=None,
                                                function_name=None,
                                                be_exec_version=None,
                                            ),
                                            opcode=None,
                                            num_children=0,
                                            agg_expr=None,
                                            bool_literal=None,
                                            case_expr=None,
                                            date_literal=None,
                                            float_literal=None,
                                            int_literal=None,
                                            in_predicate=None,
                                            is_null_pred=None,
                                            like_pred=None,
                                            literal_pred=None,
                                            slot_ref=TSlotRef(
                                                slot_id=2,
                                                tuple_id=1,
                                                col_unique_id=-1,
                                                is_virtual_slot=False,
                                            ),
                                            string_literal=None,
                                            tuple_is_null_pred=None,
                                            info_func=None,
                                            decimal_literal=None,
                                            output_scale=-1,
                                            fn_call_expr=None,
                                            large_int_literal=None,
                                            output_column=None,
                                            output_type=None,
                                            vector_opcode=None,
                                            fn=None,
                                            vararg_start_idx=None,
                                            child_type=None,
                                            is_nullable=True,
                                            json_literal=None,
                                            schema_change_expr=None,
                                            column_ref=None,
                                            match_predicate=None,
                                            ipv4_literal=None,
                                            ipv6_literal=None,
                                            label="_table_valued_function_file.id",
                                            timev2_literal=None,
                                            varbinary_literal=None,
                                            is_cast_nullable=None,
                                            search_param=None,
                                        )
                                    ]
                                )
                            ],
                            partition_infos=None,
                        ),
                        ignore_not_found=None,
                        output_exprs=None,
                        output_tuple_id=None,
                        conjuncts=None,
                        runtime_filters=None,
                        tablet_sink_schema=None,
                        tablet_sink_partition=None,
                        tablet_sink_location=None,
                        tablet_sink_txn_id=-1,
                        tablet_sink_tuple_id=None,
                        tablet_sink_exprs=None,
                        is_merge=False,
                    ),
                    result_sink=None,
                    mysql_table_sink=None,
                    export_sink=None,
                    olap_table_sink=None,
                    memory_scratch_sink=None,
                    odbc_table_sink=None,
                    result_file_sink=None,
                    jdbc_table_sink=None,
                    multi_cast_stream_sink=None,
                    hive_table_sink=None,
                    iceberg_table_sink=None,
                    dictionary_sink=None,
                    blackhole_sink=None,
                ),
                partition=TDataPartition(
                    type=1, partition_exprs=[], partition_infos=None
                ),
                min_reservation_bytes=0,
                initial_reservation_total_claims=0,
                query_cache_param=None,
            ),
            local_params=[
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349390
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={
                        2: [
                            TScanRangeParams(
                                scan_range=TScanRange(
                                    palo_scan_range=None,
                                    kudu_scan_token=None,
                                    broker_scan_range=None,
                                    es_scan_range=None,
                                    ext_scan_range=TExternalScanRange(
                                        file_scan_range=TFileScanRange(
                                            ranges=[
                                                TFileRangeDesc(
                                                    load_id=None,
                                                    path="/data11/chen/doris-latest/test.csv",
                                                    start_offset=0,
                                                    size=21,
                                                    file_size=21,
                                                    columns_from_path=[],
                                                    columns_from_path_keys=[],
                                                    table_format_params=TTableFormatFileDesc(
                                                        table_format_type="tvf",
                                                        iceberg_params=None,
                                                        hudi_params=None,
                                                        paimon_params=None,
                                                        transactional_hive_params=None,
                                                        max_compute_params=None,
                                                        trino_connector_params=None,
                                                        lakesoul_params=None,
                                                        table_level_row_count=-1,
                                                    ),
                                                    modification_time=0,
                                                    file_type=None,
                                                    compress_type=1,
                                                    fs_name=None,
                                                    format_type=0,
                                                    self_split_weight=None,
                                                    columns_from_path_is_null=None,
                                                )
                                            ],
                                            params=None,
                                            split_source=None,
                                        )
                                    ),
                                    data_gen_scan_range=None,
                                    meta_scan_range=None,
                                ),
                                volume_id=-1,
                            )
                        ]
                    },
                    sender_id=0,
                    runtime_filter_params=None,
                    backend_num=56,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349389
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=1,
                    runtime_filter_params=None,
                    backend_num=57,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349388
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=2,
                    runtime_filter_params=None,
                    backend_num=58,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349387
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=3,
                    runtime_filter_params=None,
                    backend_num=59,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349386
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=4,
                    runtime_filter_params=None,
                    backend_num=60,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349385
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=5,
                    runtime_filter_params=None,
                    backend_num=61,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349384
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=6,
                    runtime_filter_params=None,
                    backend_num=62,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349383
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=7,
                    runtime_filter_params=None,
                    backend_num=63,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349382
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=8,
                    runtime_filter_params=None,
                    backend_num=64,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349381
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=9,
                    runtime_filter_params=None,
                    backend_num=65,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349380
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=10,
                    runtime_filter_params=None,
                    backend_num=66,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349379
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=11,
                    runtime_filter_params=None,
                    backend_num=67,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349378
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=12,
                    runtime_filter_params=None,
                    backend_num=68,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349377
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=13,
                    runtime_filter_params=None,
                    backend_num=69,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349376
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=14,
                    runtime_filter_params=None,
                    backend_num=70,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349375
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=15,
                    runtime_filter_params=None,
                    backend_num=71,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349374
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=16,
                    runtime_filter_params=None,
                    backend_num=72,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349373
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=17,
                    runtime_filter_params=None,
                    backend_num=73,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349372
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=18,
                    runtime_filter_params=None,
                    backend_num=74,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349371
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=19,
                    runtime_filter_params=None,
                    backend_num=75,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349370
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=20,
                    runtime_filter_params=None,
                    backend_num=76,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349369
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=21,
                    runtime_filter_params=None,
                    backend_num=77,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349368
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=22,
                    runtime_filter_params=None,
                    backend_num=78,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349367
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=23,
                    runtime_filter_params=None,
                    backend_num=79,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349366
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=24,
                    runtime_filter_params=None,
                    backend_num=80,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349365
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=25,
                    runtime_filter_params=None,
                    backend_num=81,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349364
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=26,
                    runtime_filter_params=None,
                    backend_num=82,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349363
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=27,
                    runtime_filter_params=None,
                    backend_num=83,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349362
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=28,
                    runtime_filter_params=None,
                    backend_num=84,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349361
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=29,
                    runtime_filter_params=None,
                    backend_num=85,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349360
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=30,
                    runtime_filter_params=None,
                    backend_num=86,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349359
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=31,
                    runtime_filter_params=None,
                    backend_num=87,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349358
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=32,
                    runtime_filter_params=None,
                    backend_num=88,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349357
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=33,
                    runtime_filter_params=None,
                    backend_num=89,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349356
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=34,
                    runtime_filter_params=None,
                    backend_num=90,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349355
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=35,
                    runtime_filter_params=None,
                    backend_num=91,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349354
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=36,
                    runtime_filter_params=None,
                    backend_num=92,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349353
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=37,
                    runtime_filter_params=None,
                    backend_num=93,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349352
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=38,
                    runtime_filter_params=None,
                    backend_num=94,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349351
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=39,
                    runtime_filter_params=None,
                    backend_num=95,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349350
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=40,
                    runtime_filter_params=None,
                    backend_num=96,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349349
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=41,
                    runtime_filter_params=None,
                    backend_num=97,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349348
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=42,
                    runtime_filter_params=None,
                    backend_num=98,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349347
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=43,
                    runtime_filter_params=None,
                    backend_num=99,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349346
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=44,
                    runtime_filter_params=None,
                    backend_num=100,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349345
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=45,
                    runtime_filter_params=None,
                    backend_num=101,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349344
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=46,
                    runtime_filter_params=None,
                    backend_num=102,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349343
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=47,
                    runtime_filter_params=None,
                    backend_num=103,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349342
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=48,
                    runtime_filter_params=None,
                    backend_num=104,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349341
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=49,
                    runtime_filter_params=None,
                    backend_num=105,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349340
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=50,
                    runtime_filter_params=None,
                    backend_num=106,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349339
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=51,
                    runtime_filter_params=None,
                    backend_num=107,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349338
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=52,
                    runtime_filter_params=None,
                    backend_num=108,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349337
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=53,
                    runtime_filter_params=None,
                    backend_num=109,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349336
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=54,
                    runtime_filter_params=None,
                    backend_num=110,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349335
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=55,
                    runtime_filter_params=None,
                    backend_num=111,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
            ],
            workload_groups=[
                TPipelineWorkloadGroup(
                    id=1761898803267, name=None, properties=None, version=None
                )
            ],
            txn_conf=None,
            table_name=None,
            file_scan_params=None,
            group_commit=False,
            load_stream_per_node=None,
            total_load_streams=None,
            num_local_sink=None,
            num_buckets=None,
            bucket_seq_to_instance_idx=None,
            per_node_shared_scans=None,
            parallel_instances=1,
            total_instances=56,
            shuffle_idx_to_instance_idx={},
            is_nereids=True,
            wal_id=None,
            content_length=None,
            current_connect_fe=TNetworkAddress(hostname="192.168.30.126", port=9020),
            topn_filter_source_node_ids=None,
            ai_resources={},
            is_mow_table=None,
        ),
        TPipelineFragmentParams(
            protocol_version=0,
            query_id=query_id,
            fragment_id=0,
            per_exch_num_senders={},
            desc_tbl=None,
            resource_info=None,
            destinations=[
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349334
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349333
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349332
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349331
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349330
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349329
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349328
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349327
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349326
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349325
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349324
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349323
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349322
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349321
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349320
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349319
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349318
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349317
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349316
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349315
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349314
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349313
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349312
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349311
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349310
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349309
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349308
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349307
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349306
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349305
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349304
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349303
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349302
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349301
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349300
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349299
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349298
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349297
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349296
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349295
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349294
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349293
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349292
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349291
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349290
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349289
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349288
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349287
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349286
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349285
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349284
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349283
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349282
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349281
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349280
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
                TPlanFragmentDestination(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349279
                    ),
                    server=TNetworkAddress(hostname="192.168.30.126", port=9060),
                    brpc_server=TNetworkAddress(hostname="192.168.30.126", port=8060),
                ),
            ],
            num_senders=56,
            send_query_statistics_with_every_batch=False,
            coord=None,
            query_globals=None,
            query_options=TQueryOptions(
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
                mem_limit=100147483648,
                abort_on_default_limit_exceeded=False,
                query_timeout=900,
                is_report_success=True,
                codegen_level=0,
                kudu_latest_observed_ts=9223372036854775807,
                query_type=0,
                min_reservation=0,
                max_reservation=107374182400,
                initial_reservation_total_claims=2147483647,
                buffer_pool_limit=2147483648,
                default_spillable_buffer_size=2097152,
                min_spillable_buffer_size=65536,
                max_row_size=524288,
                disable_stream_preaggregations=False,
                mt_dop=0,
                load_mem_limit=0,
                max_scan_key_num=48,
                max_pushdown_conditions_per_column=1024,
                enable_spilling=False,
                enable_enable_exchange_node_parallel_merge=False,
                runtime_filter_wait_time_ms=1000,
                runtime_filter_max_in_num=40960,
                resource_limit=None,
                return_object_data_as_binary=False,
                trim_tailing_spaces_for_external_table_query=False,
                enable_function_pushdown=False,
                fragment_transmission_compression_codec="none",
                enable_local_exchange=True,
                skip_storage_engine_merge=False,
                skip_delete_predicate=False,
                enable_new_shuffle_hash_method=None,
                be_exec_version=8,
                partitioned_hash_join_rows_threshold=0,
                enable_share_hash_table_for_broadcast_join=True,
                check_overflow_for_decimal=True,
                skip_delete_bitmap=False,
                enable_pipeline_engine=True,
                repeat_max_num=0,
                external_sort_bytes_threshold=0,
                partitioned_hash_agg_rows_threshold=0,
                enable_file_cache=False,
                insert_timeout=14400,
                execution_timeout=900,
                dry_run_query=False,
                enable_common_expr_pushdown=True,
                parallel_instance=56,
                mysql_row_binary_format=False,
                external_agg_bytes_threshold=0,
                external_agg_partition_bits=4,
                file_cache_base_path="random",
                enable_parquet_lazy_mat=True,
                enable_orc_lazy_mat=True,
                scan_queue_mem_limit=107374182,
                enable_scan_node_run_serial=False,
                enable_insert_strict=True,
                enable_inverted_index_query=True,
                truncate_char_or_varchar_columns=False,
                enable_hash_join_early_start_probe=False,
                enable_pipeline_x_engine=True,
                enable_memtable_on_sink_node=True,
                enable_delete_sub_predicate_v2=False,
                fe_process_uuid=1762444564496,
                inverted_index_conjunction_opt_threshold=1000,
                enable_profile=True,
                enable_page_cache=True,
                analyze_timeout=43200,
                faster_float_convert=False,
                enable_decimal256=False,
                enable_local_shuffle=True,
                skip_missing_version=False,
                runtime_filter_wait_infinitely=False,
                condition_cache_digest=0,
                inverted_index_max_expansions=50,
                inverted_index_skip_threshold=50,
                enable_parallel_scan=True,
                parallel_scan_max_scanners_count=0,
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
                enable_common_expr_pushdown_for_inverted_index=True,
                local_exchange_free_blocks_limit=4,
                enable_force_spill=False,
                enable_parquet_filter_by_min_max=True,
                enable_orc_filter_by_min_max=True,
                max_column_reader_num=20000,
                enable_local_merge_sort=False,
                enable_parallel_result_sink=True,
                enable_short_circuit_query_access_column_store=True,
                enable_no_need_read_data_opt=True,
                read_csv_empty_line_as_null=False,
                serde_dialect=0,
                enable_match_without_inverted_index=True,
                enable_fallback_on_missing_inverted_index=True,
                keep_carriage_return=False,
                runtime_bloom_filter_min_size=1048576,
                hive_parquet_use_column_names=True,
                hive_orc_use_column_names=True,
                enable_segment_cache=True,
                runtime_bloom_filter_max_size=67108864,
                in_list_value_count_threshold=10,
                enable_verbose_profile=False,
                rpc_verbose_profile_max_instance_count=5,
                enable_adaptive_pipeline_task_serial_read_on_limit=True,
                adaptive_pipeline_task_serial_read_on_limit=10000,
                parallel_prepare_threshold=32,
                partition_topn_max_partitions=1024,
                partition_topn_pre_partition_rows=1000,
                enable_parallel_outfile=False,
                enable_phrase_query_sequential_opt=True,
                enable_auto_create_when_overwrite=False,
                orc_tiny_stripe_threshold_bytes=8388608,
                orc_once_max_read_bytes=8388608,
                orc_max_merge_distance_bytes=1048576,
                ignore_runtime_filter_error=False,
                enable_fixed_len_to_uint32_v2=False,
                enable_shared_exchange_sink_buffer=True,
                enable_inverted_index_searcher_cache=True,
                enable_inverted_index_query_cache=True,
                enable_condition_cache=False,
                profile_level=1,
                min_scanner_concurrency=1,
                min_scan_scheduler_concurrency=0,
                enable_runtime_filter_partition_prune=True,
                minimum_operator_memory_required_kb=1000,
                enable_mem_overcommit=True,
                query_slot_count=1,
                enable_spill=False,
                enable_reserve_memory=True,
                revocable_memory_high_watermark_percent=-1,
                spill_sort_mem_limit=134217728,
                spill_sort_batch_bytes=8388608,
                spill_aggregation_partition_count=32,
                spill_hash_join_partition_count=32,
                low_memory_mode_buffer_limit=33554432,
                dump_heap_profile_when_mem_limit_exceeded=False,
                inverted_index_compatible_read=False,
                check_orc_init_sargs_success=False,
                exchange_multi_blocks_byte_size=262144,
                enable_strict_cast=False,
                new_version_unix_timestamp=True,
                hnsw_ef_search=32,
                hnsw_check_relative_distance=True,
                hnsw_bounded_queue=True,
                optimize_index_scan_parallelism=True,
                enable_prefer_cached_rowset=False,
                query_freshness_tolerance_ms=-1,
                merge_read_slice_size=8388608,
                enable_fuzzy_blockable_task=False,
                shuffled_agg_ids=[],
                disable_file_cache=False,
            ),
            import_label=None,
            db_name=None,
            load_job_id=None,
            load_error_hub_info=None,
            fragment_num_on_host=168,
            backend_id=1761898803229,
            need_wait_execution_trigger=True,
            instances_sharing_hash_table=None,
            is_simplified_param=True,
            global_dict=None,
            fragment=TPlanFragment(
                plan=TPlan(
                    nodes=[
                        TPlanNode(
                            node_id=0,
                            node_type=29,
                            num_children=0,
                            limit=-1,
                            row_tuples=[0],
                            nullable_tuples=[False],
                            conjuncts=None,
                            compact_data=False,
                            hash_join_node=None,
                            agg_node=None,
                            sort_node=None,
                            merge_node=None,
                            exchange_node=None,
                            mysql_scan_node=None,
                            olap_scan_node=None,
                            csv_scan_node=None,
                            broker_scan_node=None,
                            pre_agg_node=None,
                            schema_scan_node=None,
                            merge_join_node=None,
                            meta_scan_node=None,
                            analytic_node=None,
                            olap_rewrite_node=None,
                            union_node=None,
                            resource_profile=None,
                            es_scan_node=None,
                            repeat_node=None,
                            assert_num_rows_node=None,
                            intersect_node=None,
                            except_node=None,
                            odbc_scan_node=None,
                            runtime_filters=None,
                            group_commit_scan_node=None,
                            materialization_node=None,
                            vconjunct=None,
                            table_function_node=None,
                            output_slot_ids=None,
                            data_gen_scan_node=None,
                            file_scan_node=TFileScanNode(
                                tuple_id=0, table_name="LocalTableValuedFunction"
                            ),
                            jdbc_scan_node=None,
                            nested_loop_join_node=None,
                            test_external_scan_node=None,
                            push_down_agg_type_opt=0,
                            push_down_count=None,
                            distribute_expr_lists=None,
                            is_serial_operator=True,
                            projections=None,
                            output_tuple_id=None,
                            partition_sort_node=None,
                            intermediate_projections_list=None,
                            intermediate_output_tuple_id_list=None,
                            topn_filter_source_node_ids=None,
                            nereids_id=171,
                        )
                    ]
                ),
                output_exprs=None,
                output_sink=TDataSink(
                    type=0,
                    stream_sink=TDataStreamSink(
                        dest_node_id=1,
                        output_partition=TDataPartition(
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
                                                            type=5,
                                                            len=None,
                                                            precision=None,
                                                            scale=None,
                                                            variant_max_subcolumns_count=0,
                                                        ),
                                                        struct_fields=None,
                                                        contains_null=None,
                                                        contains_nulls=None,
                                                    )
                                                ],
                                                is_nullable=None,
                                                byte_size=-1,
                                                sub_types=None,
                                                result_is_nullable=None,
                                                function_name=None,
                                                be_exec_version=None,
                                            ),
                                            opcode=None,
                                            num_children=0,
                                            agg_expr=None,
                                            bool_literal=None,
                                            case_expr=None,
                                            date_literal=None,
                                            float_literal=None,
                                            int_literal=None,
                                            in_predicate=None,
                                            is_null_pred=None,
                                            like_pred=None,
                                            literal_pred=None,
                                            slot_ref=TSlotRef(
                                                slot_id=0,
                                                tuple_id=0,
                                                col_unique_id=-1,
                                                is_virtual_slot=False,
                                            ),
                                            string_literal=None,
                                            tuple_is_null_pred=None,
                                            info_func=None,
                                            decimal_literal=None,
                                            output_scale=-1,
                                            fn_call_expr=None,
                                            large_int_literal=None,
                                            output_column=None,
                                            output_type=None,
                                            vector_opcode=None,
                                            fn=None,
                                            vararg_start_idx=None,
                                            child_type=None,
                                            is_nullable=True,
                                            json_literal=None,
                                            schema_change_expr=None,
                                            column_ref=None,
                                            match_predicate=None,
                                            ipv4_literal=None,
                                            ipv6_literal=None,
                                            label="_table_valued_function_file.id",
                                            timev2_literal=None,
                                            varbinary_literal=None,
                                            is_cast_nullable=None,
                                            search_param=None,
                                        )
                                    ]
                                )
                            ],
                            partition_infos=None,
                        ),
                        ignore_not_found=None,
                        output_exprs=None,
                        output_tuple_id=None,
                        conjuncts=None,
                        runtime_filters=None,
                        tablet_sink_schema=None,
                        tablet_sink_partition=None,
                        tablet_sink_location=None,
                        tablet_sink_txn_id=-1,
                        tablet_sink_tuple_id=None,
                        tablet_sink_exprs=None,
                        is_merge=False,
                    ),
                    result_sink=None,
                    mysql_table_sink=None,
                    export_sink=None,
                    olap_table_sink=None,
                    memory_scratch_sink=None,
                    odbc_table_sink=None,
                    result_file_sink=None,
                    jdbc_table_sink=None,
                    multi_cast_stream_sink=None,
                    hive_table_sink=None,
                    iceberg_table_sink=None,
                    dictionary_sink=None,
                    blackhole_sink=None,
                ),
                partition=TDataPartition(
                    type=1, partition_exprs=[], partition_infos=None
                ),
                min_reservation_bytes=0,
                initial_reservation_total_claims=0,
                query_cache_param=None,
            ),
            local_params=[
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349446
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={
                        0: [
                            TScanRangeParams(
                                scan_range=TScanRange(
                                    palo_scan_range=None,
                                    kudu_scan_token=None,
                                    broker_scan_range=None,
                                    es_scan_range=None,
                                    ext_scan_range=TExternalScanRange(
                                        file_scan_range=TFileScanRange(
                                            ranges=[
                                                TFileRangeDesc(
                                                    load_id=None,
                                                    path="/data11/chen/doris-latest/test2.csv",
                                                    start_offset=0,
                                                    size=10,
                                                    file_size=10,
                                                    columns_from_path=[],
                                                    columns_from_path_keys=[],
                                                    table_format_params=TTableFormatFileDesc(
                                                        table_format_type="tvf",
                                                        iceberg_params=None,
                                                        hudi_params=None,
                                                        paimon_params=None,
                                                        transactional_hive_params=None,
                                                        max_compute_params=None,
                                                        trino_connector_params=None,
                                                        lakesoul_params=None,
                                                        table_level_row_count=-1,
                                                    ),
                                                    modification_time=0,
                                                    file_type=None,
                                                    compress_type=1,
                                                    fs_name=None,
                                                    format_type=0,
                                                    self_split_weight=None,
                                                    columns_from_path_is_null=None,
                                                )
                                            ],
                                            params=None,
                                            split_source=None,
                                        )
                                    ),
                                    data_gen_scan_range=None,
                                    meta_scan_range=None,
                                ),
                                volume_id=-1,
                            )
                        ]
                    },
                    sender_id=0,
                    runtime_filter_params=None,
                    backend_num=0,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349445
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=1,
                    runtime_filter_params=None,
                    backend_num=1,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349444
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=2,
                    runtime_filter_params=None,
                    backend_num=2,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349443
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=3,
                    runtime_filter_params=None,
                    backend_num=3,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349442
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=4,
                    runtime_filter_params=None,
                    backend_num=4,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349441
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=5,
                    runtime_filter_params=None,
                    backend_num=5,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349440
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=6,
                    runtime_filter_params=None,
                    backend_num=6,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349439
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=7,
                    runtime_filter_params=None,
                    backend_num=7,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349438
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=8,
                    runtime_filter_params=None,
                    backend_num=8,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349437
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=9,
                    runtime_filter_params=None,
                    backend_num=9,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349436
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=10,
                    runtime_filter_params=None,
                    backend_num=10,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349435
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=11,
                    runtime_filter_params=None,
                    backend_num=11,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349434
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=12,
                    runtime_filter_params=None,
                    backend_num=12,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349433
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=13,
                    runtime_filter_params=None,
                    backend_num=13,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349432
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=14,
                    runtime_filter_params=None,
                    backend_num=14,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349431
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=15,
                    runtime_filter_params=None,
                    backend_num=15,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349430
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=16,
                    runtime_filter_params=None,
                    backend_num=16,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349429
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=17,
                    runtime_filter_params=None,
                    backend_num=17,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349428
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=18,
                    runtime_filter_params=None,
                    backend_num=18,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349427
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=19,
                    runtime_filter_params=None,
                    backend_num=19,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349426
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=20,
                    runtime_filter_params=None,
                    backend_num=20,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349425
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=21,
                    runtime_filter_params=None,
                    backend_num=21,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349424
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=22,
                    runtime_filter_params=None,
                    backend_num=22,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349423
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=23,
                    runtime_filter_params=None,
                    backend_num=23,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349422
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=24,
                    runtime_filter_params=None,
                    backend_num=24,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349421
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=25,
                    runtime_filter_params=None,
                    backend_num=25,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349420
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=26,
                    runtime_filter_params=None,
                    backend_num=26,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349419
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=27,
                    runtime_filter_params=None,
                    backend_num=27,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349418
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=28,
                    runtime_filter_params=None,
                    backend_num=28,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349417
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=29,
                    runtime_filter_params=None,
                    backend_num=29,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349416
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=30,
                    runtime_filter_params=None,
                    backend_num=30,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349415
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=31,
                    runtime_filter_params=None,
                    backend_num=31,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349414
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=32,
                    runtime_filter_params=None,
                    backend_num=32,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349413
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=33,
                    runtime_filter_params=None,
                    backend_num=33,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349412
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=34,
                    runtime_filter_params=None,
                    backend_num=34,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349411
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=35,
                    runtime_filter_params=None,
                    backend_num=35,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349410
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=36,
                    runtime_filter_params=None,
                    backend_num=36,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349409
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=37,
                    runtime_filter_params=None,
                    backend_num=37,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349408
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=38,
                    runtime_filter_params=None,
                    backend_num=38,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349407
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=39,
                    runtime_filter_params=None,
                    backend_num=39,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349406
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=40,
                    runtime_filter_params=None,
                    backend_num=40,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349405
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=41,
                    runtime_filter_params=None,
                    backend_num=41,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349404
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=42,
                    runtime_filter_params=None,
                    backend_num=42,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349403
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=43,
                    runtime_filter_params=None,
                    backend_num=43,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349402
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=44,
                    runtime_filter_params=None,
                    backend_num=44,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349401
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=45,
                    runtime_filter_params=None,
                    backend_num=45,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349400
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=46,
                    runtime_filter_params=None,
                    backend_num=46,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349399
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=47,
                    runtime_filter_params=None,
                    backend_num=47,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349398
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=48,
                    runtime_filter_params=None,
                    backend_num=48,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349397
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=49,
                    runtime_filter_params=None,
                    backend_num=49,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349396
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=50,
                    runtime_filter_params=None,
                    backend_num=50,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349395
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=51,
                    runtime_filter_params=None,
                    backend_num=51,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349394
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=52,
                    runtime_filter_params=None,
                    backend_num=52,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349393
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=53,
                    runtime_filter_params=None,
                    backend_num=53,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349392
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=54,
                    runtime_filter_params=None,
                    backend_num=54,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
                TPipelineInstanceParams(
                    fragment_instance_id=TUniqueId(
                        hi=-1762484765925226891, lo=-8308220895157349391
                    ),
                    build_hash_table_for_broadcast_join=False,
                    per_node_scan_ranges={},
                    sender_id=55,
                    runtime_filter_params=None,
                    backend_num=55,
                    per_node_shared_scans=None,
                    topn_filter_source_node_ids=None,
                    topn_filter_descs=None,
                ),
            ],
            workload_groups=[
                TPipelineWorkloadGroup(
                    id=1761898803267, name=None, properties=None, version=None
                )
            ],
            txn_conf=None,
            table_name=None,
            file_scan_params=None,
            group_commit=False,
            load_stream_per_node=None,
            total_load_streams=None,
            num_local_sink=None,
            num_buckets=None,
            bucket_seq_to_instance_idx=None,
            per_node_shared_scans=None,
            parallel_instances=1,
            total_instances=56,
            shuffle_idx_to_instance_idx={},
            is_nereids=True,
            wal_id=None,
            content_length=None,
            current_connect_fe=TNetworkAddress(hostname="192.168.30.126", port=9020),
            topn_filter_source_node_ids=None,
            ai_resources={},
            is_mow_table=None,
        ),
    ],
    desc_tbl=None,
    file_scan_params=None,
    coord=None,
    query_globals=None,
    resource_info=None,
    fragment_num_on_host=None,
    query_options=None,
    is_nereids=True,
    workload_groups=None,
    query_id=None,
    topn_filter_source_node_ids=None,
    runtime_filter_merge_addr=None,
    runtime_filter_info=TRuntimeFilterInfo(
        runtime_filter_params=TRuntimeFilterParams(
            runtime_filter_merge_addr=TNetworkAddress(
                hostname="192.168.30.126", port=8060
            ),
            rid_to_target_param=None,
            rid_to_runtime_filter=None,
            runtime_filter_builder_num=None,
            rid_to_target_paramv2=None,
        ),
        topn_filter_descs=None,
    ),
)

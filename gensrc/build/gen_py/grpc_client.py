import sys
import os
sys.path.append(os.path.dirname(__file__))

import grpc
import internal_service_pb2
import internal_service_pb2_grpc
import types_pb2

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from Data import ttypes as Data_ttypes

# import v3
import formated_params


def run():
    # Doris BE 的brpc端口是8060
    with grpc.insecure_channel("localhost:8060") as channel:
        stub = internal_service_pb2_grpc.PBackendServiceStub(channel)

        # # with open("pipeline-params-modified.bin", "rb") as f:
        # with open("pipeline-params.bin", "rb") as f:
        #
        #     # Construct the request
        #     prepare_request = internal_service_pb2.PExecPlanFragmentRequest(
        #         request=f.read(),  # 对于VERSION_3, 需要传入的是TPipelineFragmentParamsList对象的序列化字节串
        #         version=internal_service_pb2.PFragmentRequestVersion.VERSION_3,
        #         compact=True,
        #     )
        #
        # # 构造query_id
        # # query_id = types_pb2.PUniqueId(hi=12345, lo=67890)
        # query_id = types_pb2.PUniqueId(hi=1199038286675263702, lo=-7586643826940453435)
        # fragment_instance_id1 = types_pb2.PUniqueId(
        #     hi=1199038286675263702, lo=-7586643826940453433
        # )
        # fragment_instance_id2 = types_pb2.PUniqueId(
        #     hi=1199038286675263702, lo=-7586643826940453434
        # )

        transport = TTransport.TMemoryBuffer()
        protocol = TCompactProtocol.TCompactProtocol(transport)
        # v3.pipeline_framgnet_params_list.write(protocol)
        formated_params.pipeline_framgnet_params_list.write(protocol)
        serialized_data = transport.getvalue()

        prepare_request = internal_service_pb2.PExecPlanFragmentRequest(
            request=serialized_data,
            version=internal_service_pb2.PFragmentRequestVersion.VERSION_3,
            compact=True,
        )

        # query_id = types_pb2.PUniqueId(hi=v3.query_id.hi, lo=v3.query_id.lo)
        query_id = types_pb2.PUniqueId(hi=formated_params.query_id.hi, lo=formated_params.query_id.lo)
        # fragment_instance_id0 = v3.fragment_instance_id0
        # fragment_instance_id = types_pb2.PUniqueId(
        #     hi=fragment_instance_id0.hi, lo=fragment_instance_id0.lo
        # )
        # fragment_instance_id = types_pb2.PUniqueId(
        #     hi=formated_params.fragment_instance_id.hi, lo=formated_params.fragment_instance_id.lo
        # )
        fragment_instance_id = types_pb2.PUniqueId(
            hi=0, lo=0
        )

        prepare_response = None
        try:
            # Call the prepare method
            prepare_response = stub.exec_plan_fragment_prepare(prepare_request)
            print("Successfully prepared plan fragment.")
            print("Prepare Response:", prepare_response)

            # Assuming the prepare_response contains the fragment_instance_id
            # and that PExecPlanFragmentStartRequest requires it.
            # You might need to adjust this based on the actual definitions.
            # if prepare_response and hasattr(prepare_response, 'query_id'):

            start_request = internal_service_pb2.PExecPlanFragmentStartRequest(
                query_id=query_id
            )

            # Call the start method
            start_response = stub.exec_plan_fragment_start(start_request)
            print("Successfully started plan fragment.")
            print("Start Response:", start_response)

            # 似乎提交是异步的, 不等待不一定有结果
            import time; time.sleep(0.5)
            # import time; time.sleep(3)

            # for fragment_instance_id in [fragment_instance_id1, fragment_instance_id2]:
            # for fragment_instance_id in [fragment_instance_id2, fragment_instance_id1]:
            # for fragment_instance_id in [fragment_instance_id1]:

            # Fetch the data
            eos = False
            fetch_request = internal_service_pb2.PFetchDataRequest(
                # finst_id=fragment_instance_id,
                finst_id=query_id,
                resp_in_attachment=False,
            )
            # import pdb; pdb.set_trace()
            while not eos:
                fetch_response = stub.fetch_data(fetch_request)
                print(">>> ", fetch_response)

                # Process the data
                # I am assuming the response has 'eos' and 'row_batch' fields.
                # You might need to adjust this based on the actual definitions.
                if hasattr(fetch_response, "row_batch") and fetch_response.row_batch:
                    # print("Received data batch:")
                    # print(fetch_response.row_batch)
                    # row_batch 是 thrift.TResultBatch 序列化后的字节串

                    # Deserialize the TRowBatch

                    # Doris FE中使用的是一个自定义类型的协议, 但是其实只是BinaryProtocol改了一下maxMessageSize参数而已.
                    # fe-core/src/main/java/org/apache/doris/rpc/TCustomProtocolFactory.java
                    # print("Trying with TBinaryProtocol...")
                    try:
                        transport = TTransport.TMemoryBuffer(fetch_response.row_batch)
                        protocol = TBinaryProtocol.TBinaryProtocol(transport)
                        # protocol = TCompactProtocol.TCompactProtocol(transport)
                        # t_row_batch = Data_ttypes.TRowBatch()
                        t_row_batch = (
                            Data_ttypes.TResultBatch()
                        )  # 命名有点坑, 应该是fetch_response.result_batch
                        t_row_batch.read(protocol)
                        print("Deserialized TRowBatch with TBinaryProtocol:")
                        print(t_row_batch)
                    except Exception as e:
                        print(
                            f"Error deserializing TRowBatch with TBinaryProtocol: {e}"
                        )

                if (
                    hasattr(fetch_response, "status")
                    and fetch_response.status.status_code != 0
                ):
                    print(fetch_response.status, "END")
                    break

                if hasattr(fetch_response, "eos"):
                    eos = fetch_response.eos
                else:
                    # If 'eos' is not present, assume end of stream
                    eos = True

                if eos:
                    print("end-of-stream")
        except grpc.RpcError as e:
            print(f"Error: {e.code()} - {e.details()}")
        finally:
            pass
            # # Clean up the fragment
            # try:
            #     cancel_request = internal_service_pb2.PCancelPlanFragmentRequest(
            #         # 似乎传fragment_instance_id和query_id都不对
            #         # java代码中说finst_id没有用了, 但是是必须字段
            #         finst_id=fragment_instance_id,
            #         # finst_id=query_id,
            #         query_id=query_id,
            #     )
            #     cancel_response = stub.cancel_plan_fragment(cancel_request)
            #     print("Successfully cancelled plan fragment.")
            #     print("Cancel Response:", cancel_response)
            # except grpc.RpcError as e:
            #     print(f"Error cancelling plan fragment: {e.code()} - {e.details()}")


if __name__ == "__main__":
    run()

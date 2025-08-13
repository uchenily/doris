import grpc
import internal_service_pb2
import internal_service_pb2_grpc
import types_pb2

from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.protocol import TBinaryProtocol
from Data import ttypes as Data_ttypes

def run():
    # Doris BE 的brpc端口是8060
    with grpc.insecure_channel('localhost:8060') as channel:
        stub = internal_service_pb2_grpc.PBackendServiceStub(channel)

        # with open("pipeline-params-modified.bin", "rb") as f:
        with open("pipeline-params.bin", "rb") as f:

            # Construct the request
            prepare_request = internal_service_pb2.PExecPlanFragmentRequest(
                request=f.read(), # 对于VERSION_3, 需要传入的是TPipelineFragmentParamsList对象的序列化字节串
                version=internal_service_pb2.PFragmentRequestVersion.VERSION_3,
                compact=True,
            )

        # 构造query_id
        # query_id = types_pb2.PUniqueId(hi=12345, lo=67890)
        query_id = types_pb2.PUniqueId(hi=1199038286675263702, lo=-7586643826940453435)
        fragment_instance_id1 = types_pb2.PUniqueId(hi=1199038286675263702, lo=-7586643826940453433)
        fragment_instance_id2 = types_pb2.PUniqueId(hi=1199038286675263702, lo=-7586643826940453434)

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

            import time; time.sleep(1)

            # for fragment_instance_id in [fragment_instance_id1, fragment_instance_id2]:
            for fragment_instance_id in [fragment_instance_id1]:
                # Fetch the data
                eos = False
                fetch_request = internal_service_pb2.PFetchDataRequest(
                    finst_id=fragment_instance_id
                )
                # import pdb; pdb.set_trace()
                while not eos:
                    fetch_response = stub.fetch_data(fetch_request)
                    print(">>>", fetch_response)
                    
                    # Process the data
                    # I am assuming the response has 'eos' and 'row_batch' fields.
                    # You might need to adjust this based on the actual definitions.
                    if hasattr(fetch_response, 'row_batch') and fetch_response.row_batch:
                        print("Received data batch:")
                        # Here you would process the data in fetch_response.row_batch
                        # For now, just printing it.
                        # print(fetch_response.row_batch)
                        # row_batch 是 thrift.TRowBatch 序列化后的字节串
                        
                        # Deserialize the TRowBatch
                        try:
                            print(f"Received data batch with size: {len(fetch_response.row_batch)}")
                            transport = TTransport.TMemoryBuffer(fetch_response.row_batch)
                            protocol = TCompactProtocol.TCompactProtocol(transport)
                            t_row_batch = Data_ttypes.TRowBatch()
                            t_row_batch.read(protocol)
                            print("Deserialized TRowBatch with TCompactProtocol:")
                            print(t_row_batch)
                            if t_row_batch.num_rows == 0:
                                print("TRowBatch contains 0 rows.")
                            else:
                                print(f"TRowBatch contains {t_row_batch.num_rows} rows.")
                        except Exception as e:
                            print(f"Error deserializing TRowBatch with TCompactProtocol: {e}")
                            print("Trying with TBinaryProtocol...")
                            try:
                                transport = TTransport.TMemoryBuffer(fetch_response.row_batch)
                                protocol = TBinaryProtocol.TBinaryProtocol(transport)
                                t_row_batch = Data_ttypes.TRowBatch()
                                t_row_batch.read(protocol)
                                print("Deserialized TRowBatch with TBinaryProtocol:")
                                print(t_row_batch)
                                if t_row_batch.num_rows == 0:
                                    print("TRowBatch contains 0 rows.")
                                else:
                                    print(f"TRowBatch contains {t_row_batch.num_rows} rows.")
                            except Exception as e2:
                                print(f"Error deserializing TRowBatch with TBinaryProtocol: {e2}")

                    if hasattr(fetch_response, 'status') and fetch_response.status != 0:
                        print(fetch_response.status)
                        # break

                    if hasattr(fetch_response, 'eos'):
                        eos = fetch_response.eos
                    else:
                        # If 'eos' is not present, assume end of stream
                        eos = True
                # else:
                #     print("Could not find fragment_instance_id in prepare response.")

        except grpc.RpcError as e:
            print(f"Error: {e.code()} - {e.details()}")
        finally:
            # Clean up the fragment
            if prepare_response and hasattr(prepare_response, 'fragment_instance_id'):
                try:
                    cancel_request = internal_service_pb2.PCancelPlanFragmentRequest(
                        finst_id=prepare_response.fragment_instance_id
                    )
                    cancel_response = stub.cancel_plan_fragment(cancel_request)
                    print("Successfully cancelled plan fragment.")
                    print("Cancel Response:", cancel_response)
                except grpc.RpcError as e:
                    print(f"Error cancelling plan fragment: {e.code()} - {e.details()}")

if __name__ == '__main__':
    run()

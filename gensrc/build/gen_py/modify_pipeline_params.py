#!/usr/bin/env python3

from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from PaloInternalService import ttypes as PaloInternalService_ttypes
from Types import ttypes as Types_ttypes

def modify_query_id(input_file, new_query_id_hi, new_query_id_lo, output_file):
    """
    Deserializes a TPipelineFragmentParamsList from a file, modifies the query_id,
    and serializes it back to a new file.
    """
    # Read the serialized data from the input file
    with open(input_file, 'rb') as f:
        serialized_data = f.read()

    # Deserialize the data
    transport = TTransport.TMemoryBuffer(serialized_data)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    params_list = PaloInternalService_ttypes.TPipelineFragmentParamsList()
    params_list.read(protocol)

    # print(f"Original TPipelineFragmentParamsList: {params_list}")

    # Modify the query_id
    new_query_id = Types_ttypes.TUniqueId(hi=new_query_id_hi, lo=new_query_id_lo)
    print("###: ", new_query_id)
    if params_list.params_list:
        for params in params_list.params_list:
            # print(f"  Original query_id: {params.query_id}")
            # params.query_id = new_query_id
            # print(f"  New query_id: {params.query_id}")
            if params.destinations:
                print("destinations -> fragment_instance_id: ", params.destinations[0].fragment_instance_id)
            if params.local_params:
                print("fragment_instance_id: ", params.local_params[0].fragment_instance_id)

    # # Serialize the modified object
    # transport = TTransport.TMemoryBuffer()
    # protocol = TCompactProtocol.TCompactProtocol(transport)
    # params_list.write(protocol)
    # serialized_data = transport.getvalue()
    #
    # # Write the modified data to the output file
    # with open(output_file, 'wb') as f:
    #     f.write(serialized_data)
    # 
    # print(f"Successfully modified and saved to {output_file}")

if __name__ == '__main__':
    # Example usage:
    # Replace with your actual file paths and desired query_id
    modify_query_id(
        input_file='pipeline-params.bin',
        new_query_id_hi=12345,
        new_query_id_lo=67890,
        output_file='pipeline-params-modified.bin'
    )

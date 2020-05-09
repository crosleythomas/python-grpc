
import logging
import sys

import grpc

import sample_pb2 as pb2
import sample_pb2_grpc as pb2_grpc


def run():
    print("Creating Channel")
    with grpc.insecure_channel('localhost:50051') as channel: # Step 1: Create a connection to the server
        print("Created channel %s" % str(channel))
        stub = pb2_grpc.SampleStub(channel)                   # Step 2: Create a stub so we can call its RPCs
        print("-------------- Calling SampleMethod --------------")
        input_msg = pb2.SampleInput(input=sys.argv[1])
        print(stub.SampleMethod(input_msg))                   # Step 3: Call the RPC


if __name__ == '__main__':
    logging.basicConfig()
    run()

import logging
import sys
import os
import argparse

import grpc

import sample_pb2 as pb2
import sample_pb2_grpc as pb2_grpc


def run(port, inputStr):
    print("Creating Channel")
    channel_address = 'localhost:%s' % port
    print("Connecting to %s" % channel_address)
    with grpc.insecure_channel(channel_address) as channel: # Step 1: Create a connection to the server
        print("Created channel %s" % str(channel))
        stub = pb2_grpc.SampleStub(channel)                   # Step 2: Create a stub so we can call its RPCs
        print("-------------- Calling SampleMethod --------------")
        print("Calling with %s" % inputStr)
        input_msg = pb2.SampleInput(input=inputStr)
        print(stub.SampleMethod(input_msg))                   # Step 3: Call the RPC


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default='50051')
    parser.add_argument('-i', '--input', default='hello')
    args = parser.parse_args()
    logging.basicConfig()
    run(args.port, args.input)

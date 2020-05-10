from concurrent import futures

import logging
import os

import grpc

# Import the two gRPC generated files for this service
import sample_pb2 as pb2
import sample_pb2_grpc as pb2_grpc


# Create a class that extends the generated Servicer object
class SampleServicer(pb2_grpc.Sample):
    # Implement the methods defined in the proto file
    def __init__(self):
        pass

    def SampleMethod(self, request, context):
        return pb2.SampleOutput(output=str("Echoing back %s" % request.input))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    pb2_grpc.add_SampleServicer_to_server(
        SampleServicer(), server)
    bind_address = "[::]:%s" % (os.environ["PORT"] if ("PORT" in os.environ) else '50051')
    print("Adding connection for %s" % bind_address)
    server.add_insecure_port(bind_address)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    print("Starting Server...")
    serve()
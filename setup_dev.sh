#!/usr/bin/env bash

# Set up any needed dependencies
pip install grpcio-tools
docker pull grpc/python

# Set up this repo
echo $1

touch $1.proto


python -m grpc_tools.protoc -I protos/ --python_out=protos --grpc_python_out=protos --proto_path protos sample.proto

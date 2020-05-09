# python-grpc
Template for deploying Python gRPC services

Goal: develop a template repository that can be cloned, updated with a single function, and immediately deployed so the function can be called.

Steps:
* Use [grpc/python](https://hub.docker.com/r/grpc/python) Docker image for portability
* Figure out how to templatize a python function being loaded into the Docker image as a gRPC service
* Set up the Github Actions that will deploy these gRPC services
* Document the one-off setup steps that will need to be performed each time this repo is cloned
    * Call setup script with ___, ___, ..., ___
    * Define input/output protobuf messages
    * Define function
    * Define any additional dependencies in `requirements.txt` or `Dockerfile`
* Put as many of these setup steps into a script 


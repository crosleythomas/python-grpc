# python-grpc
Template for deploying Python gRPC services

## Goal
Develop a template repository that can be cloned, updated with a single function, and seamlessly deployed to a cloud provider.

There will be some one-time setup to set up of an account with a cloud hosting provider, but after that is set up, deploying new gRPC functions should be as frictionless as possible.

To Do:
* Make workflow read from Github project name (and other meta-data?) to populate different things
* Make the server and clients re-usable - importing the generated clients
* See if we can automate some of the one-time setup via git hooks

## One-Time Setup
1. Google Cloud Platform
    1. [Create an account](http://console.cloud.google.com/)
    2. [Create a `Project`](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
    3. Set up a billing account
    4. Create an IAM role with the permissions Service Account User, Cloud Run Admin, Storage Admin
2. Local Setup
    1. [Install gRPC tools](https://grpc.io/docs/quickstart/python/) 

## New-Service Setup
1. Fork this repo
2. Set a Secret value named `GCLOUD_AUTH` with a value from step 1.
    
## Implementation
1. Add input/output/function protobuf definitions [here](sample.proto)
2. Run the gRPC code generator, python -m grpc_tools.protoc -I protos/ --python_out=protos --grpc_python_out=protos --proto_path protos/ sample.proto
 --proto_path=.`
3. Implement your function logic [here](sample_server.py)
4. Add in additional dependencies in the [Dockerfile](Dockerfile) or [requirements.txt](requirements.txt) 
5. Test your changes locally
    1. `python sample_server.py`
    2. `python sample_client.py`
4. Push your changes and check the build [here]()

Steps:
* Use [grpc/python](https://hub.docker.com/r/grpc/python) Docker image for portability
* Figure out how to templatize a python function being loaded into the Docker image as a gRPC service
* Set up the Github Actions that will deploy these gRPC services
* Document the one-off setup steps that will need to be performed each time this repo is cloned
    * GCP Account setup
        * Enable Billing
        * Create a Project
        * Docker Registry [Enable the Container Registry API](https://cloud.google.com/container-registry/docs/pushing-and-pulling?_ga=2.194564205.-1139661921.1583806155)
        * Configure Docker to use gcloud `gcloud auth configure-docker`
        * Cloud Run
    * Call setup script with ___, ___, ..., ___
    * Define input/output protobuf messages
    * Define function
    * Define any additional dependencies in `requirements.txt` or `Dockerfile`
* Put as many of these setup steps into a script 

https://github.com/marketplace/actions/cloud-run
https://cloud.google.com/blog/products/compute/serve-cloud-run-requests-with-grpc-not-just-http
https://github.com/fullstorydev/grpcurl

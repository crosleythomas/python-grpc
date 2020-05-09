"""
This repo can be setup by calling this script with the following arguments


python3 setup_dev.py $service $method $method_type $input_msg $output_msg

$method_type : [simple, response-streaming, request-streaming, bidirectional-streaming]

"""

# Create the .proto file for service and message definitions
# Generate quicklink to .proto cheat sheet so it's quick to write new definitions

# Fill the .proto file with template definitions based on service name

# Generate sample_server.py based on the given arguments
# (this is where the real logic is implemented)
# Question - if we want to keep the core logic for a method we've implemented
#   but update part of the definition, how do we regenerate the server file
#   without over-writing all of the contents?



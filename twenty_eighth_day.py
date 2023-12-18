#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

import boto3

# AWS credentials and region
AWS_ACCESS_KEY = 'YOUR_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_SECRET_KEY'
REGION_NAME = 'us-west-2'  # Change to your desired region

# Connect to EC2
ec2 = boto3.client(
    'ec2',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME
)

# Function to start EC2 instance
def start_ec2_instance(instance_id):
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Starting EC2 instance {instance_id}")
    except Exception as e:
        print(f"Error starting instance {instance_id}: {str(e)}")

# Function to stop EC2 instance
def stop_ec2_instance(instance_id):
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping EC2 instance {instance_id}")
    except Exception as e:
        print(f"Error stopping instance {instance_id}: {str(e)}")

# Usage examples
if __name__ == "__main__":
    # Replace INSTANCE_ID with your EC2 instance ID
    instance_id = 'INSTANCE_ID'

    # Start or stop the EC2 instance
    start_ec2_instance(instance_id)
    # stop_ec2_instance(instance_id)

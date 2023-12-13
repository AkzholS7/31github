#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

from azure.identity import DefaultAzureCredential
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from azure.mgmt.containerregistry.models import SourceControlType, SourceProperties

# Azure subscription ID, resource group name, ACR name, and Dockerfile path
subscription_id = 'your_subscription_id'
resource_group_name = 'your_resource_group'
acr_name = 'your_acr_name'
dockerfile_path = 'path/to/your/Dockerfile'

# Authenticate using Azure credentials
credential = DefaultAzureCredential()

# Create ACR management client
acr_client = ContainerRegistryManagementClient(credential, subscription_id)

# Get ACR details
acr = acr_client.registries.get(resource_group_name, acr_name)

# Build the source properties for Dockerfile
source_properties = SourceProperties(
    source_control_type=SourceControlType.DOCKERFILE,
    docker_file_path=dockerfile_path,
)

# Queue a build for the Dockerfile in ACR
build_task = acr_client.registries.schedule_run(
    resource_group_name,
    acr_name,
    {
        'platform': {'os': 'Linux', 'architecture': 'amd64'},
        'source': source_properties,
    }
)

print(f"Build task queued for Dockerfile at '{dockerfile_path}' in ACR '{acr_name}'")

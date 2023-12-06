#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient

def stop_all_aks_clusters():
    subscription_id = 'YOUR_SUBSCRIPTION_ID'
    resource_group_name = 'YOUR_RESOURCE_GROUP_NAME'
    # Set the Azure credential using DefaultAzureCredential
    credential = DefaultAzureCredential()

    container_client = ContainerServiceClient(credential, subscription_id)

    # Get all AKS clusters in the specified resource group
    aks_clusters = container_client.managed_clusters.list_by_resource_group(resource_group_name)

    for cluster in aks_clusters:
        if cluster.power_state == 'Running':
            # Stop the AKS cluster if it's currently running
            print(f"Stopping AKS cluster: {cluster.name}")
            container_client.managed_clusters.begin_stop(resource_group_name, cluster.name)
            print(f"AKS cluster {cluster.name} stopping.")

if __name__ == "__main__":
    stop_all_aks_clusters()
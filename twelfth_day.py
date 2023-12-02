#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

import time

def devops_deployment(app_name, version):
    print(f"Initiating deployment of {app_name} - Version {version}")
    print("Running tests...")
    time.sleep(2)  # Simulating test execution (2 seconds delay)
    
    print("Building the application...")
    time.sleep(3)  # Simulating build process (3 seconds delay)
    
    print("Deploying to staging environment...")
    time.sleep(2)  # Simulating deployment to staging (2 seconds delay)
    
    print("Running integration tests on staging...")
    time.sleep(2)  # Simulating integration tests (2 seconds delay)
    
    print("Promoting to production...")
    time.sleep(2)  # Simulating deployment to production (2 seconds delay)
    
    print(f"{app_name} - Version {version} deployed successfully to production!")

# Example deployment
app_name = "MyApp"
app_version = "1.0.0"

devops_deployment(app_name, app_version)
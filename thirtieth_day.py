#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

from datadog import initialize, api

# Set your Datadog API key and application key
options = {
    'api_key': 'YOUR_API_KEY',
    'app_key': 'YOUR_APP_KEY'
}

# Initialize Datadog API client
initialize(**options)

# Define downtime details
scope = ['env:production', 'service:example-service']  
start = 1640971200  
end = 1641057600  
message = "Scheduled maintenance downtime"  

# Create downtime
downtime = api.Downtime.create(scope=scope, start=start, end=end, message=message)

print("Downtime created successfully:")
print(downtime)

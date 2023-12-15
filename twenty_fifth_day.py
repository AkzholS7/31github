#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

import re

class TerraformChecker:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_ec2_tags(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()

                # Define the pattern for AWS EC2 instance resource
                ec2_pattern = r'resource\s+"aws_instance"\s+"(\w+)"\s+{[^}]+}'
                instances = re.findall(ec2_pattern, content)

                for instance in instances:
                    # Pattern to check if a tag 'Name' is present
                    tag_pattern = fr'resource\s+"aws_instance"\s+"{instance}"\s+{{[^}}]+"tags"\s+=\s+{{[^}}]+"Name"\s+=\s+"[^"]+"'
                    tag_match = re.search(tag_pattern, content)
                    if not tag_match:
                        print(f"Warning: EC2 instance '{instance}' is missing 'Name' tag!")

        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Usage
file_path = 'path/to/your/terraform.tf'
checker = TerraformChecker(file_path)
checker.check_ec2_tags()

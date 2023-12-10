#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

import paramiko

def execute_command_ssh(server, username, password, command):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(server, username=username, password=password)
        print(f"Connected to {server} via SSH")
        
        stdin, stdout, stderr = ssh_client.exec_command(command)
        
        # Print the output of the command
        for line in stdout.readlines():
            print(line.strip())

        print("Command executed successfully!")
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"SSH error occurred: {e}")
    finally:
        ssh_client.close()

if __name__ == "__main__":
    server_address = "your_server_address"  # Replace with your server's IP address or hostname
    username = "your_username"  # Replace with your SSH username
    password = "your_password"  # Replace with your SSH password
    command_to_execute = "ls -l"  # Replace with the command you want to execute

    execute_command_ssh(server_address, username, password, command_to_execute)

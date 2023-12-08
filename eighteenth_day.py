#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

import os

def create_directory_and_file(directory_name, file_name):
    try:
        # Create a new directory
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created.")

        # Change to the new directory
        os.chdir(directory_name)

        # Create a new file
        with open(file_name, 'w') as file:
            file.write("This is a new file.")
        print(f"File '{file_name}' created in '{directory_name}'.")

    except OSError as e:
        print(f"Error: {e}")

# Example usage:
directory_name = 'my_directory'
file_name = 'my_file.txt'

create_directory_and_file(directory_name, file_name)
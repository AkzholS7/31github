#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Change the length parameter to generate passwords of different lengths
password = generate_password(16)
print("Generated Password:", password)
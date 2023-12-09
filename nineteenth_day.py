#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe
import random
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "What do you call a fake noodle? An impasta!",
    "I told my wife she should embrace her mistakes. She gave me a hug.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

# Function to get a random joke
def get_random_joke():
    return random.choice(jokes)

# Display a random joke
print("Here's a random joke for you:")
print(get_random_joke())
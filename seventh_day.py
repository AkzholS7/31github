#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

name = input("What is your name? ")
print(
    "Your name is as long or longer than average first name in the United States"
) if len(name) >= 6 else print(
    "Your name is shorter than the average first name in the United States"
)

message = (
    "The first letter in your name is among the five most common"
    if name[0].lower() in ["a", "j", "m", "e", "l"]
    else "The first letter of your name is not among the five most common"
)

print(message)

for letter in name:
    print(
        f"{letter} {'is a vowel' if letter.lower() in ['a', 'e', 'o', 'i', 'o', 'u'] else 'is constant'}"
    )
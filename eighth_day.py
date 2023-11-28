#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

# Example usage:
while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        divide_numbers(num1, num2)
        break
    except ValueError:
        print("Please enter a valid number!")

print("Program completed.")
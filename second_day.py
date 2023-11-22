#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

from statistics import mean, median, mode

print("Welcome to the Basic Data Analysis Tool!")

# Get a list of numbers from the user
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]

# Calculate mean, median, and mode
mean_value = mean(numbers)
median_value = median(numbers)
try:
    mode_value = mode(numbers)
except StatisticsError:
    mode_value = "No unique mode"

# Display the calculated values
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
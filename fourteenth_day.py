#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get user input for the year
year_input = int(input("Enter a year: "))

# Check if it's a leap year and display the result
if is_leap_year(year_input):
    print(year_input, "is a leap year!")
else:
    print(year_input, "is not a leap year.")

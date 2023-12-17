#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

import math

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    return area

circle_area = calculate_circle_area()
print(f"The area of the circle is: {circle_area:.2f}")

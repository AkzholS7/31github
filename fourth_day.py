#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Cannot divide by zero"
        return self.num1 / self.num2

# Example usage:
calc = Calculator(10, 5)

addition_result = calc.add()
print("Addition:", addition_result)

subtraction_result = calc.subtract()
print("Subtraction:", subtraction_result)

multiplication_result = calc.multiply()
print("Multiplication:", multiplication_result)

division_result = calc.divide()
print("Division:", division_result)
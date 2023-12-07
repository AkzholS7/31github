#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old!"


# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes and calling methods
print(person1.introduce())

# Modifying attributes
person1.age = 35

# Calling the method again after modification
print(person1.introduce())
#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

# Function to remove a task from the list
def remove_task():
    print("Current tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

# Function to show all tasks
def show_tasks():
    if tasks:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks yet!")

# Main loop to interact with the to-do list
while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")

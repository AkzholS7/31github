#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"Book '{self.title}' by {self.author} has been checked out.")
        else:
            print(f"Book '{self.title}' is already checked out.")

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            print(f"Book '{self.title}' has been checked in.")
        else:
            print(f"Book '{self.title}' is already checked in.")


# Example usage:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
book2 = Book("Python Crash Course", "Eric Matthes", "Programming")

book1.check_out()  # Checkout book1
book1.check_out()  # Try to checkout book1 again
book1.check_in()   # Checkin book1
book1.check_in()   # Try to checkin book1 again

book2.check_out()  # Checkout book2
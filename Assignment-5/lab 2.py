# Library Management System

class Library:

    def __init__(self):
        self.books = ["Python", "Java", "C Programming"]

    def display(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)

    def borrow(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book borrowed successfully")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print("Book returned successfully")


library = Library()

library.display()

book = input("\nEnter book name to borrow: ")
library.borrow(book)

library.display()

book = input("\nEnter book name to return: ")
library.return_book(book)

library.display()

# OUTPUT:
# Available Books:
# Python
# Java
# C Programming
#
# Enter book name to borrow: Python
# Book borrowed successfully
#
# Available Books:
# Java
# C Programming
#
# Enter book name to return: Python
# Book returned successfully
#
# Available Books:
# Java
# C Programming
# Python

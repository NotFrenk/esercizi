#Exercise 1: 
#Creating an Abstract Class with Abstract Methods
# Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.
"""
from abc import ABC, abstractmethod

import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle area: {circle.area()}\n")
print(f"Circle perimeter: {circle.perimeter()}\n")
print(f"Rectangle area: {rectangle.area()}\n")
print(f"Rectangle perimeter: {rectangle.perimeter()}\n")
"""

# Exercise 2: 
# Implementing Static Methods
# Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
# and another static method multiply that takes two numbers and returns their product.
"""
class MathOperations:
    @staticmethod
    def add(a,b):
        return a + b 
    
    @staticmethod
    def multiply(a,b):
        return a*b
    

if __name__ == "__main__":
    # Utilizzo del metodo statico add
    somma = MathOperations.add(3, 5)
    print(f"La somma di 3 e 5 è: {somma}")

    prodotto = MathOperations.multiply(5,5)
    print(f"Il prodotto di 4 e 6 è: {prodotto}")
"""    


# Exercise 3: 
# Library Management System 
# Create a Book class containing the following attributes: title, author, isbn
# The book class must contains the following methods:

# __str__ method to return a string representation of the book.

# @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". 
# It means that you must use the class reference cls to create a new object of the Book class using a string.

"""
class Book:
    def __init__(self, title:str, author:str, isbn:str):
        self.title=title
        self.author=author
        self.isbn=isbn

    def __str__ (self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}'
    
    @classmethod
    def from_string(cls, book_str):
        title, author, isbn = book_str.split(',')
        return cls(title, author, isbn)

if __name__ == "__main__":
    # Creazione di un libro usando il costruttore
    book1 = Book("1984", "George Orwell", "1234567890")
    print(book1)

    # Creazione di un libro usando il metodo di classe from_string
    book2 = Book.from_string("Brave New World, Aldous Huxley, 0987654321")
    print(book2)
"""




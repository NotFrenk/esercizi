#Exercise 1: 
#Creating an Abstract Class with Abstract Methods
# Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.

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


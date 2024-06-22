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

# Exercise 4: 
# University Management System

# Create a system to manage a university with departments, courses, professors, and students. 

# Create an abstract class Person:
# Attributes:

# name (string)
# age (int)
# Methods:

# __init__ method to initialize the attributes.
# Abstract method get_role to be implemented by subclasses.
# __str__ method to return a string representation of the person.
# Create subclasses Student and Professor that inherit from Person and implement the abstract methods:

# Student:
# Additional attributes: student_id (string), courses (list of Course instances)
# Method enroll(course) to enroll the student in a course.
# Professor:
# Additional attributes: professor_id (string), department (string), courses (list of Course instances)
# Method assign_to_course(course) to assign the professor to a course.

# Create a class Course:
# Attributes:

# course_name (string)
# course_code (string)
# students (list of Student instances)
# professor (Professor instance)
# Methods:

# __init__ method to initialize the attributes.
# add_student(student) to add a student to the course.
# set_professor(professor) to set the professor for the course.
# __str__ method to return a string representation of the course.

from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self,name:str, age:int):
        self.age=age
        self.name=name

    @abstractmethod
    def get_role (self):
        pass

    def __str__(self):
        return f'\t\tPerson\n'\
               f'Name --> {self.name}\n'\
               f'Age --> {self.age}\n'\
               f'Role --> {self.get_role()}\n'
    
class Student(Person):
    def __init__(self, name: str, age: int, student_id:int):
        super().__init__(name, age)

        self.student_id=student_id
        self.courses=[]

    def get_role (self):
        return 'Student'
    
    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)

class Professor(Person):
    def __init__(self, name: str, age: int, professor_id:int, department:str):
        super().__init__(name, age)
        
        self.professor_id=professor_id
        self.department=department
        self.courses = []

    def get_role (self):
        return 'Professor'
    
    def assign_to_course(self, course):
        self.courses.append(course)
        course.professor =self

class Course:
    def __init__(self, course_name:str, course_code:str, ):
        self.course_name=course_name
        self.course_code=course_code
        self.students = []
        self.professor = None

    def add_student(self, student):
        self.students.append(student)
    
    def set_professor(self, professor):
        self.professor = professor

    def __str__(self):
        professor_name = self.professor.name if self.professor else 'None'
        return f'\t\t Course\n'\
               f'Name --> {self.course_name}'\
               f'Code --> {self.course_code}'\
               f'Professor --> {professor_name}'\
               f'Students --> {[student.name for student in self.students]}'
    
class Department:
    def __init__(self, department_name:str):
        self.department_name =department_name
        self.courses = []
        self.professors = []

    def add_course(course)

        
"""    
student = Student("Alice", 20)
professor = Professor("Bob", 40)

print(student)
print(professor)
"""
# Create a class Department:

# Attributes:

# department_name (string)
# courses (list of Course instances)
# professors (list of Professor instances)

# Methods:

# __init__ method to initialize the attributes.
# add_course(course) to add a course to the department.
# add_professor(professor) to add a professor to the department.
# __str__ method to return a string representation of the department.
# Create a class University:

# Attributes:

# name (string)
# departments (list of Department instances)
# students (list of Student instances)

# Methods:

# __init__ method to initialize the attributes.
# add_department(department) to add a department to the university.
# add_student(student) to add a student to the university.
# __str__ method to return a string representation of the university.

# Create a script:

# Create instances of departments, courses, professors, and students.
# Add them to the university.
# Enroll students in courses and assign professors to courses.
# Display the state of the university.

# Create instances
uni = University("Example University")

# Create departments
math_dept = Department("Mathematics")
cs_dept = Department("Computer Science")

# Add departments to the university
uni.add_department(math_dept)
uni.add_department(cs_dept)

# Create courses
course_calc = Course("Calculus", "MATH101")
course_alg = Course("Algebra", "MATH102")
course_prog = Course("Programming", "CS101")

# Add courses to departments
math_dept.add_course(course_calc)
math_dept.add_course(course_alg)
cs_dept.add_course(course_prog)

# Create professors
prof_john = Professor("John Smith", 50, "P123", "Mathematics")
prof_ann = Professor("Ann Brown", 45, "P124", "Computer Science")

# Add professors to departments
math_dept.add_professor(prof_john)
cs_dept.add_professor(prof_ann)

# Assign professors to courses
prof_john.assign_to_course(course_calc)
prof_ann.assign_to_course(course_prog)

# Create students
student_jane = Student("Jane Doe", 21, "S456")
student_mike = Student("Mike Ross", 22, "S457")

# Add students to the university
uni.add_student(student_jane)
uni.add_student(student_mike)

# Enroll students in courses
student_jane.enroll(course_calc)
student_mike.enroll(course_prog)

# Display the state of the university
print(uni)
print()
print(math_dept)
print()
print(cs_dept)
print()
print(course_calc)
print(course_alg)
print(course_prog)
print()
print(student_jane)
print(student_mike)
print()
print(prof_john)
print(prof_ann)
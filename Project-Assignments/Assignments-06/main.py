# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. 
# Use the self keyword to initialize these values via a constructor.
# Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print("Assignment 1")
        print(f"Name: {self.name}, Marks: {self.marks}")


# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created.
#  Use a class variable and a class method with cls to manage and display the count

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
        @classmethod
        def display_count(cls):
            print("Assignment 2")
            print(f"Total objects created: {cls.count}")
            return cls.count



# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start().
#  Instantiate the class and access both from outside the class.


class Car:
    def __init__(self, brand):
        self.brand = brand
        def start(self):
            print("Assignment 3")
            print(f"Car {self.brand} started")
            return self.brand
        
# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name.
#  Add a class method change_bank_name(cls, name) that allows changing the bank name.
#   Show that it affects all instances.

class Bank:
    bank_name = "ABC Bank"
    def __init__(self, name):
        self.name = name
        @classmethod
        def change_bank_name(cls, name):
            cls.bank_name = name
            return cls.bank_name


# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum.
#  No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor)
# and another message when it is destroyed (destructor).
    


    









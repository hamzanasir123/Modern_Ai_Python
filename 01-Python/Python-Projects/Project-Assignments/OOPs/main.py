# What Is OOP

# OOP is a programing style that uses objects and classes to structure code on real time objects.
# OOP is for better code organization, reusability, and maintainability.

# What Is Class

# A class is the blueprint for instances os the class
# and Its a Set Of direction For Reaching A Specific Goal.

class Car:
    pass

# What Is An Object 

# An object is an instance of a class 
# Or A Copy Of the Class
# Or A Live Example Of A Class

mycar = Car()

# What Is an __init__

# The __init__ is an constructor of an instance
# that is for initializing object
# and also put multiple data in instance

class Car:
    def __init__():
        pass


# what is self

# Self is the reference of the current instance 
# Every Instance have its own self

class Car:
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model


# What Is Encapsulation

# Encapsulation is a OOP Principle where we bind data(attribiutes) and methods(functions) together in a class
# and restricting direct access to some of the object's internal parts
# It helps to hide the internal state of an object and allows controlled access through getters, setters, or properties.

class Car:
    def __init__(self):
        # Public Attribute
        self.public = "Public"
        # Protected Attribute
        self._protected = "Protected"
        # Private Attribute
        self.__private = "Private"

a = Car()
print(a.public)  # ✅ OK
print(a._protected)  # ⚠️ Technically allowed, but discouraged
# print(a.__private)  # ❌ Error: AttributeError


# We Can Use Name Mangling To Access Private Attributes But Is Not recommended

print(a._Car__private) # Name Mangling


# Getter & Setter

# Getter is to get private attributes

# Setter is to set private attributes  

class Car:
    def __init__(self):
        # Public Attribute
        self.public = "Public"
        # Protected Attribute
        self._protected = "Protected"
        # Private Attribute
        self.__private = "Private"

    # That Is Getter
    def get_private(self):
        return self.__private
    
    # That Is Setter
    def set_private(self, new_private):
        if new_private != "":
            self.__private = new_private
        else:
            print("❌ Error")


# What Is Inheritance

# Inheritance Means (Virasat)
# Technically A child class takes methods of parent class by inherit 

class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Car Started!")

    def stop(self):
        print("Car Stopped!")


class ToyotaCar(Car):
    pass

car = ToyotaCar("Hondae", "Sonata")
print(car.start())


# There Are 3 types of inheritance

# 1 Single inheritance

# Single inheritance means a one child inherit from one parent

# 2 multiple inheritance

# Multiple inheritance means a one child inherit from multiple parents

# 3 multi level inheritance

# Multi level inheritance means a chain of single inheritance


# What is Polymorphism

# Polymorphism means one body and many faces
# means the a method changes its behaviour behalf of its context

# For example + operator

print(2 + 2) # here + operator Perform Addition
print("2" + "2") # here + operator perform concatination

# What Is Abstraction

# Abstraction means hiding complexity from user and show only essential or needy features

# means user does not have to know that how engine works, how car moving towards or backwards
# user just have to know that this is the accelerator and this is the brake thats it

# What Is Composition

# means STRONG RELATIONSHIP
# Composition is a design technique to impiement "has-a" relationship between objects
# Composition is when one class uses another class as a part of its design.

class Toy:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"Playing with {self.name}")

class ToyBox:
    def __init__(self):
        self.toys = []  # This is composition!

    def add_toy(self, toy):
        self.toys.append(toy)

    def show_all_toys(self):
        for toy in self.toys:
            print(toy.name)

car = Toy("Car")
bike = Toy("Bike")

box = ToyBox()
box.add_toy(car)
box.add_toy(bike)
box.show_all_toys()

# ToyBox is composed of many Toy objects — this is composition!

# What Is The Difference Between Overloading & Overriding

# Method Overloading (Same Method name, different argumants)

# Overloading means creating multiple methods with the same name but different parameters in the same class.

class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(2, 3))       # 5
print(calc.add("2","3"))    # 9

# Same method different arguments = Overloading


# Method Overriding (Same method name, same arguments, different behaviour in subclass)

# Overriding means redefining a method in a child class that already exists in the parent class.

# 📌 Purpose: To change or customize inherited behavior.


class Animal:
    def speak(self):
        print("Some animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

d = Dog()
c = Cat()

d.speak()   # Bark!
c.speak()   # Meow!

# same method name and perameters but different behaviour in child class = Overriding
# This is a real-world use case of method overriding to change inherited behavior based on specific needs.

# Real Life Example Of Overriding....

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdrew {amount}, new balance is {self.balance}"

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            return "Cannot overdraw savings account"
        self.balance -= amount
        return f"Savings withdrawal: {amount}, balance: {self.balance}"

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        # Current accounts allow overdraft up to -500
        if amount > self.balance + 500:
            return "Overdraft limit exceeded"
        self.balance -= amount
        return f"Current account withdrawal: {amount}, balance: {self.balance}"

# Test the behavior
savings = SavingsAccount(1000)
current = CurrentAccount(1000)

print(savings.withdraw(1100))  # Cannot overdraw savings account
print(current.withdraw(1400))  # Current account withdrawal: 1400, balance: -400


# A destructor is a special method in object-oriented programming 
# that is automatically called when an object is destroyed (or goes out of scope or is deleted).
# It is used to perform cleanup tasks like releasing memory, closing files, 
# or disconnecting network resources.

# In Python, destructors are defined using the __del__() method.
# Only one destructor per class.

class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print("File opened.")

    def write_data(self, data):
        self.file.write(data)

    def __del__(self):
        self.file.close()
        print("File closed in destructor.")

# Using the class
handler = FileHandler("example.txt")
handler.write_data("Hello, world!")

# Destructor will be called automatically when 'handler' is deleted or goes out of scope


# What Is The Purpose Of Access Modifiers

# Access Modifiers are used in object-oriented programming to control the visibility and 
# accessibility of classes, methods, and variables from outside the class. 
# Their main purpose is to enforce encapsulation, which is a core principle of OOP.

# For Example 

# Use

# Public attributes
# Protected attributes
# Private attributes

# What is a Static Method?


# A Static Method Belongs To A Class Rather Then An Instance Of A Class

# Defined using @staticmethod decorator in Python.

# Cannot access or modify instance (self) or class (cls) variables.

# Useful for utility functions that are related to the class, but do not depend on object state.


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Call without creating an instance
print(MathUtils.add(5, 3))  # Output: 8

# What is the difference between Class Variables and Instance Variables?

# In object-oriented programming, particularly in Python, both class variables and instance variables are used to store data —
# but they differ in scope, lifetime, and behavior.


# Class Variables

# Belong to: The class itself, shared across all instances.

# Declared in: Directly inside the class, outside any method.

# Accessed using: ClassName.variable_name or self.variable_name (less preferred)

# Same value shared across all objects unless overridden.

class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Bruno")
dog2 = Dog("Max")

print(dog1.species)  # Canine
print(dog2.species)  # Canine


# Instance Variables

# Belong to: Specific instance (object) of a class.

# Declared in: __init__() method or anywhere in the object’s scope.

# Accessed using: self.variable_name

# Unique for each object.

class Dog:
    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Bruno")
dog2 = Dog("Max")

print(dog1.name)  # Bruno
print(dog2.name)  # Max


# What Is Method Chaining

# Method chaining is a programming technique where multiple methods are called on the same object 
# in a single line by returning the object itself (self) from each method.

class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def set_name(self, name):
        self.name = name
        return self  # returns the object for chaining

    def set_age(self, age):
        self.age = age
        return self

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        return self

# Method chaining in action
person = Person()
person.set_name("Ali").set_age(25).display()

# Each method must return self to allow chaining.


#  What is the role of super keyword

# The super keyword in object-oriented programming is used to call methods or 
# constructors of a parent (super) class from a child (subclass). 
# It allows you to reuse the parent class's behavior without rewriting code.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call to parent constructor
        self.breed = breed

    def speak(self):
        super().speak()         # Call to parent method
        print(f"{self.name} barks.")

dog = Dog("Bruno", "Labrador")
dog.speak()

# super() works with single and multiple inheritance.
# Python uses the Method Resolution Order (MRO) to determine what super() refers to.

# What is an Abstract Class

# An abstract class is a class that cannot be instantiated directly and is meant to be inherited by other classes.
# It serves as a blueprint for other classes and may contain abstract methods 
# (methods with no implementation) that must be implemented by subclasses.

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def speak(self):
        pass  # Abstract method

    def sleep(self):
        print("Sleeping...")  # Concrete method

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

# animal = Animal()        ❌ Error: Can't instantiate abstract class
dog = Dog()                # ✅ Valid
dog.speak()                # Output: Dog barks.
dog.sleep()                # Output: Sleeping...


# What is an Interface

# An interface is a programming structure that defines a contract — a set of methods and properties 
# that a class must implement — without providing the implementation itself.

from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def speak(self):
        print(f"{self.name} barks.")

dog = Dog("Bruno")
dog.speak()  # Output: Bruno barks.



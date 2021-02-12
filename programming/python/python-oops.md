# Python Object Oriented Programming:
## Attributes, Classes, Features and More
---
## Object Oriented Programming Concepts

### **TOC**
- What is the 'Python Object-Oriented Programming Concept?'
- What is a **class**
- What is an **object**
- The _init_ method
- Creating classes and objects in Python
- Python OOPs concept
  - Inheritance
  - Polymorphism
  - Abstraction
  - Encapsulation

## What is the Python Object-Oriented Programming Concept?

Objet-oriented programming(OOP) is a methodology that focuses on classes and objects. The concept of OOP in python focuses on building efficient and reusable code. This is also known as DRY(don't repeat yourself). Every individual objects represent a different part of the application having its own logic.

Example: An Object could represent a car with a name, model and color as attributes.

#### What is a Class?

The class can be defined as a collection of objects that define the common attributes and behaviors of all the objects.

Class is defined under a **"Class"** keyword.
Example:
    # defining a class
    class car:
      pass
#### What is an Object?
 
 The object is an entity that has state and behavior. It is an instance of a class that can access the data.
Example:
  # defining a class
  class car:
    pass
  
  # defining an object
  obj = car()
### The _init_ method 

The `_init_` method is run as soon as an objet of a class is created. This method is useful for passing initial value to your objects.

class employee():
  def _init_(self,name,age,id,salary):  # creating a function
    self.name = name          # self = instance of class
    self.age = age
    self.salary = salary
    self.id = id

### Creating Classes and Objects in Python

class employee():
  def _init_(self,name,age,id,salary):    # creating a function
    self.name = name            # self is instance of class
    self.age = age
    self.salary = salary
    self.id = id

emp1 = employee("Jack",19,1300,12)      # Creating Objects
emp2 = employee("Saam",23,2000,13)
print(empl.__dict__)            # prints dictionary

{'name': 'Jack', 'age': 19, 'salary': 12, 'id' ; 1300}

> Here, emp1 and emp2 are objects of the class employee.

## Python OOP Concepts

The four major OOP concepts are:

1. Inheritance:
  - This refers to defining a new class with little or no modification to an existing class.
  - This new class is known as derived (or child) class, and the one from  which it inherits is known as the base(or parent) class.
  - The derived class inherits features from the base class, which adds new features to it.
    - EXAMPLE: 
  - class employee():       #This is a parent class
      def _init_(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    class childemployee(employee):  #This is a child class
      def _init_(self, name, age, salary, id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
    emp1 = employee('jack',19,1400)
    
    print (emp1.age)
    19
    
    # We have created a class called childemployee, which is inheriting the properties of a parent class, and emp1 is passed as a parameter
2. Polymorphism:
  - In OOP , polymorphism refers to a programming language's ability to process objects in more than on form. It is the ability to redefine methods for derived classes.
  - EXAMPLE:
  - class employee():
      def _init_(self,name,age,id,salary):
      self.name = name
      self.age = age
      self.salary = salary
      self.id = id
    def earn(self):
      pass
    
    class childemployee1(employee):
    
      def earn(self): #Run-time polymorphism
        print("Hello")
3. Abstraction:
  - Abstraction is a programming methodology in which details of the programming code are hidden from the user - only essential information is displayed. Abstraction focuses on ideas, rather than events:
  - example:
  - from abc import ABC,abstractmethod
    class employee(ABC):
      def emp_id(self,id,name,age,salary):    #ABSTRACTION
        pass
    
    class childemployee(employee):
      def emp_id(self,id):
        print("emp_id is 1")
    
    emp1 = childemployee()
    emp1.emp_id(id)
    
    emp_id is 1       # print function
    # In the preceding example, we have imported an abstract method. An object is created for childemployee base class, and the functionality of the abstract class is used.
4. Encapsulation:
  - The binding of data and function into one single unit is known as encapsulation. Encapsulation keeps the data safe from misuse and changes in the code can be done independently. 
  - EXAMPLE:
  - class Person:
      def _init_(self, name, age=0):
        self.name = name
        self.age = age
    
      def display(self):
        print(self.name)
        print(self.age)
    
    person = Person('Same', 20)
    #accessing using class method
    person.display()
    #accessing directly from outside
    print(person.name)
    print(person.age)
    # In the class "Person", there are two variables, and we have accessed those variables directly and though a method.
    

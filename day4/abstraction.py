from abc import ABC, abstractmethod

class Sample(ABC):
    @abstractmethod
    def hello(self):
        print("say hello")
    
    def sayHi(self):
        print("Hi")

class Example(Sample):
    def hello(self):
        pass

    def sayHi(self):
        print("Hi! lets go out")
    
ob = Example()
ob.sayHi()

# Cannot create objects for an abstract class
# ob = Sample()
# ob.hello()

"""
Rules for abstract class:
1) Cannot create objects for abstract classes or interfaces
2) Abstract class: Class with mixture of abstract and normal methods
3) Interface: Only has abstract class
4) We provide method definitions for child classes
5) Mandatory to provide definitions for all abstract methods (doesn't matter if you use them or not)
"""

# Task
# Build a library management system Book - ISBN number, author, name, dept, price, manufacturing date; Library - Array which consists of objects of classes - book
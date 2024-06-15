"""
class Wish:
    def wishing(self):
        print("Hello world!")
# Creating an object 
w = Wish()
# Calling the function through object
w.wishing()
"""

# class Student:
#     id=101
#     name="Akshaya"
#     def display(self):
#         print(self.id, "," ,self.name)
# st = Student()
# st.display()

"""
The constructor is initialized using init keyword
Syntax:
def __init__(self, parameters):
    Initialization code
"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# person1 = Person("Akshaya", 18)
# person2 = Person("Varshini",17)
# print(person1.name)
# print(person1.age)

# class Student:
#     def __init__(self,id,name):
#         self.name = name
#         self.id = id
#     def display(self):
#         print(self.id , self.name)
# st=Student(1, "quincy")
# st.display()

# class Vehicle:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#     def display(self):
#         print( f"My vehicle is {self.name} and it is of {self.color} color")
# car=Vehicle("Innova", "Black")
# car.display()

# Destructor - to delete a object
# Program to delete person1

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def __del__(self):
#         print(f"{self.name} has been destroyed")
#     def display(self):
#         print(self.age, self.name)
# person1=Person("Akshaya", 18)
# del person1  # Deleted person1
# person1.display()

# Inheritance - Acquring the properties of parent class by child class
"""
class Parent:
    def method_parent(self):
            print("Parent class")
class Child(Parent):
      def method_child(self):
            print("Child class")
child=Child()
child.method_parent()
"""

# Single Inheritance - Single base class and child class
"""
class Book:  # Parent class
    def author(self):
        print("Author Name: Akshaya Varshini")
class BookName(Book):   # Child class
    def bookName(self):
        print("The book name is secret")
c=BookName()
c.author()
"""

# Multiple Inheritance - Multiple base classes, single child class
"""
class Book1:  # Parent class
    def author1(self):
        print("First Author: Akshaya Varshini")
class Book2:  # Parent class
    def author2(self):
        print("Second Author: Swapna Reddy")
class BookName(Book1, Book2):   # Child class
    def bookName(self):
        print("The book name is: % SECRET %")
c=BookName()
c.author1()
c.author2()
c.bookName()
"""

# Multilevel Inheritance - Grandfather -> Father -> Child
"""
class Grandparent:      # Parent class
    def grand(self, a, b):
        print("Grand Parent",a+b)
class Parent(Grandparent):      # Sub parent class
    def parent(self, a,b):
        print("Parent class", a-b)
class Child(Parent):        # Child class
    def child(self):
        print("Child class")
obj=Child()
obj.grand(1,2)
obj.parent(2,1)
obj.child()
"""

# Hierarchical Inheritance - One parent, multiple children
"""
class Arithmetic:       # Parent class
    def calc(self, a, b):
        print(a**b)
class Addition(Arithmetic): # Child class
    def add(self, a,b):
        print(a+b)
class Division(Arithmetic): # Child class
    def div(self, a,b):
        print(a//b)
obj1 = Addition()   # Creating an object1
obj2 = Division()   # Creating an object2
obj1.calc(2,2)
obj1.add(2,1)
obj2.div(8,2)
obj2.calc(2,5)
"""

# Hybrid Inheritance - Combination of two or more types of inheritance
# Combining Hierarchical and Multiple Inheritance3
"""
class Base:
    def parent(self):
        print("Parent")
class Parent1(Base):
    def func1(self):
        print("Sub Parent")
class Parent2(Base):
    def func2(self):
        print("Sub Parent")
class Child(Parent1, Parent2):
    def child(self):
        print("Child")
obj1=Child()
obj1.parent()
obj1.func1()
obj1.func2()
obj1.child()
"""

# Multilevel and Single Inheritance

class String:
    def func1(self):
        return "I am "
        
class String2(String):
    def func2(self):
        return "Marreddy "
        
class String3(String2):
    def func3(self):
        return "Akshaya Varshini"

class Child(String3):
    def child(self):
        output = "Hello!, " + self.func1() + self.func2() + self.func3()
        print(output)

obj1 = Child()
obj1.child()
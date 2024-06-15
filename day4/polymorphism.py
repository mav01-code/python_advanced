# A method acting or producing different outputs in different circumstances.

# Types - Compile time & Runtime Polymorphism
# 1) Method overloading- same class & method name and different method signature
# 2) Method overriding - different class, same method name & method signature


# Method overriding - It takes the latest method argument
"""
class A:
    def method_1(self, name):
        print(f"Hey {name} how are you?")
    
    def method_1(self, name, age):
        print("Hey {name}, you are {age} years old")

    def method_1(self):
        print("Hello, good morning")

class B:
    def method_1(self):
        print("Hey, how are you?")

ob = A()
ob.method_1()  # Calls method_1 of class A with no arguments
ob.method_1("Akshaya") # TypeError: A.method_1() takes 1 positional argument but 2 were given - because python takes latest positional argument
"""


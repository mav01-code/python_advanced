# Single Inheritance
"""
class Parent:
    myMoney = 1000
    def displayMoney(self):
        print(self.myMoney)

class Child(Parent):
    childMoney = 2000
    def displayTotalMoney(self):
        return self.childMoney + self.myMoney

obj = Child()
print(obj.displayTotalMoney())
"""

# Multiple Inheritance - Diamond problem
"""
class A:
    def method_a(self):
        print("In method a")
    def common_method(self):
        print("I'm in class A")
class B:
    def method_b(self):
        print("In method b")
    def common_method(self):
        print("I'm in class B")
class Driver(A,B):  # First inherited class is A, so the priority order is A->B
    pass
ob = Driver()
ob.method_a()
ob.common_method()
"""
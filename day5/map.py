"""
def square(num):
    return num*num
data = [1, 2, 3, 4, 5]

# squares = []
# for i in data:
#     squares.append(square(i))
# print(squares)

# Using map
res = list(map(square, data)) # Syntax: map(function, iterables), iterable: list, tuple, etc...
print(res)
"""
"""
def verify(age):
    # if age>18:          
    #     return True
    # else:
    #     return False
    return age>18
ages = [12, 45, 23, 54, 13, 14]
adult = list(filter(verify, ages))
print(adult)
"""

# Reduce function - takes  args - reduce(function, data)

from functools import reduce
def func(a, b):
    return a+b

data = [1,2,3,4,5]
sum = reduce(func, data)
print(sum)
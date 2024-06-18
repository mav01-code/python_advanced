# Sorting a 2D array
"""
arr = [
    [1,2,3,4,5],
    [5,4,3,2,1],
    [4,5,2,1,3],
    [1,5,4,3,2],
    [1,2,3,5,4]
]

# for a in arr:
#     a.sort()
# print(arr)

arr.sort(key=lambda ele:ele[-1] )
print(*arr, sep="\n")
"""

# from functools import reduce

# def sum(a,b):
#     return a+b
# data=[1,2,3,4,5]
# res = reduce(lambda a,b: a+b, data, 10)
# print(res)

# Factorial function using lambda and reduce functions
"""
from functools import reduce

n = 5

data=list(range(1, n+1))
print(data)
res = reduce(lambda a,b: a*b, data)
print(res)
"""

# Print ages which are >18
# ages = [12,45,23,25,78,96,15,13]
# adult = list(filter(lambda age: age>18, ages))
# print(adult)

data = [1,2,3,4,5]
res = list(map(lambda num:num*num, data))
print(res)
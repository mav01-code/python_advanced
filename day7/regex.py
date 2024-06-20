"""import re

data = "hello students"
pattern = re.compile = r"\w+"
res = re.finditer(pattern, data)

for row in res:
    print(row)
"""
# OUTPUT : 
# <re.Match object; span=(0, 5), match='hello'>
# <re.Match object; span=(6, 14), match='students'>

"""
import re

data = "hello students"
pattern = re.compile = r"\b"  #  s - spaces, S - other than spaces
res = re.finditer(pattern, data)

for row in res:
    print(row)
"""

"""
import re

data = "ab cd ef ab cd ef"
pattern = re.compile( r"[a-z]" ) # Checks and prints only the alphabets present in the data
res = re.finditer(pattern, data)

for row in res:
    print(row)
"""

# import re

# data = "1234567890"
# pattern = re.compile( r"\d{10}" ) # Prints all 10 digits at a time
# res = re.finditer(pattern, data)

# for row in res:
#     print(row)

#                   ------------------------- Email verification---------------------------
"""
import re

file = open("D:\\python_advanced\\day7\\example.txt","r")
data = file.read()
pattern = re.compile( r"[a-zA-Z0-9]{10}@iare.ac.in" ) 
res = re.finditer(pattern, data)

for row in res:
    print(row)
"""

"""
import re

file = open("D:\\python_advanced\\day7\\example.txt","r")
data = file.read()
pattern = re.compile( r"[a-zA-Z0-9-._]+@[a-z0-9]+\.[a-z.]+" ) 
res = re.finditer(pattern, data)

for row in res:
    print(row)
"""

#                   ------------------------- Roll Number Verification---------------------------

import re

file = open("D:\\python_advanced\\day7\\example.txt","r")
data = file.read()
pattern = re.compile( r"[0-9]{2}[0-9]{2}[0-9]{1}[A-Z]{1}[0-9]{2}[A-Z0-9]{2}" ) 
res = re.finditer(pattern, data)

for row in res:
    print(row)

    #                   ------------------------- Name Verification---------------------------

import re

file = open("D:\\python_advanced\\day7\\example.txt","r")
data = file.read()
pattern = re.compile( r"(Mrs|Ms|Mr)[. ]*[a-zA-Z ]+" ) 
res = re.finditer(pattern, data)

for row in res:
    print(row)


   #                   ------------------------- Name Verification---------------------------

import re

file = open("D:\\python_advanced\\day7\\example.txt","r")
data = file.read()
pattern = re.compile( r"(?=[A-Z]+)(?=[a-z])(?=)" ) 
res = re.finditer(pattern, data)

for row in res:
    print(row)
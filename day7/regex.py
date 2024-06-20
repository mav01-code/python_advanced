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

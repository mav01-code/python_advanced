# import json

# Reading a json file
"""
file = open("D:\\python_advanced\\day5\\data.json","r")

# json.load() # Read the data

# json.dump() # Send the data
data = json.load(file)
print(data)
print(type(data))

file.close()
"""

# Writing a json file
"""
file = open("file.json","w")
data = {
    "name" : "Akshaya Varshini",
    "age" : 18,
    "Mobile" : [9951829207, 9951581213]
}

json.dump(data, file, indent = 4) # Indentation - 4 spaces

file.close()
"""

# CSV file - It is stored in the text format separated by commas

# Reading a csv file
"""
import csv

file = open("D:\\python_advanced\\day5\\data.csv", "r")
read = csv.reader(file)
for row in read:
    print(row)
file.close()
"""

# Writing in a csv file
"""
import csv

file = open("sample.csv", "w")
write = csv.writer(file)

data = [
    ["name", "roll", "email"],
    ["Akshaya", "0H", "23951a050h@iare.ac.in"],
    ["Varshini", "1", "dontknow@gmail.com"]
]

write.writerows(data)
"""

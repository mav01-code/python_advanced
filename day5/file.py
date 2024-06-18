import json

file = open("D:\\python_advanced\\day5\\data.json","r")

# json.load() # Read the data

# json.dump() # Send the data
data = json.load(file)
print(data)
print(type(data))

file.close()
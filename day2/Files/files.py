# Opening file in read mode

# Method - 1
# f=open("description.txt","r")
# print(f.read())
# f.close()

# Method - 2
# f=open("D:\\python_advanced\\day2\\TxtFile\\txt1.txt","r")
# print(f.read())
# f.close()

# Method - 3
# with open("description.txt","r") as file:
#     print(file.read())
#     file.close()

# Writing in a file - erases existing data and writes new content. If the file doesn't exist, creates a new file.

# with open("description1.txt","w") as file:
#     file.write("Hello.. how are you?")
#     file.close()

# Appending a file - adds extra data without erasing the existing content

# with open("description.txt","a") as file:
#     file.write("\nAkshaya Varshini")
#     file.close() 

# Reads a single line

# with open("description.txt","r") as file:
#     print(file.readline())

# Reads all lines 

# with open("description.txt","r") as file:
#     print(file.readlines())

# prints all lines in a file using for loop

# with open("description.txt","r") as file:
#     for line in file:
#         print(line, end=" ")


# with open("description.txt","r") as file:
#     content=file.read()

# with open("description1.txt","w") as file:
#     print(content)


# CSV files - stores data in the form of table

# import csv
# with open("description.csv","w", newline='') as file:
#     writer=csv.writer(file)
#     writer.writerow(["Name","Age","City"])
#     writer.writerow(["Alice","30","NewYork"])
#     writer.writerow(["Bob","25","Los Angeles"])

# To read the existing data in a csv file

# import csv
# with open("description.csv","r") as file:
#     reader=csv.reader(file)
#     for read in reader:
#         print(read)

# JSON - JavaScript Object Notation, stores data in key-value pairs

# import json
# data = {
#     "name" : "grapes",
#     "color" : "green",
# }
# file = open("description1.json","w")
# json.dump(data,file)
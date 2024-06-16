fp = open("D:\\python_advanced\\day4\\example.txt","r")
content = fp.readlines()

content.append("\nI'm fine, how are you?")

fp.close()

writer = open("D:\\python_advanced\\day4\\example.txt","w")
writer.writelines(content)
writer.close()

# Task - Library Management System
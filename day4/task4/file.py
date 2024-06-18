fp = open("D:\\python_advanced\\day4\\task4\\file.txt","r")
content = fp.readlines()

content.append()

fp.close()

writer = open("D:\\python_advanced\\day4\\example.txt","w")
writer.writelines(content)
writer.close()
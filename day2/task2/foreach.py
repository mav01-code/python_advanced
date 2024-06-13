file_path = "D:\\python_advanced\\day2\\task2\\description2.txt"

# Read the file and store the lines
with open(file_path, "r") as file:
    lines = file.readlines()
    print(lines)

# Write back to the same file
with open(file_path, "w") as file:
    for line in lines:
        file.write("Hello!, "+line)


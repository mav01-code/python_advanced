import csv
import os

# Define the path for the CSV file
DATABASE_FILE = 'D:\\python_advanced\\day5\\task5\\students.csv'

# Predefined users for login
USERS = {
    "faculty": {
        "username": "faculty",
        "password": "faculty123",
        "role": "faculty"
    },
    "students": {
        "23951A0501": {
            "password": "01",
            "role": "student"
        },
        "23951A0504": {
            "password": "04",
            "role": "student"
        },
        "23951A050G": {
            "password": "0G",
            "role": "student"
        },
        "23951A050H": {
            "password": "0H",
            "role": "student"
        },
        "23951A050M": {
            "password": "0M",
            "role": "student"
        },
        "23951A050R": {
            "password": "0R",
            "role": "student"
        },
        "23951A050U": {
            "password": "0U",
            "role": "student"
        },
        "23951A050V": {
            "password": "0V",
            "role": "student"
        },
        "23951A050W": {
            "password": "0W",
            "role": "student"
        },
        "23951A0515": {
            "password": "15",
            "role": "student"
        },
        "23951A0516": {
            "password": "16",
            "role": "student"
        },
        "23951A051D": {
            "password": "1D",
            "role": "student"
        },
        "23951A051T": {
            "password": "1T",
            "role": "student"
        },
        "23951A051U": {
            "password": "1U",
            "role": "student"
        },
        
    }
}

def load_students():
    if not os.path.exists(DATABASE_FILE):
        return []
    with open(DATABASE_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_students(students):
    with open(DATABASE_FILE, mode='w', newline='') as file:
        fieldnames = ['Name', 'Roll Number', 'Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def add_student(name, email, roll_number):
    students = load_students()
    for student in students:
        if student['Roll Number'] == roll_number:
            print(f"Student with roll number {roll_number} already exists.")
            return
    new_student = {
        "Name": name,
        "Email": email,
        "Roll Number": roll_number
    }
    students.append(new_student)
    save_students(students)

def update_student(roll_number, name=None, email=None):
    students = load_students()
    for student in students:
        if student['Roll Number'] == roll_number:
            if name:
                student['Name'] = name
            if email:
                student['Email'] = email
            save_students(students)
            return
    print("Student not found!")

def get_student(roll_number):
    students = load_students()
    for student in students:
        if student['Roll Number'] == roll_number:
            return student
    return None

def display_students():
    students = load_students()
    for student in students:
        print(f"Roll Number: {student['Roll Number']}, Name: {student['Name']}, Email: {student['Email']}")

def login():
    username = input("Enter username (faculty or roll number): ")
    password = input("Enter password: ")

    if username == "faculty" and USERS["faculty"]["password"] == password:
        return USERS["faculty"]
    elif username in USERS["students"] and USERS["students"][username]["password"] == password:
        user_info = USERS["students"][username]
        user_info["username"] = username
        return user_info
    else:
        print("Invalid username or password.")
        return None

# Example usage
if __name__ == "__main__":
    user = login()
    if user:
        role = user['role']
        if role == 'faculty':
            while True:
                print("\n1. Add Student")
                print("2. Update Student")
                print("3. Get Student Info")
                print("4. Display All Students")
                print("5. Exit")
                choice = input("\nEnter your choice: ")

                if choice == '1':
                    name = input("Enter student name: ")
                    email = input("Enter student email: ")
                    roll_number = input("Enter student roll number: ")
                    add_student(name, email, roll_number)
                elif choice == '2':
                    roll_number = input("Enter student roll number: ")
                    name = input("Enter new name (leave blank to keep current): ")
                    email = input("Enter new email (leave blank to keep current): ")
                    update_student(roll_number, name=name if name else None, email=email if email else None)
                elif choice == '3':
                    roll_number = input("Enter student roll number: ")
                    student = get_student(roll_number)
                    if student:
                        print(f"Roll Number: {student['Roll Number']}, Name: {student['Name']}, Email: {student['Email']}")
                    else:
                        print("Student not found!")
                elif choice == '4':
                    display_students()
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif role == 'student':
            roll_number = user['username']
            student = get_student(roll_number)
            if student:
                print(f"Roll Number: {student['Roll Number']}, Name: {student['Name']}, Email: {student['Email']}")
            else:
                print("Student not found!")
    else:
        print("Login failed.")

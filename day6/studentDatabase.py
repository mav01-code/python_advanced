import csv


class Student:
    def __init__(self, rollnumber):
        self.rollnumber = rollnumber
        file = open("D:\\python_advanced\\day6\\db.csv","r")
        self.dbReader = csv.reader(file)

    def getMyDetails(self, roll=None):
        # Todo: Add Validation
        def filterRoll(ele):
            if ele[2]==self.rollnumber:
                return ele
        myDetails = list(filter(filterRoll, list(self.dbReader)))
        return myDetails[0]
# stu = Student("1001")
# stu.displayMyDetails()


    def displayMyDetails(self):
        details = self.getMyDetails(self.rollnumber)
        print(details)

class Faculty(Student):
    def __init__(self):
        file = open("D:\\python_advanced\\day6\\db.csv","r")
        self.dbReader = csv.reader(file)

    def addStudent(self):
        fp = open("D:\\python_advanced\\day6\\db.csv","a")
        dbWriter = csv.writer(fp)

        name = "\nSample"
        email = "sample@gmail.com"
        roll = "1003"
        # details = [f"\n{name},{email},{roll}"]
        details = [name,email,roll]
        dbWriter.writerow(details)

        fp.close()

        def displayMyDetails(self, roll, newdetails):
            details = self.getStudentDetails()

    def updateStudent(self,name, email, roll, newdetails):
        student_data = list(self.dbReader)
        for row in student_data:
            if row[2]==roll:
                row[0]=name
                row[1]=email
                break
        fp = open("D:\\python_advanced\\day6\\db.csv","w")
        dbWriter = csv.writer(fp)
        dbWriter.writerows(student_data)
        fp.close()

fac = Faculty()
fac.updateStudent("Vignesh","vignesh@gmail.com", "1001")

def addStudent():
    pass

def displayStudentDetails():
    pass
class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" --- " + book)
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(f"{bookname} BOOK IS NOT AVAILABLE OR TAKEN BY SOMEONE ELSE, WAIT UNTIL HE/SHE RETURNS.\n")
        else:
            track.append({name: bookname})
            print("BOOK ISSUED. \n")
            self.books.remove(bookname)

    def returnBook(self, bookname):
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.append(bookname)

class Student():
    def requestBook(self):
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book


if __name__ == "__main__":

    library = Library(
        ["Engineering Graphics with AutoCAD", "Mathematics for Engineers", "Spring Boot Edition: 1.2", "Data Visualization with Mathplotlib & Numpy", "Power BI", "R Programming"])
    student = Student()
    track = []

    print("\t\t\t\t-------%-------WELCOME TO THE AKSHAYA'S LIBRARY-------%-------")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Track books\n5. exit the library\n""")

    while (True):
        # print(track)
        try:
            user = int(input("Enter your choice: "))

            if user == 1:  # display
                library.displayAvailableBooks()
            elif user == 2:  # borrow
                library.borrowBook(
                    input("Enter your name: "), student.requestBook())
            elif user == 3:  # return
                library.returnBook(student.returnBook())
            elif user == 4:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
            
            elif user == 5: #exit
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:              #catch errors
            print("INVALID INPUT!")
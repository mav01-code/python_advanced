class Book:
    def __init__(self, name, isbn, author, mfg, edition, barcodeId, price, dept):
        self.name = name
        self.isbn = isbn
        self.author = author
        self.mfg = mfg
        self.edition = edition
        self.barcodeId = barcodeId
        self.price = price
        self.dept = dept

    def display(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")

# Creating an instance of the Book class
book = Book("Pride & Prejudice", "1234567890", "F. Scott Fitzgerald", "1925", "1st", "001", "$10", "Literature")
book.display()

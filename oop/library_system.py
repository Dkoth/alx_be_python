#library_system.py

#Constructor to initialize class Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    #User-friendly representation using str
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

#Inheritance of derived class EBook from Book

class EBook(Book):
    def __init__(self, title, author, file_size):
        #Calling the base class Book
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
#class PrintBook inheriting from Book

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        #Calling the base class Book
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
#Initializing composition 
class Library:
    def __init__(self):
        self.books = []
    #Adding method library
    def add_book(self, book):
        self.books.append(book)
    #Method listing all books in library
    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)



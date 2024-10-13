#book_class.py
class Book:
    
    #Constructor to initialize 'title', 'author', year
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    #Deconstructor to display message when the object is deleted
    def __del__(self):
        print("Deleting {self.title}")

    #__str__method for user-friendly string representation
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    #__repr__method for more detailed
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"




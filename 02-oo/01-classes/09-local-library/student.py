class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    

book1 = Book("We are football", "Jashan")
book2 = Book("We are football2", "Jashan")
book3 = Book("We are football3", "Jashan")
book4 = Book("We are baseball", "Sonam")
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for library_book in self.books:
            if book.title == library_book.title and book.author == library_book.author:
                self.books.remove(book)

    def search_books(self, search_string):
        search_string = search_string.lower()
        return [book for book in self.books if search_string in book.title.lower() or search_string in book.author.lower()]

library = Library("HasseltBIB")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
# library.remove_book(book2)


for book in library.search_books("jashan"):
    print(f'Title: {book.title}, Author: {book.author}')

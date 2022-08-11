import sqlite3

import time

class Book():
    def __init__(self,name,author,publisher,type,edition):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.type = type
        self.edition = edition

    def __str__(self):

        return "Name of the book: {}\nAuthor: {}\nPublisher: {}\nType:{}\nEdition:{}\n".format(self.name,self.author,self.publisher,self.type,self.edition)


class Library():
    def __init__(self):

        self.create_connection()

    def create_connection(self):

        self.connect = sqlite3.connect("bookshelf.db")
        self.cursor = self.connect.cursor()

        enquiry = ("Create Table if not exists books (name TEXT,author TEXT,publisher TEXT,type TEXT,edition INT)")

        self.cursor.execute(enquiry)
        self.connect.commit()

    def cut_connection(self):
        self.connection.close()

    def list_books(self):

        enquiry = "Select * from books"

        self.cursor.execute(enquiry)

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("No books in the library.....")
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                print(book)

    def enquire_book(self,name):
        enquiry = "Select * from books where name = ?"

        self.cursor.execute(enquiry(name,))

        books = self.cursor.fetchall()

        if len(books == 0):
            print("No such book exists...")
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])
            print(book)

    def add_book(self,book):
        enquiry = "Insert into books Values(?,?,?,?,?)"

        self.cursor.execute(enquiry(book.name,book.author,book.publisher,book.type,book.edition))

        self.connect.commit()

    def delete_book(self,name):
        enquiry = "Delete from books where name = ?"

        self.cursor.execute(enquiry(name,))
        self.connect.commit()
    def change_edition(self,name):
        enquiry = "Select * from books where name = ?"

        self.cursor.execute(enquiry(name,))

        books = self.cursor.fetchall()

        if len(books == 0):
            print("No such book exists....")
        else:
            edition = books [0][4]
            edition += 1
            enquiry2 = "Update books set edition = ? where isim = ?"
            self.cursor.execute(enquiry2(edition,name))
            self.connect.commit()

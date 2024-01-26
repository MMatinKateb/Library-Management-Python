import sqlite3
import sys

class Book:
    # attributes
    title = None 
    author = None 
    isbn = None
    available_copies = None 
    total_copies = None

    # Methods
    def __init__(self, title, author, isbn, available_copies, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies
        self.total_copies = total_copies

    def print_book_info(self):
        print(f"Title: {self.title} - Author: {self.author} - ISBN: {self.isbn} - Available Copies: {self.available_copies}", end=" - ")
        print(f"Total Copies: {self.total_copies}")
        # print("=#"*40)

class Library:
    # attr
    database = None; books = []

    # methods
    def __init__(self, book_list):
        # connect to db
        self.database = sqlite3.connect('Library.db')

        # check if books exist in db
        cursor = self.database.cursor()
        cursor.execute("SELECT * FROM Books")
        res = cursor.fetchall()
        if res:
            # append data from db to book_list
            for row in res:
                book = Book(row[1], row[2], row[0], row[3], row[4])
                self.books.append(book)
        else:
            # use book_list passed as argument
            self.books = book_list
            self.store_db_data()
        cursor.close()

    def show_books(self):
        cur = self.database.cursor()
        cur.execute("SELECT * FROM Books")
        res = cur.fetchall()
        print("--"*40)
        for row in res:
            book = Book(row[1], row[2], row[0], row[3], row[4])
            book.print_book_info()
        print("--"*40)
        cur.close()

    def take_parameters():
        title = sys.argv[1]
        author = sys.argv[2]
        isbn = int(sys.argv[3])
        available_copies = int(sys.argv[4])
        total_copies = int(sys.argv[5])
        
        # create book obj
        book = Book(title, author, isbn, available_copies, total_copies)
        return book
    
    def add_book(self, new_book):
        self.books.append(new_book)

    # search by author
    def search_by_author(self, author_name):
        cursor = self.database.cursor()
        cursor.execute(f"SELECT * FROM Books WHERE author='{author_name}';")
        # fetch
        res = cursor.fetchall()
        # print
        print("--"*40)
        for row in res:
            book = Book(row[1], row[2], row[0], row[3], row[4])
            book.print_book_info()
        print("--"*40)
        cursor.close()
    
    def create_db_table(self):
        cursor = self.database.cursor()
        query='''CREATE TABLE Books (
            isbn INTEGER PRIMARY KEY UNIQUE NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            available_copies INTEGER NOT NULL,
            total_copies INTEGER NOT NULL
        );'''
        cursor.execute(query)
        self.database.commit()
        cursor.close()
    
    def insert_books(self):
        for book in self.books:
            cursor = self.database.cursor()
            query = f"INSERT INTO Books (isbn, title, author, available_copies, total_copies) VALUES ({book.isbn}, '{book.title}', '{book.author}', {book.available_copies}, {book.total_copies})"
            cursor.execute(query)
            self.database.commit()
            cursor.close()

    def remove_book(self, book_name):
        if book_name:
            cursor = self.database.cursor()
            cursor.execute(f"DELETE FROM Books WHERE title='{book_name}'")
            self.database.commit()
            cursor.close()
            if book_name in self.books:
                self.books.remove(book_name)
        else: # Flush data
            cursor = self.database.cursor()
            cursor.execute(f"DELETE FROM Books")
            self.database.commit()
            cursor.close()
            if book_name in self.books:
                self.books.remove(book_name)

    def store_db_data(self):
        for book in self.books:
            cursor = self.database.cursor()
            query = f"INSERT INTO Books (isbn, title, author, available_copies, total_copies) VALUES ({book.isbn}, '{book.title}', '{book.author}', {book.available_copies}, {book.total_copies})"
            cursor.execute(query)
            self.database.commit()
            cursor.close()
        
    def __del__(self):
        self.database.close()
import sqlite3

from domain.book import Book
from domain.ports import BookRepository

class SQLiteBookRepo(BookRepository):
    
    def __init__(self, db_path="books.db"):
        self.db_path = db_path
        self._create_table()
        
    
    def _connect(self):
        return sqlite3.connect(self.db_path)
    
    def _create_table(self):
        connection = self._connect()
        cursor = connection.cursor()
        
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                pages INTEGER NOT NULL,
                isbn TEXT UNIQUE NOT NULL
            )
            """
        )
        
        connection.commit()
        connection.close()
        
    def store(self, book):
        connection = self._connect()
        cursor = connection.cursor()
        
        cursor.execute(
            "INSERT INTO books (id, title, pages, isbn) VALUES (?, ?, ?, ?)", (book.id, book.title, book.pages, book.isbn)
        )
        
        connection.commit()
        connection.close()
        
    def check_if_book_exists_on_isbn(self, isbn : str) -> bool:
        connection = self._connect()
        cursor = connection.cursor()
        
        cursor.execute("SELECT 1 FROM books WHERE isbn = ?", (isbn,))
        exists - cursor.fetchone() is not None
        
        connection.close()
        return exists
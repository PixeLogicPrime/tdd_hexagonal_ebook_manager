import sqlite3

from app.domain.book import Book
from app.domain.ports import BookRepository

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
        
    def get_all(self) -> list[Book]:
        connection = self._connect()
        cursor = connection.cursor()
        
        cursor.execute("SELECT id, title, pages, isbn FROM books")
        rows = cursor.fetchall()
        connection.close()

        # Zamieniamy każdy wiersz na obiekt Book
        books = [
            Book(
                id=row[0],
                title=row[1],
                pages=row[2],
                isbn=row[3]
            )
            for row in rows
        ]
        return books
        
    def check_if_book_exists_on_isbn(self, isbn : str) -> bool:
        connection = self._connect()
        cursor = connection.cursor()
        
        cursor.execute("SELECT 1 FROM books WHERE isbn = ?", (isbn,))
        exists = cursor.fetchone() is not None
        
        connection.close()
        return exists
    
    def get_book_where_isbn(self, isbn : str) -> Book | None:
        connection = self._connect()
        cursor = connection.cursor()
        
        cursor.execute("SELECT 1 FROM books WHERE isbn = ?", (isbn,))
        exists = cursor.fetchone() is not None
        
        connection.close()
        return exists
from abc import ABC, abstractmethod
from app.domain.book import Book

class BookRepository(ABC):
    
    @abstractmethod
    def store(self, book: Book) -> None:
        pass
    
    
    @abstractmethod
    def check_if_book_exists_on_isbn(self, isbn: str) -> bool:
        pass
    
    
    @abstractmethod
    def get_book_where_isbn(self, isbn: str) -> Book | None:
        pass
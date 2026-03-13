from abc import ABC, abstractmethod
from domain.book import Book

class BookRepository(ABC):
    
    @abstractmethod
    def store(self, book: Book) -> None:
        pass
    
    
    @abstractmethod
    def check_if_book_exists_on_isbn(self, isbn: str) -> Book | None:
        pass
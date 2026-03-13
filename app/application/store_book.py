from app.domain.book import Book
from app.domain.ports import BookRepository
import uuid

class StoreBook:
    
    def __init__(self, repo: BookRepository):
        self.repo = repo
        
    def execute(
        self,
        title: str,
        pages: int,
        isbn: str
    ):
        check_if_book_exists = self.repo.check_if_book_exists_on_isbn(isbn)
        if check_if_book_exists:
            raise ValueError(f"Pozycja o podanym ISBN : {isbn} istnieje w bazie.")
        
        book = Book(
            id = str(uuid.uuid4()),
            title=title,
            pages=pages,
            isbn=isbn
        )
        
        self.repo.store(book)
        return book
    
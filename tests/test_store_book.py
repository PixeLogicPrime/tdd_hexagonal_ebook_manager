import pytest

from app.application.store_book import StoreBook
from app.domain.book import Book
from app.domain.ports import BookRepository

class InMemoryRepo(BookRepository):
    def __init__(self):
        self.books = []

    def stroe(self, book: Book) -> None:
        self.books.append(book)

    def check_if_book_exists_on_isbn(self, isbn: str) -> bool:
        return any(b.isbn == isbn for b in self.books)


@pytest.fixture
def service():
    repo = InMemoryRepo()
    return StoreBook(repo)

def test_create_book(service):
    book = service.execute("Hobbit", 300, "123456")
    assert book.title == "Hobbit"
    assert book.pages == 300
    assert book.isbn == "123456"
    assert len(book.id) > 0

def test_duplicate_isbn_raises(service):
    service.execute("Hobbit", 300, "123456")
    import pytest
    with pytest.raises(ValueError):
        service.execute("Hobbit2", 200, "123456")
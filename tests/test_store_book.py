import pytest

from app.application.store_book import StoreBook
from app.infrastructure.sqlite_repo import SQLiteBookRepo
from app.domain.book import Book
from app.domain.ports import BookRepository




@pytest.fixture
def service():
    repo = SQLiteBookRepo(db_path=":memory")
    return StoreBook(repo)

def test_create_book(service):
    book = service.execute("Hobbit", 300, "13")
    assert book.title == "Hobbit"
    assert book.pages == 300
    assert book.isbn == "13"
    assert len(book.id) > 0

def test_duplicate_isbn_raises(service):
    service.execute("Hobbit", 300, "14")
    import pytest
    with pytest.raises(ValueError):
        service.execute("Hobbit2", 200, "14")
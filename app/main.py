from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.infrastructure.sqlite_repo import SQLiteBookRepo
from app.application.store_book import StoreBook
from app.application.list_books import ListBooks

app = FastAPI()
repo = SQLiteBookRepo()
service = StoreBook(repo)
list_book_service = ListBooks(repo)

class BookRequest(BaseModel):
    title: str
    pages: int
    isbn: str
    

@app.post("/books")
def create_book(book: BookRequest):
    try:
        return service.execute(
            book.title,
            book.pages,
            book.isbn
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/books")
def list_books():
    return list_book_service.execute() 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from infrastructure.sqlite_repo import SQLiteBookRepo
from application.store_book import StoreBook

app = FastAPI()
repo = SQLiteBookRepo()
service = StoreBook(repo)

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
    return None 
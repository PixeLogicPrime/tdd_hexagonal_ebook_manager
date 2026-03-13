from dataclasses import dataclass
import uuid

@dataclass
class Book:
    id: uuid
    title: str
    pages: int
    isbn: str
    
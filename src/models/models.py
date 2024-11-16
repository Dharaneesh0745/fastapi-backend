from pydantic import BaseModel

class Book(BaseModel):
    id: int
    name: str
    author: str
    publisher: str
    page_number: int
    publication_year: int
    genre: str
    isbn: str
    language: str

class UpdateBook(BaseModel):
    name: str
    author: str
    publisher: str
    page_number: int
from fastapi import status, APIRouter
from typing import List
from fastapi.exceptions import HTTPException
from src.data.data import books
from src.models.models import Book, UpdateBook

router = APIRouter()

@router.get("/")
async def index():
    return {"message": "Hello, World!"}

@router.get("/books", response_model = List[Book], status_code = status.HTTP_200_OK)
async def get_all_books():
    return books

@router.get("/book/{book_id}")
async def get_a_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book Not Found!")

@router.post("/books", status_code = status.HTTP_201_CREATED)
async def create_a_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

@router.patch("/book/{book_id}", status_code = status.HTTP_202_ACCEPTED)
async def update_a_book(book_id: int, update_book: UpdateBook):
    for book in books:
        if book["id"] == book_id:
            book["name"] = update_book.name
            book["author"] = update_book.author
            book["publisher"] = update_book.publisher
            book["page_number"] = update_book.page_number

            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book Not Found!")

@router.delete("/book/{book_id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book Deleted!"}

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book Not Found!")

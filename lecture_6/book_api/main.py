from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

import models
import schemas
from database import engine, get_db
from dependencies import validate_book_id

# Create all database tables based on the models
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI(
    title="Book Collection API",
    description="A simple API for managing a book collection",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    """Health check endpoint for Docker"""
    return {"status": "ok"}

@app.get("/")
def read_root():
    """Root endpoint providing API information and documentation links"""
    return {
        "message": "Welcome to a Book Collection!",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.post(
    "/books/",
    response_model=schemas.BookResponse,
    status_code=status.HTTP_201_CREATED
)

def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """Create a new book in the collection"""
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=List[schemas.BookResponse])
def read_books(
        skip: int = Query(0, ge=0),
        limit: int = Query(100, ge=1, le=100),
        db: Session = Depends(get_db)
)-> List[models.Book]:
    """Get a paginated list of all books in the collection"""
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books


@app.get("/books/search/", response_model=List[schemas.BookResponse])
def search_books(
        title: Optional[str] = Query(None),
        author: Optional[str] = Query(None),
        year: Optional[int] = Query(None),
        db: Session = Depends(get_db)
):
    """Search books by title, author, or publication year"""
    query = db.query(models.Book)

    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(models.Book.year == year)

    return query.all()


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int = Depends(validate_book_id)):
    """Get details of a specific book by ID"""
    return book_id


@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(
        book_update: schemas.BookUpdate,
        book: models.Book = Depends(validate_book_id),
        db: Session = Depends(get_db)
):
    """Update an existing book's information"""
    update_data = book_update.dict(exclude_unset=True)

    for field, value in update_data.items():
        if value is not None:
            setattr(book, field, value)

    db.commit()
    db.refresh(book)
    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
        book: models.Book = Depends(validate_book_id),
        db: Session = Depends(get_db)
):
    """Delete a book from the collection"""
    db.delete(book)
    db.commit()
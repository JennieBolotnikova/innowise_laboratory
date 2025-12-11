from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import models


def validate_book_id(book_id: int, db: Session = Depends(get_db)):
    """Validate that a book with the given ID exists in the database"""
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} is not found"
        )

    return book
from pydantic import BaseModel, Field
from typing import Optional


class BookBase(BaseModel):
    """Base schema for book data with common attributes and validation rules"""
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=100)
    year: Optional[int] = Field(None, ge=1000, le=2100)

class BookCreate(BookBase):
    """Schema for creating a new book"""
    pass

class BookUpdate(BaseModel):
    """Schema for updating an existing book (partial updates)"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    year: Optional[int] = Field(None, ge=1000, le=2100)

class BookResponse(BookBase):
    """Schema for API responses containing book data"""
    id: int

    class Config:
        from_attributes = True
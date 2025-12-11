from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    """SQLAlchemy model representing a book in the database"""
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)

    def __repr__(self):
        """Return a string representation of the Book instance"""
        return f"<Book(id={self.id}, title='{self.title}')>"
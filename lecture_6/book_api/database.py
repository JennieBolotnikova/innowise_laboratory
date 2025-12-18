from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL for SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create a database engine instance
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency function to get a database session
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
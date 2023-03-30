from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from core.config import settings

#Starts a new session, HOST_URL is the remote database, POSTGRES_URL is the local database
SQLALCHEMY_DATABASE_URL = settings.HOST_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

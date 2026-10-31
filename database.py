import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DB_URL = os.getenv("DB_URL")
USERNAME = os.getenv("DB_USER")
PASSWORD = os.getenv('DB_PASSWORD')


DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{DB_URL}:3306/doc_db"

engine = create_engine(
    DATABASE_URL,
    echo = True
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
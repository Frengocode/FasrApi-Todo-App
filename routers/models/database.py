from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine



SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:python$_venv@localhost:5432/ToDo'


Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessinLocal = sessionmaker(bind=engine, autoflush=False, autocommit = False)

async def get_db():
    db = SessinLocal()
    try:
        yield db
    finally:
        db.close()


import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
print(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

engine = create_engine(str(SQLALCHEMY_DATABASE_URL))

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():

    '''Function to session require'''

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


# HOW TO MIGRATE DB: 

# cd /media/daniil/Work/Python/git_projects/FastAPI-REST/app/pkg/db/migrations$

# alembic revision --autogenerate -m "Commit name"

# alembic upgrade head
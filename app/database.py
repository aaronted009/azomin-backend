from sqlmodel import create_engine, Session, SQLModel
from fastapi import Depends
from typing import Annotated
from dotenv import load_dotenv
import os

load_dotenv()

# DATABASE INFOS
user = os.environ.get("DATABASE_USERNAME")
password = os.environ.get("DATABASE_PASSWORD")
database_name = os.environ.get("DATABASE_NAME")
database_host = os.environ.get("DATABASE_HOST")
database_port = os.environ.get("DATABASE_PORT")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{user}:{password}@{database_host}:{database_port}/{database_name}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# DATABASE INFOS
user = os.environ.get("DATABASE_USERNAME")
password = os.environ.get("DATABASE_PASSWORD")
database_name = os.environ.get("DATABASE_NAME")
database_host = os.environ.get("DATABASE_HOST")
database_port = os.environ.get("DATABASE_PORT")

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{database_host}:{database_port}/{database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
from ..database import Base
from sqlalchemy import Column, Integer, String


class Student(Base):
    """`Student` model class."""

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

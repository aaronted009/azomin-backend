from datetime import date
from sqlmodel import Field, Relationship
from .person import Person
from .course import Course


class Teacher(Person, table=True):
    id: int = Field(primary_key=True)
    hireDate: date | None = Field()
    qualification: str = Field(index=True)
    salary: float = Field()
    courses: list["Course"] = Relationship(back_populates="teacher")

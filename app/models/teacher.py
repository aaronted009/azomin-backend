from sqlmodel import Field, Date, Relationship
from .person import Person
from .course import Course


class Teacher(Person, table=True):
    id: int = Field(primary_key=True)
    hireDate: Date | None = Field()
    qualification: str = Field(index=True)
    salary: float = Field()
    courses: list["Course"] = Relationship(back_populates="teacher")
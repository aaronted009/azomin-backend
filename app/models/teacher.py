from .person import Person
from sqlmodel import Field, Date


class Teacher(Person, table=True):
    id: int = Field(primary_key=True)
    hireDate: Date | None = Field()
    qualification: str = Field(index=True)
    salary: float = Field()
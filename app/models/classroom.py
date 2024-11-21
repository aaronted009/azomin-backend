from sqlmodel import Field, SQLModel, Relationship
from .student import Student
from .fee import Fee


class ClassRoom(SQLModel, table=True):
    id: int = Field(primary_key=True)
    className: str = Field()
    numberOfStudents: int = Field()
    students: list["Student"] = Relationship(back_populates="classroom")
    fees: Fee = Relationship(back_populates="classroom")

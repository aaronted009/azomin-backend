from sqlmodel import Field, Relationship, SQLModel
from .teacher import Teacher


class Course(SQLModel, table=True):
    id: int = Field(primary_key=True)
    courseName: str = Field(index=True)
    description: str = Field(index=True)
    coefficient: int = Field()
    teacher_id: int = Field(foreign_key="teacher.id")
    teacher: Teacher = Relationship(back_populates="courses")

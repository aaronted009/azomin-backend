from sqlmodel import Field, SQLModel
from .teacher import Teacher


class Course(SQLModel, table=True):
    id: int = Field(primary_key=True)
    courseName: str = Field(index=True)
    description: str = Field(index=True)
    coefficient: int = Field()
    teacher_id: int | None = Field(default=None, foreign_key="teacher.id")

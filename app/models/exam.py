from datetime import date
from sqlmodel import Field, SQLModel, Relationship
from .exam_result import ExamResult
from typing import Optional


class Exam(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(index=True)
    examDate: date | None = Field()
    trimester: int = Field()
    classroom_id: int = Field(foreign_key="classroom.id")
    course_id: int = Field(foreign_key="course.id")
    exam_results: Optional[ExamResult] = Relationship(back_populates="exam")
from sqlmodel import Field, SQLModel, Relationship
from .exam import Exam
from .student import Student


class ExamResult(SQLModel, table=True):
    id: int = Field(primary_key=True)
    score: int = Field()
    exam_id: int = Field(foreign_key="exam.id")
    exam: Exam = Relationship(back_populates="exam_results")
    student_id: int = Field(foreign_key="student.id")
    student: Student = Relationship(back_populates="exam_results")

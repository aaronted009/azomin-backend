from sqlmodel import Field, Relationship
from .person import Person
from .classroom import ClassRoom
from .student_tutor import StudentTutor
from .exam_result import ExamResult


class Student(Person, table=True):
    id: int = Field(primary_key=True)
    classroom_id: int = Field(foreign_key="classroom.id")
    classroom: ClassRoom = Relationship(back_populates="students")
    student_tutors: list["StudentTutor"] = Relationship(back_populates="student")
    exam_results: list["ExamResult"] = Relationship(back_populates="student")

from sqlmodel import Field, Relationship
from .person import Person
from .classroom import ClassRoom
from .student_tutor import StudentTutor


class Student(Person, table=True):
    id: int = Field(primary_key=True)
    firstname: str = Field(index=True)
    lastname: str = Field(index=True)
    classroom_id: int = Field(foreign_key="classroom.id")
    classroom: ClassRoom = Relationship(back_populates="students")
    student_tutors: list["StudentTutor"] = Relationship(back_populates="student")

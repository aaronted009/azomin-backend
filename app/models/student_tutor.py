from .student import Student
from .person import Person
from sqlmodel import Field, Relationship

class StudentTutor(Person, table=True):
    id: int = Field(primary_key=True)
    student_id: int = Field(foreign_key="student.id")
    student: Student = Relationship(back_populates="student")
    
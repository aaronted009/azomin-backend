from datetime import date
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional


class Person(SQLModel):
    firstName: str = Field(index=True)
    lastName: str = Field(index=True)
    dateOfBirth: date | None = Field()
    gender: str = Field(index=True)
    address: str = Field()
    phoneNumber: str = Field()
    email: str = Field()


class Student(Person, table=True):
    id: int = Field(primary_key=True)
    classroom_id: int = Field(foreign_key="classroom.id")
    classroom: "ClassRoom" = Relationship(back_populates="students")
    student_tutors: list["StudentTutor"] = Relationship(back_populates="student")
    exam_results: list["ExamResult"] = Relationship(back_populates="student")


class StudentTutor(Person, table=True):
    id: int = Field(primary_key=True)
    student_id: int = Field(foreign_key="student.id")
    student: "Student" = Relationship(back_populates="student_tutors")


class Teacher(Person, table=True):
    id: int = Field(primary_key=True)
    hireDate: date | None = Field()
    qualification: str = Field(index=True)
    salary: Optional[float] = Field()
    courses: Optional[list["Course"]] = Relationship(back_populates="teacher")
    password: str = Field()


class ClassRoom(SQLModel, table=True):
    id: int = Field(primary_key=True)
    className: str = Field()
    numberOfStudents: Optional[int] = Field()
    students: list["Student"] = Relationship(back_populates="classroom")
    fees: "Fee" = Relationship(back_populates="classroom")


class Course(SQLModel, table=True):
    id: int = Field(primary_key=True)
    courseName: str = Field(index=True)
    description: str = Field(index=True)
    coefficient: int = Field()
    teacher_id: int = Field(foreign_key="teacher.id")
    teacher: "Teacher" = Relationship(back_populates="courses")


class Exam(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(index=True)
    examDate: date | None = Field()
    trimester: int = Field()
    classroom_id: int = Field(foreign_key="classroom.id")
    course_id: int = Field(foreign_key="course.id")
    exam_results: list["ExamResult"] = Relationship(back_populates="exam")


class ExamResult(SQLModel, table=True):
    id: int = Field(primary_key=True)
    score: int = Field()
    exam_id: int = Field(foreign_key="exam.id")
    exam: "Exam" = Relationship(back_populates="exam_results")
    student_id: int = Field(foreign_key="student.id")
    student: "Student" = Relationship(back_populates="exam_results")


class Fee(SQLModel, table=True):
    id: int = Field(primary_key=True)
    amount: float = Field()
    classroom_id: int = Field(foreign_key="classroom.id")
    classroom: "ClassRoom" = Relationship(back_populates="fees")

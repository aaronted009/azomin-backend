from sqlmodel import Field, SQLModel


class ExamResult(SQLModel, table=True):
    id: int = Field(primary_key=True)
    score: int = Field()
    exam_id: int = Field(foreign_key="exam.id")
    student_id: int = Field(foreign_key="student.id")
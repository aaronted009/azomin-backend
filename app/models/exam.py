from sqlmodel import Field, Date, SQLModel


class Exam(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(index=True)
    examDate: Date | None = Field()
    trimester: int = Field()
    classroom_id: int | None = Field(default=None, foreign_key="classroom.id")
    course_id: int | None = Field(default=None, foreign_key="course.id")
from sqlmodel import Field, SQLModel


class Student(SQLModel, table=True):
    id: int = Field(primary_key=True)
    firstname: str = Field(index=True)
    lastname: str = Field(index=True)

from sqlmodel import Field, SQLModel


class Subject(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    coefficient: int = Field()

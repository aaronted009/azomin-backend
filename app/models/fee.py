from sqlmodel import Field, SQLModel

class Fee(SQLModel, table=True):
    id: int = Field(primary_key=True)
    amount: float = Field()
    classroom_id: int | None = Field(default=None, foreign_key="classroom.id")
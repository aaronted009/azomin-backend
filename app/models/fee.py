from sqlmodel import Field, Relationship, SQLModel
from .classroom import ClassRoom

class Fee(SQLModel, table=True):
    id: int = Field(primary_key=True)
    amount: float = Field()
    classroom_id: int = Field(foreign_key="classroom.id")
    classroom: ClassRoom = Relationship(back_populates="fees")
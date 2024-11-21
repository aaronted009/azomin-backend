from datetime import date
from sqlmodel import Field, SQLModel


class Person(SQLModel):
    firstName: str = Field(index=True)
    lastName: str = Field(index=True)
    dateOfBirth: date | None = Field()
    gender: str = Field(index=True)
    address: str = Field()
    phoneNumber: str = Field()
    email: str = Field()

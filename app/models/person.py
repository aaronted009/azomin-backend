from sqlmodel import Field, SQLModel, Date

class Person(SQLModel):
    firstName: str = Field(index=True)
    lastName: str = Field(index=True)
    dateOfBirth: Date | None = Field()
    gender: str = Field(index=True)
    address: str = Field()
    phoneNumber: str = Field()
    email: str = Field()
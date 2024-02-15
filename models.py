from pydantic import BaseModel, Field, EmailStr


class CustomerCreateSchema(BaseModel):
    name: str = Field(min_length=5)
    age: int = Field(gt=16)
    email: EmailStr
    address: str
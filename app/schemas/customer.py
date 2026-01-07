from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    full_name: str
    email: EmailStr


class CustomerResponse(BaseModel):
    id: int
    business_id: int
    full_name: str
    email: EmailStr

    class Config:
        orm_mode = True

from pydantic import BaseModel


class BookingCreate(BaseModel):
    slot_id: int
    customer_id: int


class BookingResponse(BaseModel):
    id: int
    business_id: int
    slot_id: int
    customer_id: int
    status: str

    class Config:
        orm_mode = True

from datetime import datetime

from pydantic import BaseModel


class ScheduleSlotCreate(BaseModel):
    starts_at: datetime
    ends_at: datetime


class ScheduleSlotResponse(BaseModel):
    id: int
    business_id: int
    starts_at: datetime
    ends_at: datetime
    is_booked: bool

    class Config:
        orm_mode = True

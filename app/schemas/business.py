from pydantic import BaseModel


class BusinessCreate(BaseModel):
    name: str


class BusinessResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

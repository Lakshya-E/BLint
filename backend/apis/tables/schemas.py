from pydantic import BaseModel

class TableResponse(BaseModel):
    id: int
    number: int
    seats: int
    status: str

    class Config:
        orm_mode = True

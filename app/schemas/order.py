from pydantic import BaseModel
from typing import List

class OrderCreate(BaseModel):
    user_id: int

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: float

    class Config:
        from_attributes = True
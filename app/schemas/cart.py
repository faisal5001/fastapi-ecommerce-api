from pydantic import BaseModel

class CartCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int = 1

class CartResponse(CartCreate):
    id: int

    class Config:
        from_attributes = True
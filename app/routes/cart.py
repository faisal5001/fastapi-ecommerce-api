from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.cart import Cart
from app.schemas.cart import CartCreate

router = APIRouter(prefix="/cart")

# ➕ Add to cart
@router.post("/")
def add_to_cart(data: CartCreate, db: Session = Depends(get_db)):
    item = db.query(Cart).filter(
        Cart.user_id == data.user_id,
        Cart.product_id == data.product_id
    ).first()

    if item:
        item.quantity += data.quantity
    else:
        item = Cart(**data.dict())
        db.add(item)

    db.commit()
    return item

# 📥 Get user cart
@router.get("/{user_id}")
def get_cart(user_id: int, db: Session = Depends(get_db)):
    return db.query(Cart).filter(Cart.user_id == user_id).all()

# ❌ Remove item
@router.delete("/{cart_id}")
def remove_item(cart_id: int, db: Session = Depends(get_db)):
    item = db.query(Cart).get(cart_id)
    db.delete(item)
    db.commit()
    return {"msg": "Item removed"}
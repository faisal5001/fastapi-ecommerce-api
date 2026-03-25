from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.cart import Cart
from app.models.product import Product

router = APIRouter(prefix="/orders")

# 🛒 Create order from cart
@router.post("/")
def create_order(user_id: int, db: Session = Depends(get_db)):
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()

    if not cart_items:
        return {"error": "Cart is empty"}

    total_price = 0

    order = Order(user_id=user_id, total_price=0)
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in cart_items:
        product = db.query(Product).get(item.product_id)
        total_price += product.price * item.quantity

        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(order_item)

    order.total_price = total_price

    # 🧹 Clear cart
    for item in cart_items:
        db.delete(item)

    db.commit()

    return order

# 📥 Get user orders
@router.get("/{user_id}")
def get_orders(user_id: int, db: Session = Depends(get_db)):
    return db.query(Order).filter(Order.user_id == user_id).all()
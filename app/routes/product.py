from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate

router = APIRouter(prefix="/products")

@router.post("/")
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    product = Product(**data.dict())
    db.add(product)
    db.commit()
    return product

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
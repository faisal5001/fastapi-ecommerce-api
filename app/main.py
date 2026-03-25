from fastapi import FastAPI
from app.database import Base, engine

# Import all models (IMPORTANT for table creation)
from app.models import user, product, category, wishlist, cart, order, order_item

# Import routers
from app.routes import auth, product, category, wishlist, cart, order

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="FastAPI E-commerce API",
    description="A complete e-commerce backend built with FastAPI",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "E-commerce API is running 🚀"}

# Include all routers
app.include_router(auth.router, tags=["Auth"])
app.include_router(product.router, tags=["Products"])
app.include_router(category.router, tags=["Categories"])
app.include_router(wishlist.router, tags=["Wishlist"])
app.include_router(cart.router, tags=["Cart"])
app.include_router(order.router, tags=["Orders"])
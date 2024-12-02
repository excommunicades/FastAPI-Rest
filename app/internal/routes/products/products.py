from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends
from fastapi import Request

from app.pkg.db.database import get_db
from app.internal.routes.products.schemas import (
    ProductOut,
    ProductCreate,
)
from app.pkg.db.repositories import (
    ProductRepository
)

router = APIRouter(
    prefix='/api/v1'
)

@router.post(path="/posts", response_model=ProductOut)
def create_post(request: Request, product: ProductCreate, db: Session = Depends(get_db)):

    product_repository = ProductRepository(db=db)

    db_product = product_repository.create_product(
                                                title=product.title,
                                                description=product.description,
                                                )

    return db_product

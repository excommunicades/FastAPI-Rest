from typing import List, Optional
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse

from app.pkg.db.database import get_db
from app.internal.routes.products.schemas import (
    ProductOut,
    ProductCreate,
    ProductUpdate,
)
from app.pkg.db.repositories import (
    ProductRepository
)
from app.internal.routes.products.services import ProductService

router = APIRouter(
    prefix='/api/v1'
)

def get_product_service(db: Session = Depends(get_db)) -> ProductService:

    return ProductService(db)

@router.post("/posts", response_model=ProductOut)
def create_product(product: ProductCreate, product_service: ProductService = Depends(get_product_service)):

    '''Creates product'''

    try:

        db_product = product_service.create_product(title=product.title, description=product.description)

        return db_product

    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))

@router.get("/posts", response_model=List[ProductOut])
def get_product_list(product_service: ProductService = Depends(get_product_service)):

    '''Return product list'''

    db_product_list = product_service.get_product_list()

    if not db_product_list:

        raise HTTPException(status_code=404, detail="Products not found")

    return db_product_list

@router.get("/posts/{product_id}", response_model=ProductOut)
def get_product(product_id: int, product_service: ProductService = Depends(get_product_service)):

    '''Return product'''

    db_product = product_service.get_product(product_id)

    if not db_product:

        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")

    return db_product

@router.put("/posts/{product_id}", response_model=ProductOut)
def update_product(product_id: int, title: Optional[str] = None, description: Optional[str] = None, product_service: ProductService = Depends(get_product_service)):

    '''Update product'''

    if not title and not description:

        raise HTTPException(status_code=400, detail="Both fields, title and description, cannot be empty.")
    
    db_product = product_service.update_product(product_id, title, description)

    if not db_product:

        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
    
    return db_product

@router.delete("/posts/{product_id}", response_model=ProductOut)
def delete_product(product_id: int, product_service: ProductService = Depends(get_product_service)):

    '''Delete product'''

    db_product = product_service.delete_product(product_id)

    if not db_product:

        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")

    return db_product

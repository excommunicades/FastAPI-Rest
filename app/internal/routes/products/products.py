from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse

from app.pkg.db.database import get_db
from app.internal.routes.products.schemas import (
    ProductOut,
    ProductGet,
    ProductCreate,
)
from app.pkg.db.repositories import (
    ProductRepository
)

router = APIRouter(
    prefix='/api/v1'
)

@router.post(path="/posts", response_model=ProductOut)
def create_product(request: Request, product: ProductCreate, db: Session = Depends(get_db)):

    '''Creates product'''

    product_repository = ProductRepository(db=db)

    db_product = product_repository.create_product(
                                                title=product.title,
                                                description=product.description,
                                                )

    return db_product


@router.get(path='/posts', response_model=list[ProductOut])
def get_product(db: Session = Depends(get_db)):

    '''Returns one product by id'''

    product_repository = ProductRepository(db=db)

    db_product_list = product_repository.get_product_list()
    print(db_product_list)
    if not db_product_list:

        return JSONResponse(
            status_code=404,
            content={
                "code": 404,
                "error": "Products not found",
            }
        )

    return [ProductOut.from_orm(product) for product in db_product_list]


@router.get(path='/posts/{product_id}', response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):

    '''Returns one product by id'''

    product_repository = ProductRepository(db=db)

    db_product = product_repository.get_product(product_id=product_id)

    if not db_product:

        return JSONResponse(
            status_code=404,
            content={
                "code": 404,
                "error": f"Product with ID {product_id} not found.",
                "product_id": product_id
            }
        )

    return db_product


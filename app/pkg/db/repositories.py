from sqlalchemy.orm import Session
from app.pkg.db.models import (
    Products,
)


class ProductRepository:

    def __init__(self, db: Session):

        self.db = db

    def create_product(self, title: str, description: str) -> Products:

        db_product = Products(title=title, description=description)

        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)

        return db_product

    def get_product(self, product_id: int) -> Products:

        return self.db.query(Products).filter(Products.id == product_id).first()


    def get_product_list(self) -> list[Products]:

        return self.db.query(Products).all()

    def update_product(self, product_id: int, title: str = None, description: str = None) -> Products:

        db_product = self.db.query(Products).filter(Products.id == product_id).first()

        if db_product:

            if title:

                db_product.title = title

            if description:

                db_product.description = description

            self.db.commit()

            self.db.refresh(db_product)

            return db_product

        return None

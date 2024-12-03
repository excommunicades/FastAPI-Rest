from sqlalchemy.orm import Session
from app.pkg.db.models import Products
from pydantic import ValidationError
from typing import Optional

class ProductService:

    def __init__(self, db: Session):
        self.db = db

    def create_product(self, title: str, description: str) -> Products:
        if not title or not description:
            raise ValueError("Title and description cannot be empty.")

        db_product = Products(title=title, description=description)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_product(self, product_id: int) -> Optional[Products]:
        return self.db.query(Products).filter(Products.id == product_id).first()

    def get_product_list(self) -> list[Products]:
        return self.db.query(Products).all()

    def update_product(self, product_id: int, title: Optional[str], description: Optional[str]) -> Optional[Products]:
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

    def delete_product(self, product_id: int) -> Optional[Products]:
        db_product = self.db.query(Products).filter(Products.id == product_id).first()

        if db_product:
            self.db.delete(db_product)
            self.db.commit()
            return db_product
        
        return None
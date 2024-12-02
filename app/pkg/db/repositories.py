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

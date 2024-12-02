from sqlalchemy import Column, Integer, String

from app.pkg.db.database import Base


class Products(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, index=True)

    description = Column(String, index=True)

from pydantic import BaseModel


class ProductOut(BaseModel):

    title: str

    description: str

    class Config:

        orm_mode = True

class ProductCreate(BaseModel):

    title: str

    description: str

    class Config:

        orm_mode = True

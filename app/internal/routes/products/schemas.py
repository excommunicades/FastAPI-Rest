from pydantic import BaseModel


class ProductOut(BaseModel):

    '''Schema for endpoint data output'''

    id: int

    title: str

    description: str

    class Config:

        orm_mode = True
        from_attributes = True

class ProductCreate(BaseModel):

    '''Schema for product create data input'''

    title: str

    description: str

    class Config:

        orm_mode = True


class ProductUpdate(BaseModel):

    '''Schema for product update data input'''

    id: int

    title: str

    description: str

    class Config:

        orm_mode = True

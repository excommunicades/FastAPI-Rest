from pydantic import BaseModel


class ProductOut(BaseModel):

    '''Information which endpoint will return'''

    id: int

    title: str

    description: str

    class Config:

        orm_mode = True
        from_attributes = True

class ProductCreate(BaseModel):

    '''Product data which endpoint will take from request'''

    title: str

    description: str

    class Config:

        orm_mode = True


class ProductUpdate(BaseModel):

    '''Updates Product'''

    id: int

    title: str

    description: str

    class Config:

        orm_mode = True
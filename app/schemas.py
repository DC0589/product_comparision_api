from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float
    retailer: str


class ProductCreate(ProductBase):
    pass


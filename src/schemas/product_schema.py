from typing import Optional

from pydantic import BaseModel


class list_product_schema(BaseModel):
    pass


class add_product_schema(BaseModel):
    productId: Optional[str] = None
    image: str
    name: str
    description: Optional[str]
    price: int
    ram: Optional[int]
    storage: Optional[int]
    operatingSystem: Optional[str]


class delete_product_schema(BaseModel):
    productId: str

from sqlmodel import SQLModel
from .good import Good
from .actor import Actor
from .base_table import BaseTable


class ProductBase(SQLModel):
    good: Good
    owner: Actor
    quantity: int = 0
    price: float


class Product(ProductBase, BaseTable, table=True):
    pass

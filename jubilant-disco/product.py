from sqlmodel import Field, Relationship, SQLModel
from .good import Good
from .actor import Actor
from .base_table import BaseTable


class ProductBase(SQLModel):
    good_id: int = Field(default=None, foreign_key="good.id")
    good: Good = Relationship(back_populates="good")

    owner_id: int = Field(default=None, foreign_key="owner.id")
    owner: Actor = Relationship(back_populates="product")
    quantity: int = 0
    price: float


class Product(ProductBase, BaseTable, table=True):
    pass

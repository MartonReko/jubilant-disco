from sqlmodel import Field, Relationship, SQLModel
from jubilant_disco.good import Good
from jubilant_disco.actor import Actor
from jubilant_disco.base_table import BaseTable


class ProductBase(SQLModel):
    good_id: int | None = Field(default=None, foreign_key="good.id")
    good: Good = Relationship(back_populates="good")

    owner_id: int | None = Field(default=None, foreign_key="owner.id")
    owner: Actor = Relationship(back_populates="product")
    quantity: int = 0
    price: float


class Product(ProductBase, BaseTable, table=True):
    pass

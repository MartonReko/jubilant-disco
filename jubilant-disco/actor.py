from sqlmodel import Relationship, SQLModel
from .product import ProductBase
from base_table import BaseTable


class ActorBase(SQLModel):
    money: int = 0
    products: list[ProductBase] = Relationship(back_populates="product")


class Actor(ActorBase, BaseTable, table=True):
    pass

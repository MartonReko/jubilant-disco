from sqlmodel import Field, Relationship, SQLModel
#from .good import Good
#from .actor import Actor
#from .base_table import BaseTable

from jubilantdisco import good
from jubilantdisco import base_table




class ProductBase(SQLModel):
    good_id: int | None = Field(default=None, foreign_key="good.id")
    mygood: good.Good = Relationship(back_populates="good")

    owner_id: int | None = Field(default=None, foreign_key="owner.id")
    owner: Actor = Relationship(back_populates="product")
    quantity: int = 0
    price: float

class Product(ProductBase, base_table.BaseTable, table=True):
    pass

class ActorBase(SQLModel):
    money: int = 0
    products: list[ProductBase] = Relationship(back_populates="owner")

class Actor(ActorBase, base_table.BaseTable, table=True):
    pass


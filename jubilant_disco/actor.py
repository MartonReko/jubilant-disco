from sqlmodel import Relationship, SQLModel
from jubilant_disco.product import ProductBase
from jubilant_disco.base_table import BaseTable

class ActorBase(SQLModel):
    money: int = 0
    products: list[ProductBase] = Relationship(back_populates="owner")


class Actor(ActorBase, BaseTable, table=True):
    pass

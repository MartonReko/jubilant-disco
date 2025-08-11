from sqlmodel import Relationship, SQLModel
from .good import GoodBase
from .base_table import BaseTable


class RecipeBase(SQLModel):
    input: dict[GoodBase, int] = Relationship(back_populates="good")
    output: dict[GoodBase, int] = Relationship(back_populates="good")


class Recipe(RecipeBase, BaseTable, table=True):
    pass

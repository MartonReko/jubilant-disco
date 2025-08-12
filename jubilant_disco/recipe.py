from sqlmodel import Relationship, SQLModel
from jubilant_disco.good import GoodBase
from jubilant_disco.base_table import BaseTable


class RecipeBase(SQLModel):
    input: dict[GoodBase, int] = Relationship(back_populates="good")
    output: dict[GoodBase, int] = Relationship(back_populates="good")


class Recipe(RecipeBase, BaseTable, table=True):
    pass

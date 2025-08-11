from sqlmodel import SQLModel
from .good import GoodBase
from .base_table import BaseTable


class RecipeBase(SQLModel):
    input: dict[GoodBase, int]
    output: dict[GoodBase, int]


class Recipe(RecipeBase, BaseTable, table=True):
    pass

from sqlmodel import SQLModel
from .good import GoodBase
from .base_table import BaseTable

class RecipeBase(SQLModel):
    input: list[GoodBase]
    output: GoodBase
    
class Recipe(RecipeBase, BaseTable, table=True):
    pass

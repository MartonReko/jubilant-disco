from .base_table import BaseTable
from sqlmodel import SQLModel

class GoodBase(SQLModel):
    name: str

class Good(GoodBase, BaseTable, table=True):
    pass
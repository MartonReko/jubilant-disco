from sqlmodel import SQLModel
from jubilant_disco.base_table import BaseTable

class GoodBase(SQLModel):
    name: str


class Good(GoodBase, BaseTable, table=True):
    pass

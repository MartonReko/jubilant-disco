from sqlmodel import Field, Relationship, SQLModel
from jubilant_disco.workplace import WorkplaceBase
from jubilant_disco.base_table import BaseTable


class OccupationBase(SQLModel):
    wage: int
    hours: int
    
    workplace_id: int | None = Field(default=None, foreign_key="workplace.id")
    workplace: WorkplaceBase = Relationship()


class Occupation(OccupationBase, BaseTable, table=True):
    pass

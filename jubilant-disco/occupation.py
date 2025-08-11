from sqlmodel import SQLModel
from .workplace import WorkplaceBase
from .base_table import BaseTable

class OccupationBase(SQLModel):
    wage: int
    hours: int
    workplace: WorkplaceBase
    
class Occupation(OccupationBase, BaseTable, table=True):
    pass
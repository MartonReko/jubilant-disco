from .actor import ActorBase
from .recipe import RecipeBase
from .base_table import BaseTable

class WorkplaceBase(ActorBase):
    maxWorkers: int = 0
    recipe: RecipeBase

class WorkPlace(WorkplaceBase, BaseTable, table=True):
    pass
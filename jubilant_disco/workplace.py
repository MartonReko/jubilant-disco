from sqlmodel import Field, Relationship
from jubilant_disco.actor import ActorBase
from jubilant_disco.recipe import RecipeBase
from jubilant_disco.base_table import BaseTable

class WorkplaceBase(ActorBase):
    maxWorkers: int = 0
      
    recipe_id: int | None = Field(default=None, foreign_key="recipe.id")
    recipe: RecipeBase = Relationship(back_populates="recipe")

class WorkPlace(WorkplaceBase, BaseTable, table=True):
    pass
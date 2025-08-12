from __future__ import annotations
from sqlmodel import Field, Relationship, SQLModel


class BaseTable(SQLModel):
    id: int | None = Field(default=None, primary_key=True)


class ActorBase(SQLModel):
    money: int = 0
    products: list[ProductBase] = Relationship(back_populates="actor")


class Actor(ActorBase, BaseTable, table=True):
    pass


class GoodBase(SQLModel):
    name: str


class Good(GoodBase, BaseTable, table=True):
    pass


class OccupationBase(SQLModel):
    wage: int
    hours: int
    
    workplace_id: int | None = Field(default=None, foreign_key="workplace.id")
    workplace: WorkplaceBase = Relationship(back_populates="workplace")


class Occupation(OccupationBase, BaseTable, table=True):
    pass


class PersonBase(ActorBase):
    name: str
    birthYear: int
    happiness: int = 0
    hunger: int = 0
    occupations: list[Occupation] = Relationship(back_populates="occupation")


class Person(PersonBase, BaseTable, table=True):
    pass

class PersonCreate(PersonBase):
    pass

class WorkplaceBase(ActorBase):
    maxWorkers: int = 0
      
    recipe_id: int | None = Field(default=None, foreign_key="recipe.id")
    recipe: RecipeBase = Relationship(back_populates="recipe")

class WorkPlace(WorkplaceBase, BaseTable, table=True):
    pass

class ProductBase(SQLModel):
    good_id: int | None = Field(default=None, foreign_key="good.id")
    good: Good = Relationship(back_populates="good")

    actor_id: int | None = Field(default=None, foreign_key="actor.id")
    actor: Actor = Relationship(back_populates="products")
    quantity: int = 0
    price: float


class Product(ProductBase, BaseTable, table=True):
    pass


class RecipeBase(SQLModel):
    input: dict[GoodBase, int] = Relationship(back_populates="good")
    output: dict[GoodBase, int] = Relationship(back_populates="good")


class Recipe(RecipeBase, BaseTable, table=True):
    pass

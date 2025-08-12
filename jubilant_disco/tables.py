from __future__ import annotations
from sqlmodel import Field, Relationship, SQLModel


class ActorBase(SQLModel):
    money: int = 0


class Actor(ActorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    products: list["Product"] = Relationship(back_populates="actor")


class GoodBase(SQLModel):
    name: str


class Good(GoodBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class OccupationBase(SQLModel):
    wage: int
    hours: int
    workplace_id: int | None = Field(default=None, foreign_key="workplace.id")
    person_id: int | None = Field(default=None, foreign_key="person.id")


class Occupation(OccupationBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    workplace: WorkPlace = Relationship(back_populates="occupations")
    person: Person = Relationship(back_populates="occupations")


class PersonBase(ActorBase):
    name: str
    birthYear: int
    happiness: int = 0
    hunger: int = 0


class Person(PersonBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    occupations: list["Occupation"] | None = Relationship(back_populates="occupation")


class PersonCreate(PersonBase):
    pass


class WorkplaceBase(ActorBase):
    maxWorkers: int = 0
    recipe_id: int | None = Field(default=None, foreign_key="recipe.id")


class WorkPlace(WorkplaceBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    recipe: Recipe = Relationship(back_populates="recipe")
    occupations: list["Occupation"] | None = Relationship(back_populates="occupation")


class ProductBase(SQLModel):
    good_id: int | None = Field(default=None, foreign_key="good.id")
    actor_id: int | None = Field(default=None, foreign_key="actor.id")
    quantity: int = 0
    price: float


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    good: Good = Relationship(back_populates="good")
    actor: Actor = Relationship(back_populates="products")


class RecipeBase(SQLModel):
    input: dict[Good, int] | None = Relationship(back_populates="good")
    output: dict[Good, int] | None = Relationship(back_populates="good")


class Recipe(RecipeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
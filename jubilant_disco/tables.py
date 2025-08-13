from __future__ import annotations
from sqlmodel import Field, Relationship, SQLModel


class ActorBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    money: int = 0


class Actor(ActorBase):
    products: list["Product"] | None = Relationship(back_populates="actor")


class GoodBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class Good(GoodBase, table=True):
    products: list["Product"] | None = Relationship(back_populates="good")
    recipe_items: list["RecipeItem"] | None = Relationship(back_populates="good")


class RecipeItemBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    good_id: int = Field(default=None, foreign_key="good.id")
    recipe_id: int = Field(default=None, foreign_key="recipe.id")
    quantity: int = 1
    is_output: bool


class RecipeItem(RecipeItemBase, table=True):
    good: Good = Relationship(back_populates="recipe_items")
    recipe: Recipe = Relationship(back_populates="recipe_items")


class RecipeBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class Recipe(RecipeBase, table=True):
    recipe_items: list["RecipeItem"] | None = Relationship(back_populates="recipe")
    workplaces: list["Workplace"] | None = Relationship(back_populates="recipe")


class OccupationBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    workplace_id: int | None = Field(default=None, foreign_key="workplace.id")
    person_id: int | None = Field(default=None, foreign_key="person.id")
    wage: int
    hours: int


class Occupation(OccupationBase, table=True):
    workplace: Workplace = Relationship(back_populates="occupations")
    person: Person = Relationship(back_populates="occupations")


class PersonBase(ActorBase):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    birthYear: int
    happiness: int = 0
    hunger: int = 0


class Person(PersonBase, table=True):
    occupations: list["Occupation"] | None = Relationship(back_populates="person")


class PersonCreate(PersonBase):
    pass


class WorkplaceBase(ActorBase):
    id: int | None = Field(default=None, primary_key=True)
    recipe_id: int | None = Field(default=None, foreign_key="recipe.id")
    maxWorkers: int = 0


class Workplace(WorkplaceBase, table=True):
    recipe: Recipe = Relationship(back_populates="workplaces")
    occupations: list["Occupation"] | None = Relationship(back_populates="workplace")


class ProductBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    good_id: int | None = Field(default=None, foreign_key="good.id")
    actor_id: int | None = Field(default=None, foreign_key="actor.id")
    quantity: int = 0
    price: float | None


class Product(ProductBase, table=True):
    good: Good = Relationship(back_populates="products")
    actor: Actor = Relationship(back_populates="products")

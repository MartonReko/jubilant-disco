from enum import Enum

from sqlmodel import SQLModel, Field


class ActorBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    money: int = 0


class GoodBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class RecipeItemBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    good_id: int = Field(default=None, foreign_key="good.id")
    recipe_id: int = Field(default=None, foreign_key="recipe.id")
    quantity: int = 1

    class Type(Enum):
        INPUT = "INPUT"
        OUTPUT = "OUTPUT"

    type: Type = Type.INPUT


class RecipeBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class OccupationBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    workplace_id: int | None = Field(default=None, foreign_key="workplace.id")
    person_id: int | None = Field(default=None, foreign_key="person.id")
    wage: int = 0
    hours: int = 8


class PersonBase(ActorBase):
    id: int | None = Field(default=None, primary_key=True)
    name: str = str(id)
    birthYear: int = 0
    happiness: int = 0
    hunger: int = 0


class WorkplaceBase(ActorBase):
    id: int | None = Field(default=None, primary_key=True)
    recipe_id: int | None = Field(default=None, foreign_key="recipe.id")
    name: str
    maxWorkers: int = 0


class ProductBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    good_id: int | None = Field(default=None, foreign_key="good.id")
    actor_id: int | None = Field(default=None, foreign_key="actor.id")
    quantity: int = 0
    price: float | None

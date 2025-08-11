from .actor import ActorBase
from .occupation import Occupation
from .base_table import BaseTable


class PersonBase(ActorBase):
    name: str
    birthYear: int
    happiness: int = 0
    hunger: int = 0
    occupations: list[Occupation] = []


class Person(PersonBase, BaseTable, table=True):
    pass

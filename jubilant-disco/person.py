from .actor import Actor
from .occupation import Occupation

class Person(Actor):
    name: str
    birthYear: int = 1838
    happiness: int = 0
    hunger: int = 0
    occupations: list[Occupation] = []

    def __init__(self) -> None:
        Actor.__init__(self)
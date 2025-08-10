from .actor import Actor
from .occupation import Occupation

class Person(Actor):
    name: str
    birthYear: int
    happiness: int
    hunger: int
    occupations: list[Occupation]

    def __init__(self):
        Actor.__init__(self)
        self.name = "Empty"
        self.birthYear = -1
        self.happiness = -1
        self.hunger = -1
        self.occupations = []

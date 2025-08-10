from .actor import Actor
from .recipe import Recipe

class Workplace(Actor):
    maxWorkers: int = 0
    recipe: Recipe

    def __init__(self) -> None:
        Actor.__init__(self) 
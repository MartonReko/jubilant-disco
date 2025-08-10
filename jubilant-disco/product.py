from .person import Person
from .good import Good

class Product:
    good: Good
    quantity: int
    price: float
    owner: Person

    def __init__(self, p: Person, g: Good):
        self.quantity = 0
        self.price = 0.0
        self.owner = p
        self.Good = g

        # TODO fix by Petya-G

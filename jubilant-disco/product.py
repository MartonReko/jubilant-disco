from .person import Person
from .good import Good

class Product:
    good: Good
    owner: Person
    quantity: int = 0
    price: float

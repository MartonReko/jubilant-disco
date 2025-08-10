from .product import Product

class Actor:
    money: int
    products : list[Product]

    def __init__(self):
        self.money = 0
        self.products = []

    def Buy(self, Product):
        # TODO
        pass

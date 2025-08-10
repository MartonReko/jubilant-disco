class Good:
    name: str
    madeOf: dict[self.Good, int]

    def __init__(self, n: str):
        self.name = n
        

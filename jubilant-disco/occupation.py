from .workplace import Workplace

class Occupation:
    wage: int
    hoursPerWeek: int
    worksAt: Workplace

    def __init__(self):
        self.wage = -1
        self.hoursPerWeek = -1
        self.worksAt = Workplace()


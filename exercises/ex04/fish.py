"""File to define Fish class."""


class Fish:

    age: int

    def __init__(self):
        """Creates initial values for Fish"""
        self.age = 0
        return None

    def one_day(self):
        """Increase fish age one everyday."""
        self.age += 1
        return None

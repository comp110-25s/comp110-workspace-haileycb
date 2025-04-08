"""File to define Bear class."""

__author__ = "730562399"


class Bear:

    age: int
    hunger_score: int

    def __init__(self):
        """Creates initial values for bear class"""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Adds age and subtrats hunger from bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Adds number of fish to bear's hunger score."""
        self.hunger_score += num_fish
        return None

"""File to define River class."""

__author__ = "730562399"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes animals from old age from River."""
        alive_bears: list[Bear] = []
        alive_fish: list[Fish] = []
        for a_bear in self.bears:
            if a_bear.age <= 5:
                alive_bears.append(a_bear)
        for a_fish in self.fish:
            if a_fish.age <= 3:
                alive_fish.append(a_fish)
        self.bears = alive_bears
        self.fish = alive_fish
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes specified number of fish from front of list."""
        for x in range(0, amount):
            self.fish.pop(x)

    def bears_eating(self):
        """Portrays bears eating in simulation when there are enough fish."""
        for a_bear in self.bears:
            if len(self.fish) >= 5:
                a_bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Remove starving bears from river."""
        alive_bears: list[Bear] = []
        for a_bear in self.bears:
            if a_bear.hunger_score >= 0:
                alive_bears.append(a_bear)
        self.bears = alive_bears
        return None

    def repopulate_fish(self):
        """Simulate fish reproduction."""
        new_fish: int = (len(self.fish) // 2) * 4
        for x in range(0, new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Simulate bear reproduction."""
        bear_pair: int = len(self.bears) // 2
        for x in range(0, bear_pair):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Print status of River"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate a week in the river."""
        for x in range(0, 7):
            self.one_river_day()
        return None

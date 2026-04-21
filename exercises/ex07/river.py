"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730640030"


class River:
    """For the class River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

        # these for loops populate the river (Lists) with the number of respective bears and fish.

    def __str__(self) -> str:
        """Modifies the string method, allowing us to view the status of the river in terms of the FIsh and Bear population."""
        return (
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

    def check_ages(self):
        """Checks if fish/bears in list are 3/5 or younger, respectively, then creates a new list to add them to."""
        self.fish = [young_fish for young_fish in self.fish if young_fish.age <= 3]
        self.bears = [young_bears for young_bears in self.bears if young_bears.age <= 5]
        return None

    # x for x in self.x if x.age <= int: x represents the new list creation
    # for x in self.x goes through the object x.
    # new list replaces the old list!
    # x at the beginning is where x in self.x goes (new list) if <= number.

    def remove_fish(self, amount: int):
        """Removes amount many fish from the list in a frontmost order."""
        for x in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)
        return None

    def bears_eating(self):
        """For each bear, if there are at least 5 fish, the bear will eat 3."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(num_fish=3)
                self.remove_fish(amount=3)
        return None

    # Bear.eat instead of Bear(eat) which would create an entirely new object.
    # Do not manually pass self when calling methods.
    # by having a for loop, we can iterate through all bears, as opposed to just once.
    # bear.eat refers to the specific instance (object) of bear. If you wrote Bear.eat, it would refer to the whole class.

    def check_hunger(self):
        """Removes a bear if their hunger is below zero."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None

    # for bear in self.bears goes through every instance in list bears.
    # bear for creates a new list if bear.hunger_score >= 0.
    # when using self. in these functions, it refers to River, not Bear or Fish.

    def repopulate_fish(self):
        """For each pair of fish, 4 offspring will be produced."""
        n: int = len(self.fish) // 2
        for x in range(n):
            for x in range(4):
                self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """For each pair of bears, 1 offspring will be reproduced."""
        n: int = len(self.bears) // 2
        for x in range(n):
            self.bears.append(Bear())
        return None

    # // divides and rounds down to the nearest integer. 5 // 2 = 2.5 = 2.

    def __add__(self, r: River) -> River:
        """Combines two River objects to create a larger River."""
        total_bears: int = len(self.bears) + len(r.bears)
        total_fish: int = len(self.fish) + len(r.fish)
        return River(total_fish, total_bears)

    # we count total bears and fish, implement these sums in the creation of a new river.

    def __mul__(self, factor: int) -> River:
        """Returns a River object with a factor times as many fish and a factor times as many Bears as the input river."""
        total_bears: int = factor * len(self.bears)
        total_fish: int = factor * len(self.fish)
        return River(total_fish, total_bears)

    def one_river_day(self):
        """Simulate one day of life in the river."""
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
        print(self)

    def one_river_week(self) -> None:
        """Calls self.one_river_day seven times."""
        for x in range(7):
            self.one_river_day()

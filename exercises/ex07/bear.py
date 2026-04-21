"""File to define Bear class."""

__author__ = "730640030"


class Bear:
    """For the class bear in the river"""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes the bear attributes to zero"""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    # self represents the specific instance we are working with; stores age inside object under the name age

    def one_day(self):
        """Adjusts age and hunger_score after each day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Updates the Bear's hunger score so it increases by num_fish"""
        self.hunger_score += num_fish
        return None

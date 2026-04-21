"""File to define Fish class."""

__author__ = "730640030"


class Fish:
    """for the class Fish in the river."""

    age: int

    def __init__(self):
        """Initializes the fish attribute to zero."""  # by the only argument being self, every fish starts with an age 0; user does not decide age value.
        self.age: int = 0
        return None

    def one_day(self):
        """Adjusts age after each day."""
        self.age += 1
        return None


# key concept: classes define what objects would be. When an object is called, it refers to the class. Self refers to the specific object.

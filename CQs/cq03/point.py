"""Challenge Question 3: Class"""

from __future__ import annotations

__author__ = "730640030"

"""Define a new class named point"""


class Point:
    x: float
    y: float

    """init constructor assigns inputs x_init and y_init to the intiial vlaues of the attributes x and y."""

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    """Mutates the Point by a given factor"""

    def scale_by(self, factor: int) -> None:
        self.x = self.x * factor
        self.y = self.y * factor

    """Returns a new point that has been mutated by scale_by"""

    def scale(self, factor: int) -> Point:
        new_point = Point(self.x, self.y)
        new_point.scale_by(factor)
        return new_point

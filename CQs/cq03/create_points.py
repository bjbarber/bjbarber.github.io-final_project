"""Check point.py to ensure code functions as expected."""

__author__ = "730640030"

from CQs.cq03.point import Point

"""Defines the first point: new_point1"""
new_point1 = Point(2, 5)
print(new_point1.x, new_point1.y)

"""point is mutated by a factor of 3"""
new_point2 = new_point1.scale(3)
print(new_point2.x, new_point2.y)

"""Checks that new_point1 is unchanged"""
print(new_point1.x, new_point1.y)

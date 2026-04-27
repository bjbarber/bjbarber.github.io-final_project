"""Mutating functions."""

__author__ = "730640030"


def manual_append(a: list[int], num: int) -> None:
    """Adds another integer to the list."""
    a.append(num)


def double(a: list[int]) -> None:
    """Doubles each item in list a."""
    i: int = 0
    while i < len(a):
        a[i] = a[i] * 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

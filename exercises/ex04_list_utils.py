"""Super fun lists!"""

__author__ = "730640030"


def all(a: list[int], num: int) -> bool:
    """Tells us if a list contains all of the same integers as the parameter num."""
    if len(a) == 0:
        return False
    i: int = 0
    while len(a) > i:
        if a[i] != num:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest value in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    x: int = input[0]
    while len(input) > i:
        if input[i] > x:
            x = input[i]
            i += 1
        else:
            i += 1
    return x


"""I worked out the logic for finding the largest number, by comparing each number to the largst down the list. However, I forgot variable "x" was just an integer and I was trying to index it so it wouldn't work. I figured this out and the code worked. """


def is_equal(a: list[int], b: list[int]) -> bool:
    """Tells us whether two lists are equal or not."""
    if len(a) != len(b):
        return False
    i: int = 0
    while i < len(a):
        if a[i] == b[i]:
            i += 1
        else:
            return False
    return True


"""I initially made this code more complicated than it needed to be by having two index variables and a count variable. I realized the simple logic is that if the lists don't equal the same length or indexes of lists do not equal, it simply evaluates to false. If not, it returns true."""


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Adds integers of one list to the end of another."""
    i: int = 0
    while len(list_2) > i:
        list_1.append(list_2[i])
        i += 1

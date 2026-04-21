""" "Exercise 8 Recursive Functions."""

from __future__ import annotations

__author__ = "730640030"


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializes attributes to self."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Magic method for string creation."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Given the inputs, returns the value of the node at a particular index. If Index does not exist, raises an Index error."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


"""I didn't realize the code was supposed to be outside of the object, which is why I was unable to call it in the first place."""
# index == 0 is the base case.
# head is None is the edge case.
# return value_at(head.next, index-1) is the recursive call.
# the recursive call moves the code fowards, while subtracting the index by one, ultimately ending at index == 0.


def max(head: Node | None) -> int:
    """Returns the maximum value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    max_value: int = max(head.next)
    if head.value > max_value:
        return head.value
    else:
        return max_value


"""This code was difficult to make as well. While other recurisions work their way through the start of a list, this recursion goes from the start to the end back to the start of the linked list. Once I was able to grasp that concept, I could do the rest."""
# ValueError checks if head.next is None. However, if head = Node(30,None) that is valid.
# It goes to the end of a linked list (none) and works its way backward.
# If head.next is greater than the head.value, it returns max_value, if not it returns head.value, and makes its way back to the start.


def linkify(items: list[int]) -> Node | None:
    """Returns a linked list when given a list."""
    if items == []:
        return None
    return Node(items[0], linkify(items[1:]))


"""I also struggle to make this code. Although it is relatively short, it still is compelex and understanding how the subscription notation worked was key to this whole thing."""
# 1: means everything except the first element. 1:3 means indexes 1-2 and stop at 3. :3 means start from 0 to 3 but don't include 3.
# items == [] is the base case. Node creation is the recursive case.
# items[:1] creates a new list and removes the first element from the previous list. That way, items[0] refers to the first index on the new list.


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list of Nodes which represent the original list scaled by factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))


"""Easiest code to make so far because I did the previous one, which allowed me to edit the Nodes in a similar manner while still understanding recursion."""
# if head is none is the base case. Node() is the recursion case.
# Node() multiplies head.value by factor and calls on scale to do the same to the next object in the linked list.

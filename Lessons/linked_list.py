"""Practicing linked lists."""

from __future__ import annotations


class Node:

    values: int
    next: Node | None
    # '|' tells us that the variable next can hold a Node object or none.

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def sum(head: Node | None) -> int:
        if head is None:
            return 0
        else:
            return head.value + sum(head.next)

    # head can be a Node or None
    # head represents the first node in the list

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"

    node_c: Node = Node(4, None)
    node_b: Node = Node(0, node_c)
    # Node(4, None) means value = 4 and next = none
    # Node(0, node_c) tells us value = 0 and next = node_c

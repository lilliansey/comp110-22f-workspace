"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730463283"


class Node:
    """An item in a single-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data:int, next: Optional[Node]):
        """Construct a sinly linked list. Use second node for arguement if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of a linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
    

def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)
    

def last(head: Optional[Node]) -> int:
    """Returns that last value of a Linked List, or raises a ValueError if the lsit is empty."""
    if head is None:
        raise ValueError("Last cannot be called with None.")
    else:
        if head.next is None:
            return last(head)


def value_at(head: Optional[Node], index: int) -> int:
    if index <=0 or index > len(head):
        raise IndexError("Index is out of bounds on the list.")
    else:
        if len(head) is index:
            return value_at(head.data)


def max(head: Optional[Node]) -> int:
    max_i: int = head
    if head is None:
        raise ValueError("Max cannot be called with None.")
    else:
        if head.next > max_i:
            max_i = head.next


def linkify(items: list[int]) -> Optional[Node]:
    """Given a list linkify will rerturn a Linked List of Nodes with the same values, in the same order, as the input list."""


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    return None
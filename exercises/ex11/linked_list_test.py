"""Tests for linked list utils."""

import pytest 
from exercises.ex11.linked_list import Node, last

__author__ = "730463283"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Index error should be raised if index is out of bounds."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list, 0) == IndexError


def test_value_at_non_empty() -> None:
    """Value at should return the value at a given index."""


def test_max_empty() -> None:
    """If the linked list is empty a ValueError should be raised."""


def test_max_non_empty() -> None:
    """Max should return the highest number in the linked list."""


def test_linkify_empty() -> None:
    """Edge case for linkify."""


def test_linkify_non_empty() -> None:
    """Linkify should turn a list into a linked list."""


def test_scale_empty() -> None:
    """Edge case for scale."""


def test_scale_non_empty() -> None:
    """Values should be scaled by the provided parameter."""
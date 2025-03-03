"""This is where I willl be testing my functions."""

__author__ = "730463283"

from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Edge case for only_evens."""
    xs: list[float] = []
    assert only_evens(xs) == []


def test_only_evens_many() -> None:
    """Use case 1 for only_evens."""
    xs: list[float] = [1.0, 2.0, 3.0]
    assert only_evens(xs) == [2.0]


def test_only_evens_many_again() -> None:
    """Use case 2 for only_evens."""
    xs: list[float] = [2.0, 7.0, 4.0]
    assert only_evens(xs) == [2.0, 4.0]


def test_concat_empty() -> None:
    """Edge case for concat."""
    xs: list[float] = []
    sx: list[float] = []
    assert concat(xs, sx) == []


def test_concat_many() -> None:
    """Use case 1 for concat."""
    xs: list[float] = [1.0, 2.0, 3.0]
    sx: list[float] = [1.0, 2.0, 3.0]
    assert concat(xs, sx) == [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]


def test_concat_many_again() -> None:
    """Use case 2 for concat."""
    xs: list[float] = [3.0, 4.0]
    sx: list[float] = [7.0, 8.0]
    assert concat(xs, sx) == [3.0, 4.0, 7.0, 8.0]


def test_sub_empty() -> None:
    """Edge case for sub."""
    xs: list[float] = []
    assert sub(xs, 0, 0) == []


def test_sub_many() -> None:
    """Use case 1 for sub."""
    xs: list[float] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_many_again() -> None:
    """Use case 2 for sub."""
    xs: list[float] = [0, 1, 2, 3, 4]
    assert sub(xs, 2, 4) == [2, 3]
"""EX07 - Dictionary Function Tests."""

__author__ = "730463283"

from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Edge case for invert."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_many() -> None:
    """Use case 1 for invert."""
    xs: dict[str, str] = {"a": "b", "l": "m", "d": "e"}
    assert invert(xs) == {"b": "a", "m": "l", "e": "d"}


def test_invert_many_again() -> None:
    """Use case 2 for invert."""
    xs: dict[str, str] = {"ella": "lilly", "gracie": "kate", "marion": "loulie"}
    assert invert(xs) == {"lilly": "ella", "kate": "gracie", "loulie": "marion"}


def test_favorit_color_empty() -> None:
    """Edge case for favorite_color."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_favorite_color_many() -> None:
    """Use case 1 for favorite_color."""
    xs: dict[str, str] = {"Ella": "green", "Lilly": "green", "Loulie": "blue"}
    assert favorite_color(xs) == "green"


def test_favorite_color_many_again() -> None:
    """Use case 2 for favorite_color."""
    xs: dict[str, str] = {"Campbell": "orange", "Caroline": "pink", "Mary": "pink", "Blair": "yellow"}
    assert favorite_color(xs) == "pink"


def test_count_empty() -> None:
    """Edge case for count."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_many() -> None:
    """Use case 1 for count."""
    xs: list[str] = ["flower", "power", "shower", "flower", "power"]
    assert count(xs) == {"flower": 2, "power": 2, "shower": 1}


def test_count_many_again() -> None:
    """Use case 2 for count."""
    xs: list[str] = ["cup", "cup", "cup", "mug", "plate", "mug", "bowl"]
    assert count(xs) == {"cup": 3, "mug": 2, "plate": 1, "bowl": 1}

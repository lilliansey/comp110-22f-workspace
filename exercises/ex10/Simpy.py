"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730463283"


class Simpy:
    """Utility class to assist in working with sequences of numerical data."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Entrypoint: initialize values attribute."""
        self.values = values

    def __repr__(self) -> str:
        """Automagically called when Simpy object is converted to an str representation able to be interperted."""
        return f"Simpy({self.values})"

    def fill(self, value_fill: float, number: int) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        self.values.clear()
        i: int = 0
        while i < number:
            self.values.append(value_fill)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        self.values.clear()
        assert step != 0.0
        i: float = start
        if stop > start:
            while i < stop:
                self.values.append(i)
                i += step
        if step < 0:
            while i > stop:
                self.values.append(i)
                i += step

    def sum(self) -> float:
        """Sum of all items in a list."""
        result: float = 0.0
        for item in range(0, len(self.values)):
            result += self.values[item]
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adding operations together if float OR Simpy."""
        if isinstance(rhs, float):
            final: list[float] = []
            for item in self.values:
                final.append(item + rhs)
            return Simpy(final)
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
            return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raising operations to the power of one another if float OR Simpy."""
        if isinstance(rhs, float):
            final: list[float] = []
            for item in self.values:
                final.append(item ** rhs)
            return Simpy(final)
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
            return Simpy(result)
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Mask based on equality of each item in calues with Simpy or float."""
        if isinstance(rhs, float):
            final: list[bool] = []
            i: int = 0 
            while i < len(self.values):
                if self.values[i] == rhs:
                    final.append(True)
                else:
                    final.append(False)
                i += 1
        else:
            final: list[bool] = []
            i: int = 0 
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    final.append(True)
                else:
                    final.append(False)
                i += 1
        return final

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a mask based on the greater than relationships between each item in values with a Simpy or float."""
        if isinstance(rhs, float):
            final: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    final.append(True)
                else:
                    final.append(False)
                i += 1
        else:
            final: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    final.append(True)
                else:
                    final.append(False)
                i += 1
        return final

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Using subscription operation to select individual items and filter with a mask with a list[bool]."""
        if isinstance(rhs, int):
            for i in range(0, len(self.values)):
                if rhs == i:
                    return self.values[i]
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                if rhs[i] is True:
                    result.append(self.values[i])
            return Simpy(result)
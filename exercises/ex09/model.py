"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730463283"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> int:
        """Determine the distance between two cells."""
        length: int
        length = sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return length


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """The tick function updates the view controller for location, direction, and recovery period."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()
    
    def contract_disease(self) -> None:
        """Assign the Infected constant to the sickness attribute."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Determine whether a cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Determine whether a cell is infected."""
        if self.sickness >= constants.INFECTED and not self.is_immune():
            return True
        else:
            return False

    def immunize(self) -> None:
        """Gives immunity to cells."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Determine whether a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False

    def color(self) -> str:
        """Change the color of a cell based on its infection status."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "pink"
        elif self.is_immune():
            return "blue"

    def contact_with(self, other: Cell) -> None:
        """Change the status of a cell to infected when a vulnerable cell comes in contact with an infected cell."""
        if other.is_vulnerable() is True and self.is_infected() is True:
            other.contract_disease()
        if self.is_vulnerable() is True and other.is_infected() is True:
            self.contract_disease()
            

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, num_infected: int, num_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        normal_cells: int = cells - (num_infected + num_immune)
        if num_infected >= cells or num_infected <= 0:
            raise ValueError("Some number of the cells must begin infected.")
        if num_immune >= cells:
            raise ValueError("The number of immune cells can not exceed the total number of cells. ")
        if (num_immune + num_infected) >= cells:
            raise ValueError("The number of immune and infected cells must not exceed the number of cells.")
        for _ in range(normal_cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(num_infected):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.contract_disease()
            self.population.append(cell)
        for _ in range(num_immune):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.immunize()
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        elif cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        elif cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        elif cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for i in range(len(self.population)):
            if self.population[i].is_infected():
                return False
        else: 
            return True

    def check_contacts(self) -> None:
        """Test whether any two Cell values come in constact with one another."""
        for i in range(len(self.population)):
            for j in range(i + 1, len(self.population)):
                cell_distance = self.population[i].location.distance(self.population[j].location)
                if cell_distance <= constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
        return
"""The ViewController drives the visualization of the simulation.""" 

from turtle import Turtle, Screen, _Screen, done
from exercises.ex09.model import Model
from exercises.ex09 import constants
from typing import Any
from time import time_ns


NS_TO_MS: int = 1000000


class ViewController:
    """This class is responsible for controlling the simulation and visualizing it."""
    screen: _Screen
    pen: Turtle
    model: Model

    def __init__(self, model: Model):
        """Initialize the VC."""
        self.model = model
        self.screen = Screen()
        self.screen.setup(constants.VIEW_WIDTH, constants.VIEW_HEIGHT)
        self.screen.tracer(0, 0)
        self.screen.delay(0)
        self.screen.title("Contagion Simulation - EX09")
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)

    def start_simulation(self) -> None:
        """Call the first tick of the simulation and begin turtle gfx."""
        self.tick()
        done()

    def tick(self) -> None:
        """Update the model state and redraw visualization."""
        start_time = time_ns() // NS_TO_MS
        self.model.tick()
        self.pen.clear()
        for cell in self.model.population:
            self.pen.penup()
            self.pen.goto(cell.location.x, cell.location.y)
            self.pen.pendown()
            self.pen.color(cell.color())
            self.pen.dot(constants.CELL_RADIUS)
            self.model.check_contacts()
    
        self.screen.update()
        if self.model.is_complete():
            return
        else:
            end_time = time_ns() // NS_TO_MS
            next_tick = 30 - (end_time - start_time)
            if next_tick < 0:
                next_tick = 0
            self.screen.ontimer(self.tick, next_tick)
import random
from turtle import Turtle
from config import UNIT_SIZE

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.restart()

    def restart(self):
        random_direction = random.randrange(0, 360)
        self.setheading(random_direction)
        self.move()

    def move(self):
        self.forward(UNIT_SIZE)

    def bounce(self, hit_direction):
        current_direction = self.heading()
        if hit_direction == "top":
            self.setheading(360-current_direction)
        if hit_direction == "bottom":
            self.setheading(360-current_direction)
        if hit_direction == "left":
            self.setheading(180-current_direction)
        if hit_direction == "right":
            self.setheading(180-current_direction)


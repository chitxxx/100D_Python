from turtle import Turtle
import random

# define constants
UNIT_SIZE = 20
STARTING_POSITION = [(-UNIT_SIZE, 0), (0, 0), (UNIT_SIZE, 0)]
SCREEN_SIZE = (int(600), int(600))
SCORE = 0

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()

    def refresh(self):
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)


from turtle import Turtle
from config import UNIT_SIZE


class PaddleDot(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()


class Paddle:
    def __init__(self,
                 size=3,
                 starting_x=0,
                 starting_y=0):
        self.body = [PaddleDot() for _ in range(size)]
        for pos in range(size):
            self.body[pos].goto(starting_x, starting_y*pos-pos*UNIT_SIZE)

    def move(self):
        for dot in self.body:
            dot.forward(UNIT_SIZE)

    def move_up(self):
        for dot in self.body:
            dot.setheading(90)

    def move_down(self):
        for dot in self.body:
            dot.setheading(270)

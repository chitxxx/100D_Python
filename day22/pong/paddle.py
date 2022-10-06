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
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.size = size
        for pos in range(self.size):
            self.body[pos].goto(starting_x, starting_y*pos-pos*UNIT_SIZE)


    def move_up(self):
        for dot in self.body:
            dot.setheading(90)
            dot.forward(UNIT_SIZE)

    def move_down(self):
        for dot in self.body:
            dot.setheading(270)
            dot.forward(UNIT_SIZE)

    def reset(self):
        for pos in range(self.size):
            self.body[pos].goto(self.starting_x, self.starting_y*pos-pos*UNIT_SIZE)


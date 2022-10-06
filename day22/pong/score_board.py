from turtle import Turtle
from config import (SCREEN_HEIGHT,
                    SCREEN_WIDTH)

ALIGNMENT = "center"
FONT = ("Arial", 15, 'normal', 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("black")
        self.pencolor("white")
        self.penup()
        self.goto(0, SCREEN_HEIGHT/2 - 50)
        self.write_score()

    def write_score(self):
        self.write(f"{self.left_score} : {self.right_score}",
                   align=ALIGNMENT,
                   font=FONT)

    def update_score(self, winner):
        if winner == "right":
            self.right_score += 1
        if winner == "left":
            self.left_score += 1
        self.clear()
        self.write_score()

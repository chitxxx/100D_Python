from turtle import Turtle
import random

# define constants
UNIT_SIZE = 20
STARTING_POSITION = [(-UNIT_SIZE, 0), (0, 0), (UNIT_SIZE, 0)]
SCREEN_SIZE = (int(600), int(600))
SCORE = 0
ALIGNMENT = "center"
FONT = ("Arial", 15, 'normal', 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.pencolor("white")
        self.penup()
        self.goto(0, 260)
        self.write_score()

    def write_score(self):
        self.write(f"SCORE: {self.score}",
                   align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER...",
                   align=ALIGNMENT,
                   font=FONT)


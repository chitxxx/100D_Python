import turtle
from turtle import Turtle, Screen
import random

## set config
N_TURTLES = 6
WIDTH = 500
HEIGHT = 400
COLORS = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE"]

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)

bet_color = screen.textinput(title="Make your bet",
                             prompt="Which turtle do you want to bet on? (Enter a colour.)")

turtles = []

for i in range(N_TURTLES):
    turtles.append(Turtle())
    turtles[i].shape("turtle")
    turtles[i].name = COLORS[i]
    turtles[i].color(COLORS[i])
    turtles[i].penup()
    turtles[i].goto(x=-0.9*WIDTH/2 + 10,
                    y= -HEIGHT/2 + i*0.9*HEIGHT/N_TURTLES + 50)

FINISH_LINE = 0.9*WIDTH/2 - 10
fastest_position = max([turtle.pos()[0] for turtle in turtles])
print(fastest_position)

while fastest_position < FINISH_LINE:
    moving_turtle = random.choice(turtles)
    moving_turtle.forward(10)
    fastest_position = max([turtle.pos()[0] for turtle in turtles])

winner = [turtle.name for turtle in turtles if turtle.pos()[0] == FINISH_LINE][0]
print(f"The {winner} turtle won!")

screen.exitonclick()

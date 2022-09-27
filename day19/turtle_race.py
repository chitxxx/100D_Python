import turtle
from turtle import Turtle, Screen

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
    turtles[i].color(COLORS[i])
    turtles[i].penup()
    turtles[i].goto(x=-0.9*WIDTH/2 + 10,
                    y= -HEIGHT/2 + i*0.9*HEIGHT/N_TURTLES + 50)
fastest_x = max([turtle.])

screen.exitonclick()

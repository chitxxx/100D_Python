import random
import numpy as np
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
timmy = Turtle()
timmy.speed("fast")
timmy.color("black", "DarkOliveGreen4")
timmy.shape("turtle")
timmy.width(5)

COLOURS_LIST = ["tomato", "dark magenta", "green yellow", "light sky blue", "navy"]

## TODO 1: Draw Square
# draw a square
# for i in range(4):
#    dian.forward(100)
#   dian.right(90)

## TODO 2: Draw Dotted Line
def draw_dotted_line(turtle, length, dot_space=5):
    drew = 0
    turtle.pendown()
    while drew <= length:
        turtle.forward(dot_space)
        turtle.penup()
        turtle.forward(dot_space)
        turtle.pendown()
        drew += dot_space * 2


# draw_dotted_line(timmy, 300)

## TODO 3: Draw Polygon
def draw_polygon(turtle, sides, side_length=50):
    turn_angle = 360 / sides
    for i in range(sides):
        turtle.forward(side_length)
        turtle.right(turn_angle)


# for s in range(3, 11):
#     timmy.color(random.choice(COLOURS_LIST))
#     draw_polygon(timmy, s)

## TODO 4: Random Walk
def random_walk(turtle, segments, segment_length=20):
    angles = [0, 90, 180, 270]
    for _ in range(segments):
        direction = random.choice(angles)
        color = get_random_color()
        turtle.pencolor(*color)
        turtle.setheading(direction)
        turtle.forward(segment_length)

def get_random_color():
    color = list(np.random.choice(range(256), size=3))
    return color

#random_walk(timmy, 250)

## TODO 5: Draw Circle

def draw_spirograph(turtle, n_circles=30, radius=100):
    turn_angle = 360/n_circles
    for _ in range(n_circles):
        color = get_random_color()
        turtle.pencolor(*color)
        turtle.circle(radius)
        turtle.left(turn_angle)

# draw_spirograph(timmy)

screen = Screen()
screen.exitonclick()

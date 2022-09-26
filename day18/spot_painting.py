import random

import colorgram
import urllib.request
import turtle
from turtle import Turtle, Screen

# get image
IMAGES_URL = [
    "https://images.squarespace-cdn.com/content/v1/5bc2bdbc0cf57d43ef55567e/1541204803866-CVTE7ZGXMXYNPVKF6U0D/chiawu-portfolio-starbucks-posters-05.jpg"
]
urllib.request.urlretrieve(IMAGES_URL[0], "image.jpg")

# # read image as tuple
# im = Image.open("image.jpg", 'r')
# pixel_values = list(im.getdata())

# extract colors
colors = colorgram.extract("image.jpg", 6)
colors = [color.rgb for color in colors]

# initalize turtle
N_COLS = 10
N_ROWS = 10
WIDTH = 600
HEIGHT = 600
SPACE = 50
turtle.colormode(255)

# initalize Turtle instance
timmy = Turtle()
timmy.speed("fast")
timmy.shape("turtle")

# initalize Screen instance
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)

# draw spots
timmy.penup()
timmy.goto(-WIDTH/2+SPACE, -HEIGHT/2+SPACE)
for _ in range(N_ROWS):
    for _ in range(N_COLS):
        color = random.choice(colors)
        timmy.dot(25)
        timmy.color(*color)
        timmy.penup()
        timmy.forward(SPACE)
    timmy.setheading(90)
    timmy.forward(SPACE)
    timmy.setheading(180)
    timmy.forward(SPACE*N_COLS)
    timmy.setheading(0)

screen.exitonclick()

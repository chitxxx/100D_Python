from turtle import Turtle, Screen
import time

# intialize screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snaking")
screen.tracer(0)

# initalize snake
STARTING_POSITION = [(-20, 0), (0, 0), (20, 0)]


class SnakeDot(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()


snake = [SnakeDot() for _ in range(3)]
for i in range(3):
    snake[i].goto(*STARTING_POSITION[i])
screen.update()

# move snake:
def move_snake(snake):
    snake_len = len(snake)
    print(snake_len)
    for dot in range(snake_len-1, 0, -1):
        snake[dot].goto(snake[dot-1].pos())
    snake[0].forward(20)
    screen.update()

def turn_left():
    snake[0].left(90)

def turn_right():
    snake[0].right(90)

screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')
screen.listen()


while True:
    move_snake(snake)
    time.sleep(0.1)

screen.exitonclick()

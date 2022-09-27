from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed("fast")

screen = Screen()


def move_forward():
    timmy.forward(1)


def move_backward():
    timmy.backward(1)

def turn_left():
    timmy.left(1)

def turn_right():
    timmy.right(1)

def clear_screen():
    timmy.home()
    timmy.clear()


screen.onkeypress(move_forward, 'w')
screen.onkeypress(move_backward, 's')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')
screen.onkeypress(clear_screen, 'c')
screen.listen()

screen.exitonclick()

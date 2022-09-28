from turtle import Turtle, Screen
from snake import Snake
import time

# initalize environment
UNIT_SIZE = 20


# intialize screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snaking")
screen.tracer(0)

snake = Snake()
screen.update()

screen.onkeypress(snake.face_up, 'Up')
screen.onkeypress(snake.face_down, 'Down')
screen.onkeypress(snake.face_left, 'Left')
screen.onkeypress(snake.face_right, 'Right')
screen.listen()

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    snake.move()
    screen.update()

screen.exitonclick()

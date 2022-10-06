import time
from turtle import Turtle, Screen

from config import (SCREEN_HEIGHT,
                    SCREEN_WIDTH)
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

# initalize environment
UNIT_SIZE = 10

X_LEFT_BOUND = -SCREEN_WIDTH / 2
X_RIGHT_BOUND = SCREEN_WIDTH / 2
Y_TOP_BOUND = -SCREEN_HEIGHT / 2
Y_BOTTOM_BOUND = SCREEN_HEIGHT / 2

# intialize screen
screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(starting_x=X_LEFT_BOUND + 3 * UNIT_SIZE)
right_paddle = Paddle(starting_x=X_RIGHT_BOUND - 3 * UNIT_SIZE)

# define ball
ball = Ball()

score_board = ScoreBoard()


def wall_collision(ball):
    x_ball, y_ball = ball.pos()
    if y_ball >= Y_TOP_BOUND:
        ball.bounce(hit_direction="top")
    if y_ball <= Y_BOTTOM_BOUND:
        ball.bounce(hit_direction="bottom")
    if x_ball >= X_RIGHT_BOUND:
        score_board.update_score("left")
        time.sleep(0.2)
        left_paddle.reset()
        right_paddle.reset()
        ball.restart()
    if x_ball <= X_LEFT_BOUND:
        score_board.update_score("right")
        time.sleep(0.2)
        left_paddle.reset()
        right_paddle.reset()
        ball.restart()

def paddle_collision(ball, left_paddle, right_paddle):
    if min([dot.distance(ball) for dot in left_paddle.body]) <=10:
        ball.bounce(hit_direction="right")
    if min([dot.distance(ball) for dot in right_paddle.body]) <=10:
        ball.bounce(hit_direction="left")

screen.update()

is_game_on = True

screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')
screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.listen()

while is_game_on:
    time.sleep(0.1)
    wall_collision(ball)
    paddle_collision(ball, left_paddle, right_paddle)
    ball.move()
    screen.update()

screen.exitonclick()

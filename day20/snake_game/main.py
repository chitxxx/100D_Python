from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

# initalize environment
UNIT_SIZE = 20

# detect_high_score
with open('high_score.txt') as f:
    high_score = f.readlines()[0]

# intialize screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snaking")
screen.tracer(0)

food = Food()
score_board = ScoreBoard(high_score)
snake = Snake()
screen.update()

screen.onkeypress(snake.face_up, 'Up')
screen.onkeypress(snake.face_down, 'Down')
screen.onkeypress(snake.face_left, 'Left')
screen.onkeypress(snake.face_right, 'Right')
screen.listen()

is_game_on = True


def check_eaten(food, snake):
    distance = snake.head.distance(food)
    return distance < UNIT_SIZE / 2


def wall_collision(snake):
    x_head, y_head = snake.head.pos()
    if x_head < -300 or x_head > 300:
        return True
    if y_head < -300 or y_head > 300:
        return True
    return False


while is_game_on:
    time.sleep(0.1)
    snake.move()
    if check_eaten(food, snake):
        snake.grow()
        food.refresh()
        score_board.increase_score()
    if wall_collision(snake):
        is_game_on = False
    if snake.check_dead():
        is_game_on = False
    screen.update()

with open('high_score.txt', 'w') as f:
    f.writelines([str(score_board.score)])

score_board.game_over()
screen.update()

screen.exitonclick()

import numpy as np

BANNER = """
 _      _     _      ____  _____ ____  ____ 
/ \  /|/ \ /\/ \__/|/  __\/  __//  __\/ ___\
| |\ ||| | ||| |\/||| | //|  \  |  \/||    \
| | \||| \_/|| |  ||| |_\\|  /_ |    /\___ |
\_/  \|\____/\_/  \|\____/\____\\_/\_\\____/
                                                                                                                             
 """

LIFE_CONFIG = {'easy': 10,
                  'hard': 5}
def set_lives():
    level = input("Choose a difficulty. Type 'easy' or 'hard'.")
    lifes = LIFE_CONFIG[level]
    return lifes

def check_guess(guess, answer):
    if guess > answer:
        print('Too high.')
    elif guess < answer:
        print('Too low.')
    else:
        print('You got it!')
    return guess == answer

def run_game():
    print(BANNER)
    print("Welcome to the game!")

    lives = set_lives()
    answer = np.random.randint(low = 1,high = 100)
    while lives > 0:
        print(f'You have {lives} lives.')
        guess = int(input("Take a guess."))
        correct = check_guess(guess, answer)
        if correct:
            return
        lives -=1

    else:
        print(f'You have {lives} lives, you lost.')

run_game()
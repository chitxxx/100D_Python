import turtle
from turtle import Turtle
import pandas as pd
# initialize screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# add background map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # click to get screen coordinates
# def get_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_coor)

df_states = pd.read_csv("50_states.csv")
df_states.set_index("state", inplace=True)


# initalize writer
ALIGNMENT = "center"
FONT = ("Arial", 15, 'normal', 'bold')
class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.color("yellow")
        self.pencolor("black")
        self.penup()

    def write_state(self, x, y, state):
        self.goto(x,y)
        self.write(state,
                   align=ALIGNMENT,
                   font=FONT)

writer = Writer()

state_left = 50
guessed_state = []
while state_left>0:
    answer_state = screen.textinput(title="Guess a state",
                                    prompt=f"{state_left} states left, take a guess a state")
    if answer_state in df_states.index:
        print("Yes")
        writer.write_state(df_states.loc[answer_state, "x"],
                           df_states.loc[answer_state, "y"],
                           answer_state)
        guessed_state.append(answer_state)
        state_left-=1

    if answer_state == "exit":
        break

if state_left>=0:
    print(f"You missed {state_left}states:")
    print(df_states.loc[~(df_states.index.isin(guessed_state))].index.tolist())



# writer.write_state(50, 50, "test")

# screen.exitonclick()
turtle.mainloop()
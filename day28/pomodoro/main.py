from tkinter import (Tk,
                     Canvas,
                     PhotoImage,
                     Label,
                     Button)

import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
reset = 0

SCHEDULE = {
    0: 5,
    1: SHORT_BREAK_MIN * 60,
    2: WORK_MIN * 60,
    3: SHORT_BREAK_MIN * 60,
    4: WORK_MIN * 60,
    5: SHORT_BREAK_MIN * 60,
    6: WORK_MIN * 60,
    7: LONG_BREAK_MIN * 60,

}

# ---------------------------- TIMER RESET ------------------------------- #
start_count = WORK_MIN * 60


def reset_timer():
    global reset, reps
    reset = 1
    reps = 0
    start_count = 25 * 60
    mins, secs = divmod(start_count, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfig(timer_text, text=timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if reset == 1:
        title.config(text="Pomodoro Timer")
        return
    mins, secs = divmod(count, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfig(timer_text, text=timer)
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        global reps
        reps += 1
        start_timer()


def start_timer():
    global reset, reps
    reset = 0
    if reps % 2 == 0:
        title.config(text="Work")
    else:
        title.config(text="Break")
    count_down(SCHEDULE[reps])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

background_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=background_img)
timer_text = canvas.create_text(100, 130, text="Timer Idle", fill="white", font=(FONT_NAME, 35, "bold"))
reset_timer()

title = Label(text="Pomodoro Timer",
              fg=GREEN, bg=YELLOW,
              font=("Arial", 24, "bold"))

start_button = Button(text="Start", width=10, command=start_timer)
reset_button = Button(text="Reset", width=10, command=reset_timer)
canvas.grid(column=2, row=2)
title.grid(column=2, row=1)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)

window.mainloop()

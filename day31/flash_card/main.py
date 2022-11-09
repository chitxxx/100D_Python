from tkinter import (Tk,
                     Canvas,
                     PhotoImage,
                     Label,
                     Entry,
                     Button,
                     messagebox)

import random
import pandas as pd
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
PAD = 50


# ---------------------------- UI SETUP ------------------------------- #
# initialize window
window = Tk()
window.title("Flash Card")
window.config(padx=PAD, pady=PAD, bg=BACKGROUND_COLOR)

# create background logo
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
img_card_front = PhotoImage(file="images/card_front.png")
img_background = canvas.create_image(400, 263, image=img_card_front)
text_language = canvas.create_text(400,150,text="French", font=("Ariel", 40, "italic"))
text_word = canvas.create_text(400,263,text="Word", font=("Ariel", 60, "bold"))

img_right = PhotoImage(file="images/right.png")
button_right = Button(image=img_right, highlightthickness=0)
img_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0)

# render objects
canvas.grid(row=1, column=1, columnspan=2)
button_right.grid(row=2, column=1)
button_wrong.grid(row=2, column=2)

# ---------------------------- WORDS ------------------------------- #
words = pd.read_csv("data/french_words.csv").to_dict(orient="records")

img_card_back = PhotoImage(file="images/card_back.png")
def flip_card(word_answer):
    canvas.itemconfig(img_background, image=img_card_back)
    canvas.itemconfig(text_language, text="English")
    canvas.itemconfig(text_word, text=word_answer)

def next_word():
    global flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(words)
    canvas.itemconfig(img_background, image=img_card_front)
    canvas.itemconfig(text_language, text="French")
    canvas.itemconfig(text_word, text=word["French"])

    flip_timer = window.after(3000, flip_card, word["English"])
    print(count_correct, count_wrong)

flip_timer = window.after(0, next_word)

count_correct = 0
count_wrong = 0

def correct_answer():
    global count_correct
    count_correct += 1
    next_word()

def wrong_answer():
    global count_wrong
    count_wrong += 1
    next_word()

button_right.config(command=correct_answer)
button_wrong.config(command=wrong_answer)


window.mainloop()
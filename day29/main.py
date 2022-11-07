from tkinter import (Tk,
                     Canvas,
                     PhotoImage,
                     Label,
                     Entry,
                     Button,
                     messagebox)
import random
import json

# ---------------------------- UI SETUP ------------------------------- #

# setup
PAD = 50
# initialize window
window = Tk()
window.title("Passer")
window.config(padx=PAD, pady=PAD)

# create background logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
background_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_img)

# create website row
lable_website = Label(text="Website")
entry_website = Entry(width=35)
button_search = Button(text="Search Password")

# create username row
lable_username = Label(text="Email/Username")
entry_username = Entry(width=35)

# create password row
lable_password = Label(text="Password")
entry_password = Entry(width=21)
button_password = Button(text="Generate Password")

# create add row
button_add = Button(text="Add", width=36)

# set layout
canvas.grid(row=1, column=2)

lable_website.grid(row=2, column=1)
entry_website.grid(row=2, column=2)
button_search.grid(row=2, column=3)

lable_username.grid(row=3, column=1)
entry_username.grid(row=3, column=2, columnspan=2)

lable_password.grid(row=4, column=1)
entry_password.grid(row=4, column=2)
button_password.grid(row=4, column=3)

button_add.grid(row=5, column=2, columnspan=2)

# launch Operations
DEFAULT_USERNAME = "user"
entry_website.focus()
entry_username.insert(0, DEFAULT_USERNAME)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_list = []
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    entry_password.delete(0, 'end')
    entry_password.insert(0, password)


button_password.config(command=generate_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    confirm = messagebox.askokcancel(title="Save Password",
                                     message="Save Password?")

    if not confirm:
        return

    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    # check valid password
    if len(website) == 0 or " " in website:
        messagebox.showwarning(title="Invalid Website",
                               message="Invalid Website")
        return

    if len(username) == 0 or " " in username:
        messagebox.showwarning(title="Invalid Username",
                               message="Invalid Username")
        return

    if len(password) == 0 or " " in password:
        messagebox.showwarning(title="Invalid Password",
                               message="Invalid Password")
        return

    new_data = {website: {"username": username,
                          "password": password}}
    try:
        with open("data.json", "r") as datafile:
            data = json.load(datafile)
            data.update(new_data)
    except FileNotFoundError:
        with open("data.json", "w") as datafile:
            json.dump(new_data, datafile, indent=4)
    else:
        with open("data.json", "w") as datafile:
            json.dump(data, datafile, indent=4)

    entry_website.delete(0, 'end')
    entry_username.delete(0, 'end')
    entry_password.delete(0, 'end')
    entry_username.insert(0, DEFAULT_USERNAME)

    messagebox.showinfo(title="Password Saved",
                        message="Password Saved")


button_add.config(command=save_password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    # load saved data
    try:
        with open("data.json", "r") as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        data = dict()

    # fill password
    website = entry_website.get()
    try:
        username = data[website]["username"]
        password = data[website]["password"]
    except KeyError:
        messagebox.showwarning(title="No Saved Password",
                               message="No Saved Password")
    else:
        entry_username.delete(0, 'end')
        entry_password.delete(0, 'end')
        entry_username.insert(0, username)
        entry_password.insert(0, password)


button_search.config(command=search_password)

window.mainloop()

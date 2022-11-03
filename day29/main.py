from tkinter import (Tk,
                     Canvas,
                     PhotoImage,
                     Label,
                     Entry,
                     Button,
                     messagebox)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
entry_website.grid(row=2, column=2, columnspan=2)

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

    with open("data.txt", "a") as datafile:
        datafile.write(f"{website} | {username} | {password} \n")

    entry_website.delete(0, 'end')
    entry_username.delete(0, 'end')
    entry_password.delete(0, 'end')
    entry_username.insert(0, DEFAULT_USERNAME)

    messagebox.showinfo(title="Password Saved",
                        message="Password Saved")


button_add.config(command=save_password)

window.mainloop()

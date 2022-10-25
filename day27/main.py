import tkinter

# initialize window
window = tkinter.Tk()
window.title("Application")
window.minsize(width=500, height=300)

# create label
label = tkinter.Label(text="Hi!", font=("Arial", 25, "bold"))
label.pack(expand=True)
label.config(text="Application 1.0")  # update properties

# create entry
input = tkinter.Entry()
input.pack()

# create button
def button_clicked():
    label.config(text=input.get())
button = tkinter.Button(text="Click Me",
                        command=button_clicked,
                        width=10)
button.pack(expand=True)

# keep window running
window.mainloop()
import tkinter

# config
APPLICATION_NAME = "Mile to Kilometer Convertor"
# initialize window
window = tkinter.Tk()
window.title(APPLICATION_NAME)
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# create label
title = tkinter.Label(text=APPLICATION_NAME, font=("Arial", 16, "bold"))
unit_in = tkinter.Label(text="km")
unit_out = tkinter.Label(text="Mile")
result = tkinter.Label(text="Click to Convert", font=("Arial", 16, "bold"))

# create entry
input = tkinter.Entry()


# create button
def button_clicked():
    if conversion_option.get() ==1:
        conversion_factor = 1.60934
    else:
        conversion_factor = 1/1.60934
    val_input = float(input.get())
    val_output = val_input * conversion_factor
    result.config(text=val_output)


button = tkinter.Button(text="Convert",
                        command=button_clicked,
                        width=10)


# create conversion option
def update_conversion_option():
    if conversion_option.get() == 1:
        unit_in.config(text="km")
        unit_out.config(text="Mile")
    if conversion_option.get() == 2:
        unit_in.config(text="Mile")
        unit_out.config(text="km")


conversion_option = tkinter.IntVar()
option_button1 = tkinter.Radiobutton(text="Mile>km",
                                     value=1,
                                     variable=conversion_option,
                                     command=update_conversion_option)
option_button2 = tkinter.Radiobutton(text="km>Mile",
                                     value=2,
                                     variable=conversion_option,
                                     command=update_conversion_option)

# render objects
title.grid(column=2, row=1)
input.grid(column=1, row=2)
unit_in.grid(column=1, row=3)
result.grid(column=3, row=2)
unit_out.grid(column=3, row=3)
button.grid(column=2, row=4)
option_button1.grid(column=1, row=5)
option_button2.grid(column=2, row=5)

# keep window running
window.mainloop()

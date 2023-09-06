from tkinter import *


def calculate_Km(miles=None):
    miles = float(Miles.get())
    kilometer = (miles * 1.6)
    Km.config(text = kilometer)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

Miles = Entry(width=7)
Miles.grid(column=1, row=0)

Miles_label = Label(text="Miles")
Miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to ")
equal_to_label.grid(column=0, row=1)

Km_label = Label(text="Km")
Km_label.grid(column=2, row=1)

Km = Label(text="0")
Km.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate_Km)
button.grid(column=1, row=2)

window.mainloop()

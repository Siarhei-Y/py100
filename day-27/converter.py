from tkinter import *

window = Tk()
window.title('Mile to KM converter')
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

equal_label = Label(text='is equal to:', font=('Arial', 10))
equal_label.pack()
equal_label.grid(column=0, row=2)

equal_km = Label(text=0, font=('Arial', 10))
equal_km.grid(column=1, row=2)

miles = Label(text='Miles', font=('Arial', 10))
miles.grid(column=2, row=1)

km = Label(text='Km', font=('Arial', 10))
km.grid(column=2, row=2)

input = Entry(width=10)
input.grid(column=1, row=1)


def convert():
    n = input.get()
    conv_val = int(n) * 1.6
    equal_km = Label(text=int(conv_val), font=('Arial', 10))
    equal_km.grid(column=1, row=2)


button = Button(text='Calculate', command=convert)
button.grid(column=1, row=3)


window.mainloop()
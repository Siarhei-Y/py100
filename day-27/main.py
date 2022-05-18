from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

#label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.pack()


my_label['text'] = 'New text'
my_label.config(text='New text')
my_label.grid(column=0, row=0)

#button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text='Click me', command=button_clicked)
button.grid(column=1, row=2)

new_button = Button(text='Click me', command=button_clicked)
new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
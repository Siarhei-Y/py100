from tkinter import *
from tkinter.tix import COLUMN
from turtle import width
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password manager')
window.config(padx=20, pady=20, background='#FFFFFF')

canvas = Canvas(width=200, height=200, background='#FFFFFF', highlightthickness=0)
img = PhotoImage(file='day-29/logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text='Website:',background='#FFFFFF')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:',background='#FFFFFF')
email_label.grid(column=0, row=2)

pass_label = Label(text='Password:',background='#FFFFFF')
pass_label.grid(column=0, row=3)

#inputs
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)

input_user = Entry(width=35)
input_user.grid(column=1, row=2, columnspan=2)

input_pass = Entry(width=21)
input_pass.grid(column=1, row=3)

#buttons
generate_pass = Button(text='Generate Password',background="#FFFFFF")
generate_pass.grid(column=2, row=3)

add = Button(text='Add',background="#FFFFFF",width=36)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
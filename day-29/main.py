import email
from ntpath import join
from tkinter import *
from tkinter.tix import COLUMN
from turtle import width
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letters = [random.choice(letters) for i in range(nr_letters)]
    symbols = [random.choice(symbols) for i in range(nr_symbols)]
    numbers = [str(random.choice(numbers)) for i in range(nr_numbers)]
    password_list = letters + symbols + numbers
    random.shuffle(password_list)

    password = ''.join(password_list)

    input_pass.insert(0,password)

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = input_website.get()
    user = input_user.get()
    password = input_pass.get()
    new_data = {
        website : {
            'email': user,
            'password': password,
        }
    }

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message=r"Please make sure yuo haven't left any fields empty.")
    else:
        try:
            with open('day-29/data.json', 'r') as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open('data.json','w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update()
            with open('day-29/data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_pass.delete(0, END)
    


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50, background='#FFFFFF')

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
input_website.focus()

input_user = Entry(width=35)
input_user.grid(column=1, row=2, columnspan=2)

input_pass = Entry(width=20)
input_pass.grid(column=1, row=3)

#buttons
generate_pass = Button(text='Generate Password',background="#FFFFFF", command=generate_password)
generate_pass.grid(column=2, row=3)

add = Button(text='Add', background="#FFFFFF", width=36, command=save_data)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
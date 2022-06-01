from tkinter import *
from tkinter.tix import COLUMN
from turtle import width
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = letters + symbols + numbers
letters = [random.choice(letters) for i in range(nr_letters)]
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
symbols = [random.choice(symbols) for i in range(nr_symbols)]
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
numbers = [random.choice(numbers) for i in range(nr_numbers)]

# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = input_website.get()
    user = input_user.get()
    password = input_pass.get()

    if len(website) != 0 or len(user) != 0 or len(password) != 0:
        f = open("file.txt", "a")
        f.write(f"{website} | {user} | {password}\n")
        f.close()
        messagebox.showinfo(message='Credentials Saved')

        input_website.delete(0, END)
        input_user.delete(0, END)
        input_pass.delete(0, END)
    else:
        messagebox.showinfo(message='Please Try again')

    


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
generate_pass = Button(text='Generate Password',background="#FFFFFF")
generate_pass.grid(column=2, row=3)

add = Button(text='Add', background="#FFFFFF", width=36, command=save_data)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
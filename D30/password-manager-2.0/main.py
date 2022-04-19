from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing required fields", message="Please check if you've filled up al the "
                                                                     "necessary items")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)  # trying to read file

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #  updating old data
            data.update(new_data)

            # update the data
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    # this is how to update the JSON data, must load first, then update
    # 1. read the JSON file
    # 2. update the JSON file with the new data value
    # 3. then write into the data file


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().lower()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Here you go", message=f"website: {website}\nemail: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details exist for {website}")





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

# website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# website entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

# Email Label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

# Email Entry
email_entry = Entry(width=21)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "webtestercs102@gmail.com")
# everytime we run the app, the email field would have been pre-populated with a common email
# this is to improve User experience (Ux) because more often than not, user would have 1 common email for most things

# Password Label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Generate button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

# Search button
search_button = Button(text="Search", command=search_password, width=13)
search_button.grid(row=1, column=2)

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

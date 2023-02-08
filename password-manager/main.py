from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))] # Return a number between 8 and 10 (both included)
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]  # Return a number between 2 and 4 (included)
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]  # Return a number between 2 and 4 (included)

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)  # automatically copy the password so that we can just paste it on the website for sign up
    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you enter all the fields!!")
    else:

        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)
        with open("data.json", "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)  # Write json file

            website_entry.delete(0, END)  # Deleting the website entry after adding
            password_entry.delete(0, END)  # Deleting the password entry after adding

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Welcome to Password Manager!")  # adding title to the window
window.config(padx=50, pady = 50)  # adding 20 padding to x and y

canvas = Canvas(height=200, width=200)  # creating height & width size 200 canvas
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) # Expecting some tuple to work on. create_image(position, **options)
canvas.pack() # canvas layout dimension
canvas.grid(row=0, column=1)  # the first row from top and second column from left

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)  # shouldn't put "width" -> not working !

# Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan = 2)  # Extending column 1 to column 2
website_entry.focus()  # User can directly type here as soon as the program runs
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan =2)
email_entry.insert(0, "samuel@gmail.com")  # pre-populated email address without having to type my email
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command = generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop() # tells Python to run the Tkinter event loop. Running until you close the window.
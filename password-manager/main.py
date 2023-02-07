from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan =2)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop() # tells Python to run the Tkinter event loop. Running until you close the window.
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Welcome to Password Manager!")  # adding title to the window
window.config(padx=20, pady =20)  # adding 20 padding to x and y

canvas = Canvas(height=200, width=200)  # creating height & width size 200 canvas
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) # Expecting some tuple to work on. create_image(position, **options)
canvas.pack() # canvas layout dimension

window.mainloop() # tells Python to run the Tkinter event loop. Running until you close the window.
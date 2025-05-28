# Module 7 - Tkinter

# TASK DESCRIPTION
# Prepare a game of “Guess the number” with a graphical interface:
# a. The program randomly selects a number from 1 to 50
# b. If the user enters values that are closer and closer to the guessed number, the program should display “warm”
# c. If the user enters values that are further and further away, the program should display “cold”.
# 2. After entering the correct number, the program should display
# an appropriate message and answer in how many steps the user guessed.

# Import libraries
import tkinter as tk
from tkinter import messagebox
from random import randint


def send_number():
    global random_number, diff, nof_tries
    nof_tries += 1
    if int(given_number.get()) == random_number:
        messagebox.showinfo(title="Status: ", message=f"You guessed correctly after {nof_tries} tries!")
    elif abs(int(given_number.get()) - random_number) <= diff:
        messagebox.showinfo(title="Status: ", message="Warmer!")
    else:
        messagebox.showinfo(title="Status: ", message="Colder!")
    diff = abs(int(given_number.get()) - random_number)


window = tk.Tk()
window.title('Guess the number')

nof_tries = 0
diff = 100
random_number = randint(1, diff)

label = tk.Label(window, text="Guess the number")
label.pack()

given_number = tk.Entry()
given_number.pack()

button = tk.Button(text="OK", command=send_number)
button.pack()

window.mainloop()

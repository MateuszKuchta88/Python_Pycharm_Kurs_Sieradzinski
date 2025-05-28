# PD7 4 - Write name and surname to txt file program

# TASK DESCRIPTION
# Write a program that asks the user for his name
# and saves this information in a text file.

# Import libraries
import tkinter as tk
from tkinter import messagebox


# Declare function
def input_name():
    with open('writeName.txt', 'a', encoding='utf8') as handler, open('writeName.txt', 'r') as file:
        name = given_name.get()
        decision = True
        for line in file:
            if name in line:
                messagebox.showerror(title="Status: ", message=f'{name} is already present in file "writeName.txt".')
                decision = False
        if decision:
            messagebox.showinfo(title="Status: ", message=f'{name} successfully added to file "writeName.txt".')
            name += "\n"
            handler.write(name)


# Program
window = tk.Tk()
window.title('Write name')

label = tk.Label(window, text="Enter name and surname: ")
label.pack()

given_name = tk.Entry()
given_name.pack()

button = tk.Button(text="Enter", command=input_name)
button.pack()

window.mainloop()

# Print output message
# print()

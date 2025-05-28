# Module 7 - Expenses

# TASK DESCRIPTION
# Write a program to manage expenses in your home.
# The program should allow you to add a new expense.
# Store them in the expenses.json file

# Import libraries
from json import load, dump

# Declare function
with open('expenses.json') as file:
    decision = str(input('What do you want to do? [a] add expense, [p] print expenses: '))
    expenses = load(file)
    if decision == 'a':
        title = str(input('What is the name of this expense?: '))
        value = float(input('Give me value of this expense: '))
        expenses.append({"title": title, "value": value})
        with open('expenses.json', 'w') as new_file:
            dump(expenses, new_file)
    elif decision == 'p':
        for expense in expenses:
            print(expense.get("title"), expense.get("value"))

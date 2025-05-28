# Paper Rock Scissors Game

# Importing required function from random module
from random import choice

# Declaring tuple with possible options
options = 'paper', 'stone', 'scissors'

# Taking choice from user
user_choice = input("Possible options:\n'p' for paper;\n'r' for rock;\nor 's' for scissors.\nWhat is your choice?: ")

# Generating computer's choice
pc_choice = choice(options)

# Printing choices to summarize decision phase.
print(f'You chose {user_choice}.')
print(f'Computer chose {pc_choice}.')

# Declaring auxiliary dictionary
choices = {"user" : user_choice, "pc" : pc_choice}

# Comparing choices in order to get winner
if choices["user"] == choices["pc"]:
    print("We have a draw.")
elif 'stone' not in choices.values():
    if choices["user"] == "scissors":
        print("User wins.")
    else:
        print("Computer wins.")
elif 'scissors' not in choices.values():
    if choices["user"] == "paper":
        print("User wins.")
    else:
        print("Computer wins.")
elif 'paper' not in choices.values():
    if choices["user"] == "stone":
        print("User wins.")
    else:
        print("Computer wins.")
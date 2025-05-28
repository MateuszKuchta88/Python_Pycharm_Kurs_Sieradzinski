# Guess the number

# Randomize a number and ask the user to guess it. If the answer is too small, write "for".
# small”, if too large, then “too large”. The program ends when the user guesses
# the drawn number and displays the number of user "shots"

# Import libraries
from random import randint

# Initiate random number
min_limit = 1
max_limit = 1000
random_number = randint(min_limit, max_limit)

# Initiate var for storing guess number
print(f'I have picked random number for you. \nRange of possible values is {min_limit}-{max_limit}.')
user_pick = int(input("Guess this number: "))

# Initiate counter
no_of_tries = 1

# While loop which collects numbers
while random_number != user_pick:
    if user_pick < random_number:
        user_pick = int(input(f'Random number is bigger. Try again: '))
    else:
        user_pick = int(input(f'Random number is smaller. Try again: '))
    no_of_tries += 1

# Print output
print(f'Great, you guessed correct number in {no_of_tries} shot(s).')

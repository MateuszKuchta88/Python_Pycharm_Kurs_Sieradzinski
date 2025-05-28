# Take 10 positive numbers

# Ask user for 10 positive numbers. If the user provides a negative number
# then it should not be counted. Display the largest and smallest number.

# Import libraries
from random import randint

# Declare empty list
positive_numbers = []

# While loop which takes positive numbers
while len(positive_numbers) < 10:
    random_number = randint(-50, 150)
    if random_number > 0:
        positive_numbers.append(random_number)

# Print output
print(positive_numbers)
print(f'Smallest given number is {min(positive_numbers)} and biggest given number is {max(positive_numbers)}.')

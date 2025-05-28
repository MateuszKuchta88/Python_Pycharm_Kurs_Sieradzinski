# Average where every next is bigger

# Ask the user to enter numbers, each subsequent one being greater
# from the previous one. If this condition does not occur. The program should follow
# end. Display the average of these numbers.

# Import libraries
from random import randint

# Declare empty list
list_of_numbers = []

# Initiate var for storing previous number
previous_number = 0

# Initiate random number
random_number = randint(5, 15)

# Initiate auxiliary var
multiplier = 1

# While loop which collects numbers
while random_number > previous_number:
    list_of_numbers.append(random_number)
    previous_number = random_number
    random_number = randint(5 + 5 * multiplier, 15 + 5 * multiplier)
    multiplier += 1

# Print output
print(list_of_numbers)
print(f'Average of given numbers is {(sum(list_of_numbers)/len(list_of_numbers)):.2f}.')

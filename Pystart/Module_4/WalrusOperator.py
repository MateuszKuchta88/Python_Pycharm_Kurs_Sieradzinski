# Walrus operator

# Write a program that takes integers from the user and displays their sum.
# The while loop should run as long as the user enters a different number
# from 0. You can use the walrus operator in the while loop condition to check whether
# the user entered a number different from 0

# Import libraries
from random import randint

# Initiate random number
min_limit = 0
max_limit = 10
random_number = randint(min_limit, max_limit)

# Initiate sum of numbers
sum_of_inputs = 0

# While loop which sums numbers
while (value := random_number) != 0:
    sum_of_inputs += value
    random_number = randint(min_limit, max_limit)

# Print output
print(f'Sum of given numbers is {sum_of_inputs}.')

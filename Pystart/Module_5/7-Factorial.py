# Module 5 - Factorial

# TASK DESCRIPTION
# Using recurrence, write a factorial function for the given one
# by the user in the number argument.

# Import libraries

# Welcome message
print('\nWelcome in "Factorial" app.')

# Get data from user
given_number = int(input("\nGive me number for factorial calculation: "))

# Testing data
# given_number = 5
# print(f'\nNumber for factorial process: "{given_number}".')

# Declare variables


# Declare function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Call function
answer = factorial(given_number)

# Quit if wrong operation

# Process

# Print output message
print(f'Factorial of {given_number} is {answer}.')

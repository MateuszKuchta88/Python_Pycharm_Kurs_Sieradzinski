# Module 5 - Multiply

# TASK DESCRIPTION
# Write a function that takes two arguments, where the second one will be
# had a default value of 2. The function should return the given value
# the number multiplied by the multiplier.

# Import libraries

# Welcome message
print('\nWelcome in "Multiply" app.')

# Get data from user
no1 = float(input("\nGive me first number to process: "))
print("\nGive me second number to process, if you want to have it different than default (default = 2).")
no2 = str(input("If you want it to remain default write no numbers: "))

# Testing data
# no1 = 20
# no2 = 10
# print(f'\nNumbers under process: "{no1}, {number2}".')

# Declare variables


# Declare function
def multiply(n1, n2=2):
    return n1 * n2


# Call function
answer = multiply(no1, int(no2)) if no2.isnumeric() else multiply(no1)

# Quit if wrong operation

# Process

# Print output message
print(f'Result of multiplying is {answer}.')

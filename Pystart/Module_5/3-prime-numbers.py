# Module 5 - Prime numbers

# TASK DESCRIPTION
# Prepare a function that will return True or False, depending on
# whether this number is prime.

# Import libraries

# Welcome message
print('\nWelcome in "Prime numbers" app.')

# Get data from user
given_number = int(input("\nGive me any number which we should check if it is prime one: "))

# Testing data
# given_number = 17
# print(f'\nNumber under process: "{given_number}".')

# Declare variables


# Declare function
def check_if_prime_number(number):
    for n in range(2, round((number+1)/2)):
        if number % n == 0:
            return False
    return True


# Call function
answer = check_if_prime_number(given_number)

# Quit if wrong operation

# Process

# Print output message
print(f'{answer}')

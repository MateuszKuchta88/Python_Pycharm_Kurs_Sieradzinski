# Module 5 - Find the biggest common divisor

# TASK DESCRIPTION
# Prepare a function that will look for common divisors for two
# numbers. The function has a third default argument specifying the value
# initial, where the greatest common divisors must always be
# greater than this value.

# Import libraries

# Welcome message
print('\nWelcome in "Find the biggest common divisor" app.')

# Get data from user
no1 = int(input("\nGive me first number to process: "))
no2 = int(input("\nGive me second number to process: "))
print("\nGive me bottom limitation for common divisors (in default = 2).\n")
bottom_lim = str(input("If you want it to remain default write no numbers: "))

# Testing data
# no1 = 20
# no2 = 10
# print(f'\nNumbers under process: "{no1}, {number2}".')

# Declare variables


# Declare function
def get_biggest_comm_div(n1, n2, start_n=2):
    list_of_divisors = []
    lower = n1 if n1 <= n2 else n2
    for n in range(start_n + 1, lower + 1):
        if n1 % n == 0 and n2 % n == 0:
            list_of_divisors.append(n)
    return list_of_divisors


# Call function
answer = get_biggest_comm_div(no1, no2, int(bottom_lim)) if bottom_lim.isnumeric() else get_biggest_comm_div(no1, no2)

# Quit if wrong operation

# Process

# Print output message
print(f'{answer}')

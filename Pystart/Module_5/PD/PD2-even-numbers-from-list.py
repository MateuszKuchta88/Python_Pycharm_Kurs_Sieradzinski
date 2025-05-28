# PD5 2 - Even numbers from list

# TASK DESCRIPTION
# Prepare a function that will be able to filter even numbers from the list passed in the argument.

# Import libraries

# Welcome message
print('\nWelcome in "Even numbers from list" app.')

# Get data from user
given_list = list(str(input("\nGive me numbers list where I should look for evens, divided with ',': ")).split(","))

# Testing data
# given_list = [2, 4, 6, 5]
# print(f'\nList used in filtering is {given_list}.')

# Declare variables


# Declare function
def get_even(list_of_numbers: list) -> list:
    """
    Function takes list of numbers and returns list of even numbers from given list
    :param list_of_numbers: list of numbers where program should look for evens
    :return: list of evens out of given list of numbers
    """
    new_list = []
    for number in list_of_numbers:
        if float(number) % 2 == 0:
            new_list.append(number)
    return new_list


# Call function
ans = get_even(given_list)


# Quit if wrong operation

# Process

# Print output message
print(f'List of even numbers out of given list is: {ans}')

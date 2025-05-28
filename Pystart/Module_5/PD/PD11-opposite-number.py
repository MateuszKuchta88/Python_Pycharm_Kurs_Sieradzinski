# PD5 11 - Opposite number

# TASK DESCRIPTION
# Write a function that will convert every single positive element of the list into a negative one, a
# negative to positive.

# Import libraries


# Testing data
g_list = [1, 2, 3, -4]


# Declare function
def opposite_number_list(lst: list) -> list:
    """
    Function takes list of numbers and return list of numbers opposite to given one
    :param lst: given list of numbers
    :return: list of numbers opposite to given
    """
    new_list = []
    for number in lst:
        new_list.append(-1 * number)
    return new_list


# Print output message
print(f'Answer is {opposite_number_list(g_list)}.')

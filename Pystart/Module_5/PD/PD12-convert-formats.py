# PD5 12 - Convert formats

# TASK DESCRIPTION
# Prepare a function that will convert all list elements into strings and
# the second one which will convert each list element to an integer.

# Import libraries


# Testing data
g_list = [1, 2, 3, -4]


# Declare function
def convert_to_str(lst: list) -> list:
    """
    Function takes list and returns list of strings based on given list of elements
    :param lst: given list
    :return: list of strings
    """
    return list(map(str, lst))


def convert_to_int(lst: list) -> list:
    """
    Function takes list and returns list of integers based on given list of elements
    :param lst: given list
    :return: list of integers
    """
    return list(map(int, lst))


# Print output message
print(f'Answer is {convert_to_str(g_list)}.')
print(f'Answer is {convert_to_int(convert_to_str(g_list))}.')

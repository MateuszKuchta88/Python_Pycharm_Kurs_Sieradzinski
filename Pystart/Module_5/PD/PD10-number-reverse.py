# PD5 10 - Reverse number

# TASK DESCRIPTION
# Write a function that will take any number and return its numbers reverted, e.g. 12345 will turn into 54321,
# and 1998 will turn into 8991

# Import libraries


# Testing data
g_int = 19989


# Declare variables


# Declare function
def number_reverse(number: int) -> int:
    """
    Function takes integer and return its reverted format
    :param number: integer to be reverted
    :return: reverted integer
    """
    return int("".join(list(str(number))[::-1]))


# Print output message
print(f'Answer is {number_reverse(g_int)}.')

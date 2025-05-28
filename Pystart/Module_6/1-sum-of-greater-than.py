# Module 6 - Sum of numbers greater than limit

# TASK DESCRIPTION
# Write a function that accepts any number of arguments: numbers
# and the limit value. The function should return the sum of the numbers that
# are greater than the specified limit value.
# The function should take positional arguments *args and
# limit, which will be the limit value.

# Import libraries


# Testing data
g_limit = 4


# Declare function
def sum_of_greater_than(*args, limit: int) -> int:
    """
    Function takes several numbers as arguments and int as limit, as result is sum of all numbers above limit
    :param args: numerical arguments
    :param limit: named argument being bottom limit of numbers taken into account in summary
    :return: conditional sum of numbers sum of numbers
    """
    result = 0
    for number in args:
        if number > limit:
            result += number
    return result


# Print output message
print(f'Answer is {sum_of_greater_than(3, 5, 4, 2, 7, 5, limit=g_limit)}.')

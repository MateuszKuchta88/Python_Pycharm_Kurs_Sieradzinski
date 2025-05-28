# PD5 13 - Sum recursively

# TASK DESCRIPTION
# Write a function that will recursively calculate the sum of all values from 1 to n.
#  for example sum_it(5) will do 5 + 4 + 3 + 2 + 1

# Import libraries


# Testing data
# g_list = [1, 2, 3, -4]


# Declare function
def sum_recursively(number: int) -> int:
    """
    Function takes integer and returns recursive sum of that integer
    :param number: Given integer
    :return: Recursive sum of given integer
    """
    x = 0
    if number > 0:
        x += number + sum_recursively(number - 1)
    return x


# Print output message
print(f'Answer is {sum_recursively(7)}.')

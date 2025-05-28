# PD5 1 - Add lists

# Import libraries

# Get data from user
# given_list1 = list(str(input("\nGive me list of numbers of first list, divided with ',': ")).split(","))
# given_list2 = list(str(input("Give me list of numbers of second list, divided with ',': ")).split(","))

# Testing data
# given_list1 = [2, 4, 6, 5]
# given_list2 = [4, 5, 6]
# print(f'\nLists used in sum: {given_list1}, {given_list2}.')

# Declare variables


# Declare function
def add_lists(list1: list, list2: list) -> list:
    """
    Function returns sum of respective values in two same-sized lists (otherwise returns error message)
    :param list1: First list
    :param list2: Second list, same size as first one
    :return: Sum of corresponding values of two lists, returned as new list (or error message if lists differ in size
    """
    if len(list1) == len(list2):
        new_list = []
        for i in range(len(list1)):
            new_list.append(float(list1[i]) + float(list2[i]))
        return new_list
    else:
        print("Lists have different lengths, please validate them again.")
        quit()


# Call function
# ans = add_lists(list1=given_list1, list2=given_list2)


# Quit if wrong operation

# Process

# Print output message
# print(f'Sum of {given_list1} and {given_list2} is {ans}.')

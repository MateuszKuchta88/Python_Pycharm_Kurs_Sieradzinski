# PD5 3 - Longer than 4, shorter than 8

# TASK DESCRIPTION
# Prepare a function that will filter only words whose length is greater than 4 and less than 8.

# Import libraries

# Welcome message
print('\nWelcome in "Longer than 4, shorter than 8" app.')

# Get data from user
given_list = list(str(input("\nGive me words where I should look for longer than 4 and shorter than 8, divided with ',"
                            "': ")).split(","))

# Testing data
# given_list = ['Andrzejki', 'Szczepan', 'mysz', 'grabiec', 'antracytowy', 'kot']
# print(f'\nList used in filtering is {given_list}.')

# Declare variables


# Declare function
def get_words_4to8(words: list) -> list:
    """
    Function takes list of words and return list of words which are longer than 4 and shorter than 8 characters
    :param words: Given list of words to look for words longer than 4 and shorter than 8
    :return: List of words longer than 4 and shorter than 8 out of given list
    """
    new_list = []
    for word in words:
        if 4 < len(word) < 8:
            new_list.append(word)
    return new_list


# Call function
ans = get_words_4to8(given_list)


# Quit if wrong operation

# Process

# Print output message
print(f'List of words shorter than 8 and longer than 4 out of given list is: {ans}')

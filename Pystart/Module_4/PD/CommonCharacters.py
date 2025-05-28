# PD4 - Common chars of 2 words

# Ask the user for two expressions, then display all characters
# common to both of these expressions. e.g. hall and balcony: should display a and l

# Import libraries

# Welcome message
print('\nWelcome in "Common chars of 2 words" app.\n')

# Get data from user
given_word1 = str(input("Give me first word you would like to process: "))
given_word2 = str(input("Give me second word you would like to process: "))
# given_word1 = "Andrzej"
# given_word2 = "Duda"
print(f'\nFirst word is "{given_word1}" and second one is "{given_word2}".\n')

# Declare variables
common_chars_str = ""

# Quit if wrong operation

# Process
common_chars_list = sorted(set(given_word1.lower()) & set(given_word2.lower()))

# print output message
for letter in common_chars_list:
    common_chars_str += letter if common_chars_str == "" else ", " + letter
print(f'Common characters for those 2 words: {common_chars_str}.')

# PD4 - Strings divided by commas

# Receive comma-separated words from the user, then
# display these words line by line, but each only once.

# Import libraries

# Welcome message
print('\nWelcome in "Strings divided by commas" app.')

# Get data from user
given_strings = str(input("\nGive me first word you would like to process: "))

# Testing data
# given_strings = "apple, banana, cherry, apple, date, banana, elderberry, fig, cherry, grape"
# print(f'\nStrings under process are: "{given_strings}".')

# Declare variables
set_of_strings = set()

# Quit if wrong operation

# Process
strings_list = given_strings.split(",")

# print output message
for word in strings_list:
    set_of_strings.add(word.lstrip().rstrip())
sorted_set_of_strings = sorted(set_of_strings)
print(f'\nStrings you have given are below:')
for string in sorted_set_of_strings:
    print(string)

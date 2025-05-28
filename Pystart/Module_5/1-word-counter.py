# Module 5 - Word counter

# TASK DESCRIPTION
# Prepare a function called word_counter, it should as an argument
# take any text and return the number of words this text contains

# Import libraries

# Welcome message
print('\nWelcome in "Word counter" app.')

# Get data from user
given_text = str(input("\nGive me any text where we should count words: "))

# Testing data
# given_text = "Give me 10 strings, divided by commas, where some of them appear more than one time."
# print(f'\nText under process: "{given_text}".')

# Declare variables


# Declare function
def word_counter(sentence):
    return len(sentence.split(' '))


# Call function
counter = word_counter(given_text)

# Quit if wrong operation

# Process

# Print output message
print(f'Given text contain {counter} words.\n')

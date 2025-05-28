# Module 5 - Return vowels

# TASK DESCRIPTION
# Prepare a function that will receive a word from the user,
# and then it will return the set of vowels found in that word.

# Import libraries

# Welcome message
print('\nWelcome in "Return vowels" app.')

# Get data from user
given_word = str(input("\nGive me any word where we should look for vowels: "))

# Testing data
# given_word = "Antagonistka"
# print(f'\nWord under process: "{given_word}".')

# Declare variables


# Declare function
def check_for_vowels(sentence):
    list_of_vowels = []
    for letter in list(sentence.lower()):
        if letter in ('a', 'e', 'y', 'u', 'i', 'o'):
            list_of_vowels.append(letter)
    return set(list_of_vowels)


# Call function
vowels_set = check_for_vowels(given_word)

# Quit if wrong operation

# Process

# Print output message
print(f'Given word contains these vowels: {vowels_set}.\n')

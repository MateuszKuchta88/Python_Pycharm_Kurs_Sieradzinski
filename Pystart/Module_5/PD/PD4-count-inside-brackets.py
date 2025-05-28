# PD5 4 - Count withing chars

# TASK DESCRIPTION
# Prepare a function that will count the number of characters in the text contained within given chars.
# Chars can appear multiple times in the text, they will never be contained within each other.

# Import libraries

# Welcome message
print('\nWelcome in "Count inside chars" app.')

# Get data from user
given_sentence = str(input("\nGive me a sentence where program should count characters within given characters: "))
given_start = str(input("\nGive me a character for start of 'within' scope: "))
given_end = str(input("\nGive me a character for end of 'within' scope: "))


# Testing data
# given_sentence = '(Ala) ma (kota)'
# given_start = '('
# given_end = ')'
# print(f"\nSentence used in counting between '{given_start}' and '{given_end}' characters is {given_sentence}.")

# Declare variables


# Declare function
def count_chars_between(sentence: str, start: str = '(', end: str = ')') -> int:
    """
    Function takes sentence and start/end of scope and returns number of characters withing start/end of scope
    :param sentence: sentence to process
    :param start: string (preferably one char) for start of scope/counting
    :param end: string (preferably one char) for end of scope/counting
    :return: number of characters within given characters
    """
    counter = 0
    count = False
    for char in list(sentence):
        if char == end:
            count = False
        elif count:
            counter += 1
        elif char == start:
            count = True
    return counter


# Call function
ans = count_chars_between(given_sentence, given_start, given_end)

# Quit if wrong operation

# Process

# Print output message
print(f'In given sentence there is {ans} chars between given characters.')

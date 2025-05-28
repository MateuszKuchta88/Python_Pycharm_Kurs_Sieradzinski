# Find not common part of words and alphabet

# Based on two words, prepare a set of characters that are not for
# them in common.

# Import libraries
import string

# Take two words from user
word_1 = str(input("Give me first word: "))
word_2 = str(input("Give me second word: "))

print(f'First word is {word_1} and second word is {word_2}.')

# Transform given words to sets and check which letters from alphabet are not used in these words
letters_set_1 = set(word_1)
letters_set_2 = set(word_2)
alphabet_set = set(string.ascii_lowercase)
alphabet_without_given_letters = alphabet_set - (letters_set_1 | letters_set_2)

# Print an output
print(f'Part of alphabet, which is not common with these words is: {sorted(alphabet_without_given_letters)}.')

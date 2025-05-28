# PD4 - Check for anagrams

# Prepare a program that will check whether two given words are mutual
# anagrams

# Import libraries

# Welcome message
print('\nWelcome in "Check for anagrams" app.')

# Get data from user
given_word1 = str(input("\nGive me first word you would like to process: "))
given_word2 = str(input("Give me second word you would like to process: "))

# Testing data
# given_word1 = "Astronom"
# given_word2 = "Tronmastatf"
# print(f'\nStrings under process are: "{given_word1} and {given_word2}".')

# Declare variables

# Quit if wrong operation

# Process
word1_set = sorted(set(list(given_word1.lower())))
word2_set = sorted(set(list(given_word2.lower())))

# print output message
if word1_set == word2_set:
    print(f'\nWords "{given_word1}" and "{given_word2}" are anagrams.\n')
else:
    print(f'\nWords "{given_word1}" and "{given_word2}" are not anagrams.\n')

# PD4 - Delete words from sentence

# Write a program that will remove from the text
# all words beginning with selected letter

# Import libraries

# Welcome message
print('Welcome in "Delete words from sentence" app.')

# Get data from user
# given_sentence = str(input("Give me a sentence you would like to process: "))
given_sentence = "Za krótki i zbyt długi sen szkodzi, podobnie jak zbyt wczesne i oczywiście zbyt późne kładzenie się do łóżka. Skutkiem są zakłócenia rytmu dobowego, wahania hormonalne w organizmie, a nawet choroby serca czy depresja. Na szczęście wystarczy zastosować się do rad badaczy."
begin_letter = str(input(f'Give me letter, which words starting with should be removed from text: '))
print(f'Sentence before operation is:\n{given_sentence}')

# Declare variables
new_sentence = ""
given_sentence_words = given_sentence.split(" ")

# Quit if wrong operation
if begin_letter.isalpha() is False:
    print("You should have given me letter!")
    quit()

# Process
for word in given_sentence_words:
    new_sentence += "" if word[0].lower() == begin_letter else word + " "

# print output message
print(f'Here you have your sentence:\n{new_sentence}')

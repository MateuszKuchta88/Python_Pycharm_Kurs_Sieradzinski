# PD8 1 - Hangman

# TASK DESCRIPTION
# Prepare a hangman game with a graphical interface. The game should randomly select one of the words written in the code.
# If the user hits a letter that is in the word, that letter should be unhidden. Otherwise accident,
# he gains another of the letters W-I- S-I-E-L-E-C. The game ends when the user
# guesses the password will complete the entire "HANGED MAN".

# Import libraries
import random


# Functions
def encode_word(word, letters):
    word_encoded = []
    for letter in list(word):
        if letter in letters:
            word_encoded.append(letter)
        else:
            word_encoded.append('-')
    return word_encoded
def encode_hangman(hangman_enc):
    rlp = random.randint(1, 7) - 1
    hangman_encoded_list = list(hangman_enc)
    while hangman_encoded_list[rlp] != '-':
        rlp = random.randint(1, 7) - 1
    hangman_encoded_list[rlp] = list('HANGMAN')[rlp]
    return ''.join(hangman_encoded_list)
def hangman_logic(word, word_enc, hangman_enc):
    print(f"Word to guess ({len(word)} letters): {''.join(word_enc)}")
    print(f'Hangman: {hangman_enc}')
    return str(input('Guess the letter: '))
def print_results(word, word_enc):
    if ''.join(word_enc) == word:
        print('Great!!! You won!!!')
    else:
        print('HANGMAN!!!\nYou lost. Try again!')


# Testing data
word_to_guess = random.choice(['apple', 'pencil', 'computer'])
guessed_letters = []
hangman_encoded = '-------'
word_to_guess_encoded = encode_word(word_to_guess, guessed_letters)


# Operation
while hangman_encoded != 'HANGMAN' and ''.join(word_to_guess_encoded) != word_to_guess:
    given_letter = hangman_logic(word_to_guess, word_to_guess_encoded, hangman_encoded)
    if given_letter in word_to_guess:
        guessed_letters.append(given_letter)
    else:
        hangman_encoded = encode_hangman(hangman_encoded)
    word_to_guess_encoded = encode_word(word_to_guess, guessed_letters)
print_results(word_to_guess, word_to_guess_encoded)

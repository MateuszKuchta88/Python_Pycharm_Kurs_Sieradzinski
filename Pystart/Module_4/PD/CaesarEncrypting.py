# PD4 - Caesar encrypting

# Prepare a program that will encrypt and decrypt expressions
# using the Caesar cipher. Hint: you may find the ord() and chr() functions useful.

# Import libraries

# Welcome message
print('Welcome in Caesar encrypting app.')

# Get data from user
oper = str(input("Do you want to encrypt od decipher?: "))
sentence = str(input(f'Give me a sentence you want to {oper}: '))
param = int(input(f'Give me integer parameter for {oper}ing: '))

# Declare variables
sent_proc = ""
letters = list(sentence)

# Quit if wrong operation
if oper not in ("encrypt", "decipher"):
    quit()

# Process
for letter in letters:
    sent_proc += (chr(ord(letter) + param)) if oper == "encrypt" else (chr(ord(letter) - param))

# print output message
print(f'Here you have your sentence {oper}ed: {sent_proc}')

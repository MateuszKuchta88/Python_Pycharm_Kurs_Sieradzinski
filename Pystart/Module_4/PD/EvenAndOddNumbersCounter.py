# PD4 - Even and Odds Numbers counter

# Write a program that will execute a while loop that will ask questions
# user to enter a number. The program will check whether the number is even and if
# yes, it will add it to the list of even numbers, and if not, then to the list of odd numbers.
# The loop will continue until the user enters the number 0. Once the loop ends
# the program should display the number of even and odd numbers and the list of even numbers
# and odd numbers.

# Import libraries

# Declare variables
even_numbers_set = set()
odd_numbers_set = set()

# Welcome message
print('Welcome in "Even and Odds Numbers counter" app.')

# While loop for operations
print('If you want to finish introducing new numbers put "0" instead of number.')
while 0 == 0:
    number = int(input("Give me number: "))
    if number == 0:
        break
    if number % 2 == 0:
        even_numbers_set.add(number)
    else:
        odd_numbers_set.add(number)

# print goodbye message
print(f'Here you have set of {len(odd_numbers_set)} odd numbers: {odd_numbers_set}')
print(f'Here you have set of {len(even_numbers_set)} even numbers: {even_numbers_set}')

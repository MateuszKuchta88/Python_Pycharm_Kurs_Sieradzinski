# PD7 3 - Write name and surname to txt file

# TASK DESCRIPTION
# Write a program that asks the user for his name
# and saves this information in a text file.

# Import libraries


# Declare function


# Program
with open('name.txt', 'w', encoding='utf8') as handler:
    name = str(input("Give me your name and surname: "))
    handler.write(name)


# Print output message
# print()

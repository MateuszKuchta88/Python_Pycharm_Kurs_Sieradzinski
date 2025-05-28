# Module 7 - Revenue

# TASK DESCRIPTION
# Write a program that will open the file revenues.txt, read the values written in the following lines and display their sum.

# Declare function
with open('revenue.txt', 'r', encoding='utf8') as handler:
    total = 0
    for line in handler:
        total += int(line.strip().split(';')[-1])
    print(f'Sum of revenues is {total}.\n')

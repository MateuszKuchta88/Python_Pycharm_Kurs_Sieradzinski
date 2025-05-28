# Module 7 - Transactions

# TASK DESCRIPTION
# A csv file is a file in which columns are separated by semicolons.
# You can read them using the split function.
# From the transaction.txt file, select only those that have a positive
# value and save them to a separate file called revenue.txt

# Declare function
with open('transakcje.txt', 'r', encoding='utf8') as handler, open('revenue.txt', 'w', encoding='utf8') as new_file:
    for line in handler:
        transaction_date, title, value = line.strip().split(';')
        if int(value) > 0:
            print(line.strip().split(';'))
            new_file.write(f'{transaction_date};{title};{value}\n')

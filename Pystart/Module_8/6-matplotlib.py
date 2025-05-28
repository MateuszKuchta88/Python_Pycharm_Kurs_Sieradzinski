# Module 8 - Plot some data

# TASK DESCRIPTION
# Open the operations.csv file attached to the task. Calculate the value of income for
# individual months, and then create a chart presenting your income for these months.
# Create a second chart illustrating the number of operations performed in individual months.
# Save both charts in the directory under the names “summary.png” and “ilosc_operacji.png”

# Import libraries
import csv
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np

# Testing data


# Declare function
with open('operacje.csv', newline='', encoding='utf8') as csvfile:
    # c_names = ['data', 'rodzaj operacji', 'opis operacji', 'kwota operacji']
    reader = csv.DictReader(csvfile, delimiter=',')
    balance = {}
    nof_operations = {}
    for row in reader:
        operation_month = datetime.strptime(row['data'], '%Y-%m-%d').strftime('%b')
        if row['rodzaj operacji'] == 'przychód':
            balance[operation_month] = balance.get(operation_month, 0) + int(row['kwota operacji'])
        elif row['rodzaj operacji'] == 'wydatek':
            balance[operation_month] = balance.get(operation_month, 0) - int(row['kwota operacji'])
        nof_operations[operation_month] = nof_operations.get(operation_month, 0) + 1


fig1, ax1 = plt.subplots()
months = balance.keys()
revenue = balance.values()
ax1.bar(months, revenue)
ax1.set_xlabel('Months')
ax1.set_ylabel('Balance')
plt.savefig('podsumowanie.png')

fig2, ax2 = plt.subplots()
months = nof_operations.keys()
count = nof_operations.values()
ax2.bar(months, count)
ax2.set(xlabel='Months', ylim=(0, 10), yticks=np.arange(1, 10))
ax2.set_ylabel('Number of operations')
plt.savefig('ilosc_operacji.png')

# Tests


# Print output message

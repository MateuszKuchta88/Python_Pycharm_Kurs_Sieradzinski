# PD7 1 - Current date

# TASK DESCRIPTION
# Write a program that will display the current date and time in the format "dd/mm/yyyy,
# hour:minute:second".

# Import libraries
from datetime import datetime


# Program
print(datetime.today().strftime('%d/%m/%Y, %H:%M:%S'))

# Print output message
# print()

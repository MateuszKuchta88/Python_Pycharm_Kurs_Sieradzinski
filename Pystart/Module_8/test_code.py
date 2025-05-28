# Import libraries
from datetime import date, datetime

# Testing data


# Declare function
birthday = "20-01-1998"
today = date.today()
birth_this_year = datetime.strptime(birthday, "%d-%m-%Y")


# Tests
# Print output message
print(f'Answer is {birth_this_year}.')

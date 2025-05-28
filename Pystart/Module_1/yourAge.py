# This is script to process given age of born
from datetime import datetime
current_date_and_time = datetime.now()
birth_year = int(input('Input year you were born in: '))
age = current_date_and_time.year - birth_year

print(f'You are {age} years old.')

if(age >= 18):
    print('You are adult.')

if(birth_year % 4 == 0):
    if(birth_year % 100 == 0):
        if(birth_year % 400 == 0):
            print('You were born in leap year.')
        else:
            print('You were not born in leap year.')
    else:
        print('You were born in leap year.')
else:
    print('You were not born in leap year.')



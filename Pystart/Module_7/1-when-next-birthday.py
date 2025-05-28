# Module 7 - When is your next birthday

# TASK DESCRIPTION
# Prepare a program that will display the date of your next birthday and
# will answer the question of how many days you have to wait for them.
# If your birthday has already passed in a given year, it should appear
# date in the following year.

# Import libraries
from datetime import date, datetime


# Testing data


# Declare function
def when_next_birthday(birthday: str) -> str:
    today = date.today()
    birthday_datetime = datetime.strptime(birthday, '%d-%m-%Y')
    birthday_this_year = date(today.year, birthday_datetime.month, birthday_datetime.day)
    birthday_this_year_str = datetime.strftime(date(today.year, birthday_datetime.month, birthday_datetime.day), '%d-%m-%Y')
    if birthday_this_year > today:
        return birthday_this_year_str
    else:
        return datetime.strftime(date(today.year + 1, birthday_datetime.month, birthday_datetime.day), '%d-%m-%Y')


def how_long_till_next_birthday(birthday: str) -> int:
    next_birthday_datetime = datetime.strptime(when_next_birthday(birthday), '%d-%m-%Y')
    next_birthday = date(next_birthday_datetime.year,
                         next_birthday_datetime.month,
                         next_birthday_datetime.day)
    return (next_birthday - date.today()).days


# Tests
def test_when_next_birthday():
    assert when_next_birthday('20-01-1998') == "20-01-2025"
    assert when_next_birthday('10-09-1998') == "10-09-2024"


def test_how_long_till_next_birthday():
    assert how_long_till_next_birthday('20-10-1998') == 41
    assert how_long_till_next_birthday('10-09-1998') == 1

# Print output message

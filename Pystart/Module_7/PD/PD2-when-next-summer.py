# PD7 2 - When next summer starts

# TASK DESCRIPTION
# Write a program that will display how many days are left until next summer (June 21).
# Take into account the situation when the date is ahead and behind us.

# Import libraries
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


# Declare function
def when_next_summer():
    today = date.today()
    summer_begin_datetime = datetime.strptime('20-01-1998', '%d-%m-%Y')
    summer_this_year = date(today.year,
                            summer_begin_datetime.month,
                            summer_begin_datetime.day)
    summer_this_year_str = datetime.strftime(date(today.year,
                                                  summer_begin_datetime.month,
                                                  summer_begin_datetime.day),
                                             '%d-%m-%Y')
    if summer_this_year > today:
        return summer_this_year_str
    else:
        return datetime.strftime(date(today.year + 1,
                                      summer_begin_datetime.month,
                                      summer_begin_datetime.day),
                                 '%d-%m-%Y')


# Program
next_summer_datetime = datetime.strptime(when_next_summer(), '%d-%m-%Y')
next_summer = date(next_summer_datetime.year,
                   next_summer_datetime.month,
                   next_summer_datetime.day)
last_summer = next_summer - relativedelta(years=1)


# Print output message
print(f'Next summer will be in {(next_summer - date.today()).days} days.')
print(f'Last summer was {(date.today() - last_summer).days} days ago.')

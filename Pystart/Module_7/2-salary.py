# Module 7 - Count salary

# TASK DESCRIPTION
# Ask the user for a start date, end date, a nd
# also about his daily wage. It should appear in response
# information on how much the user will earn.
# Double count an employee's pay for working on Saturdays
# and Sundays.

# Import libraries
from datetime import datetime, timedelta


# Testing data


# Declare function
def count_salary(start: str, end: str, wage: float) -> float:
    start_datetime = datetime.strptime(start, '%d-%m-%Y')
    end_datetime = datetime.strptime(end, '%d-%m-%Y')
    return (end_datetime - start_datetime + timedelta(days=1)).days * wage


def count_salary_with_weekend_bonus(start: str, end: str, wage: float) -> float:
    start_datetime = datetime.strptime(start, '%d-%m-%Y')
    end_datetime = datetime.strptime(end, '%d-%m-%Y')
    count_day = start_datetime
    salary = 0
    while end_datetime - count_day >= timedelta(days=0):
        if datetime.strftime(count_day, '%a') in ('Sat', 'Sun'):
            salary += 2 * wage
        else:
            salary += wage
        count_day += timedelta(days=1)
    return salary


# Tests
def test_count_salary():
    assert count_salary('20-01-1998', '23-01-1998', 100) == 400
    assert count_salary('20-12-2023', '10-03-2024', 25) == 2050


def test_count_salary_with_weekend_bonus():
    assert count_salary_with_weekend_bonus('20-01-2024', '23-01-2024', 100) == 600
    assert count_salary_with_weekend_bonus('20-12-2023', '10-03-2024', 25) == 2650

# Print output message

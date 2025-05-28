# PD9 1 - Employee class

# TASK DESCRIPTION
# Create a BaseEmployee class to store the name, surname and date of employment.
# If the user provides a date later than today's date or indicating a working time longer than 50 years, throw it away
# InvalidDateOfEmployment exception. Add special methods to sort by length employment
# Create a get_employment_time method in the BaseEmployee class. This method should return every time
# information on how many days a given employee works (from the beginning)
# Create an Employee class that will inherit from the BaseEmployee class, this class
# should have an hourly rate, full-time employment (e.g. full-time is 160 hours),
# and the value of the employee's bonus. Prepare a method to calculate its value remuneration

# Import libraries
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Code
class InvalidDateOfEmployment(Exception):
    pass


class BaseEmployee:
    def __init__(self, first_name: str, last_name: str, date_of_employment: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_employment = date_of_employment
        try:
            self.date_of_employment_datetime = datetime.strptime(self.date_of_employment, '%Y-%m-%d')
        except ValueError:
            raise ValueError("!!!ERROR!!! Check input data again - probably you gave the wrong date format (it has to be YYYY-MM-DD)")
        try:
            if not self.date_of_employment_datetime <= datetime.today():
                raise InvalidDateOfEmployment()
        except InvalidDateOfEmployment:
            raise InvalidDateOfEmployment("He\She couldn't have been employed in future!")
        try:
            if not self.date_of_employment_datetime > datetime.today() - relativedelta(years=50):
                raise InvalidDateOfEmployment()
        except InvalidDateOfEmployment:
            raise InvalidDateOfEmployment("It's not possible he\she was employed more than 50 years ago!")

    def __repr__(self):
        return f"Base employee {self.first_name} {self.last_name}, employed since {self.date_of_employment}."

    def get_employment_time(self):
        return (datetime.today() - datetime.strptime(self.date_of_employment, '%Y-%m-%d')).days


class Employee(BaseEmployee):
    def __init__(self, first_name: str, last_name: str, date_of_employment: str, hourly_rate: float, monthly_workload: int = 160, bonus: int = 0):
        super().__init__(first_name, last_name, date_of_employment)
        self.hourly_rate = hourly_rate
        self.monthly_workload = monthly_workload
        self.bonus = bonus

    def get_salary(self):
        return self.hourly_rate * self.monthly_workload + self.bonus


# Example usage
try:
    x = BaseEmployee("Mateusz", "Kuchta", "2026/01/01")  # Invalid format
    print(x, ' ', x.get_employment_time())
except ValueError as e:
    print(e)
except InvalidDateOfEmployment as e:
    print(e)

try:
    x = BaseEmployee("Mateusz", "Kuchta", "2024-01-01")
    print(x, ' ', x.get_employment_time())
except ValueError as e:
    print(e)
except InvalidDateOfEmployment as e:
    print(e)

try:
    x = BaseEmployee("Mateusz", "Kuchta", "1924-01-01")
    print(x, ' ', x.get_employment_time())
except ValueError as e:
    print(e)
except InvalidDateOfEmployment as e:
    print(e)

try:
    x = BaseEmployee("Mateusz", "Kuchta", "2026-01-01")
    print(x, ' ', x.get_employment_time())
except ValueError as e:
    print(e)
except InvalidDateOfEmployment as e:
    print(e)

try:
    x = Employee("Mateusz", "Kuchta", "2024-01-01", 50, 160, 400)
    print(x, ' ', x.get_employment_time(), ' ', x.get_salary())
except ValueError as e:
    print(e)
except InvalidDateOfEmployment as e:
    print(e)

# Tests
def test_base_employee():
    assert BaseEmployee("Mateusz", "Kuchta", "2024-01-01") == str('Base employee Mateusz Kuchta, employed since 2024-01-01 sucessfully created!')

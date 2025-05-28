from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytest

# Custom Exception
class InvalidDateOfEmployment(Exception):
    """Raised when the provided date of employment is invalid."""
    pass

# BaseEmployee Class
class BaseEmployee:
    """
    A class representing a base employee.

    Attributes:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        date_of_employment (str): The date the employee was employed in 'YYYY-MM-DD' format.
    """

    def __init__(self, first_name: str, last_name: str, date_of_employment: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_employment = date_of_employment

        try:
            self.date_of_employment_datetime = datetime.strptime(self.date_of_employment, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

        if self.date_of_employment_datetime > datetime.today():
            raise InvalidDateOfEmployment("Employment date cannot be in the future.")

        if self.date_of_employment_datetime <= datetime.today() - relativedelta(years=50):
            raise InvalidDateOfEmployment("Employment date cannot be more than 50 years in the past.")

    def __repr__(self):
        return f"Base employee {self.first_name} {self.last_name}, employed since {self.date_of_employment}."

    def get_employment_time(self) -> int:
        """
        Calculate the number of days the employee has been employed.

        Returns:
            int: Number of days since employment.
        """
        return (datetime.today() - self.date_of_employment_datetime).days

# Employee Class
class Employee(BaseEmployee):
    """
    A class representing an employee, inheriting from BaseEmployee.

    Attributes:
        hourly_rate (float): The employee's hourly rate.
        monthly_workload (int): The number of hours the employee works per month.
        bonus (int): The employee's monthly bonus.
    """

    def __init__(self, first_name: str, last_name: str, date_of_employment: str, hourly_rate: float, monthly_workload: int = 160, bonus: int = 0):
        super().__init__(first_name, last_name, date_of_employment)
        self.hourly_rate = hourly_rate
        self.monthly_workload = monthly_workload
        self.bonus = bonus

    def get_salary(self) -> float:
        """
        Calculate the employee's monthly salary.

        Returns:
            float: Total monthly salary including bonus.
        """
        return self.hourly_rate * self.monthly_workload + self.bonus

# Example Usage
if __name__ == "__main__":
    try:
        emp = Employee("John", "Doe", "2020-05-01", 20.0, 160, 500)
        print(emp)
        print(f"Employment time (days): {emp.get_employment_time()}")
        print(f"Monthly salary: {emp.get_salary()} USD")
    except Exception as e:
        print(f"Error: {e}")

# Unit Tests
def test_base_employee_valid():
    emp_test = BaseEmployee("Jane", "Doe", "2015-06-15")
    assert emp_test.get_employment_time() > 0
    assert "Jane" in repr(emp_test)

def test_base_employee_invalid_future_date():
    with pytest.raises(InvalidDateOfEmployment):
        BaseEmployee("Future", "Person", "2050-01-01")

def test_base_employee_invalid_past_date():
    with pytest.raises(InvalidDateOfEmployment):
        BaseEmployee("Old", "Timer", "1900-01-01")

def test_employee_salary():
    emp_test = Employee("Sam", "Smith", "2018-03-01", 25.0, 160, 300)
    assert emp_test.get_salary() == 25.0 * 160 + 300
    assert emp_test.get_employment_time() > 0

if __name__ == "__main__":
    pytest.main(["-v", __file__])

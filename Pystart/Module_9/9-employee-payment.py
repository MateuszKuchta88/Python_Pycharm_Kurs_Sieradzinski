# Module 9 - Employee payment

# TASK DESCRIPTION
# Prepare an Employee class that will receive the name in the init,
# name and hourly rate. Prepare a Manager class that
# will inherit from the Employee class, whose every working hour
# will be counted twice, and there will be an additional option to specify
# manager bonus(add_bonus(amount: int)).

# Import libraries


# Declare function

class Employee:
    def __init__(self, first_name: str = 'Employee_name', last_name: str = 'Employee_surname', hourly_rate: float = 20, bonus: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.hourly_rate_employee = hourly_rate
        self.bonus = bonus
        self.working_time = 0

    def add_time(self, time_in_h: float = 168):
        self.working_time += time_in_h

    def reset_time(self):
        self.working_time = 0

    def get_salary(self) -> float:
        return self.hourly_rate_employee * self.working_time + self.bonus

class Manager(Employee):
    def __init__(self, salary_multiplier: float = 2):
        super().__init__()
        self.salary_multiplier = salary_multiplier
        self.hourly_rate_employee = self.hourly_rate_employee * self.salary_multiplier

    def add_bonus(self, amount: int = 100):
        self.bonus = amount

# Tests


# Print output message

# Module 9 - Bank account

# TASK DESCRIPTION
# Prepare a BankAccount class that will allow you to deposit
# and withdraw funds. Create a savings account class
# SavingsAccount, which will inherit from BankAccount and enable
# increasing your account balance by a percentage of interest.

# Import libraries


# Declare function

class BankAccount:
    def __init__(self, initial_balance: float = 0):
        self._balance = initial_balance

    def deposit(self, amount_to_deposit: float):
        self._balance += amount_to_deposit

    def withdraw(self, amount_to_withdraw: float):
        if self._balance >= amount_to_withdraw:
            self._balance -= amount_to_withdraw
        else:
            return f"You don't have such amount of money on your account."

    def account_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self, increase_percentage: int = 4):
        super().__init__()
        self.increase_percentage = increase_percentage

    def increase_savings(self):
        self.deposit(self._balance * self.increase_percentage / 100)

# Tests
def test_account():
    account = BankAccount()
    account.deposit(10000)
    account.withdraw(2000)
    assert account.account_balance() == 8000
    assert account.withdraw(9000) == f"You don't have such amount of money on your account."

    account = BankAccount(3000)
    account.deposit(1000)
    account.withdraw(2000)
    assert account.account_balance() == 2000
    assert account.withdraw(3000) == f"You don't have such amount of money on your account."

def test_savings_account():
    account = SavingsAccount()
    account.deposit(10000)
    account.increase_savings()
    assert account.account_balance() == 10400

    account = SavingsAccount(2)
    account.deposit(10000)
    account.increase_savings()
    assert account.account_balance() == 10200


# Print output message

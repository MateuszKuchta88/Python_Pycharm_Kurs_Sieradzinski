# Module 9 - Bank account (gpt modified)

# TASK DESCRIPTION
# Prepare a BankAccount class that will allow you to deposit
# and withdraw funds. Create a savings account class
# SavingsAccount, which will inherit from BankAccount and enable
# increasing your account balance by a percentage of interest.

# Import libraries


# Declare function

class BankAccount:
    """
    A class representing a generic bank account.

    Attributes:
        _balance (float): The current balance of the account.
    """

    def __init__(self, initial_balance: float = 0):
        """
        Initialize the bank account with an optional initial balance.

        Args:
            initial_balance (float): The starting balance. Defaults to 0.
        """
        self._balance = initial_balance

    def deposit(self, amount: float):
        """
        Deposit a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float):
        """
        Withdraw a specified amount from the account if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            str: An error message if insufficient funds are available.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self._balance >= amount:
            self._balance -= amount
        else:
            return "Insufficient funds."

    def get_balance(self) -> float:
        """
        Retrieve the current account balance.

        Returns:
            float: The current balance.
        """
        return self._balance


class SavingsAccount(BankAccount):
    """
    A class representing a savings account, inheriting from BankAccount.

    Attributes:
        _interest_rate (float): The percentage rate used to increase the account balance.
    """

    def __init__(self, initial_balance: float = 0, interest_rate: float = 4):
        """
        Initialize the savings account with an optional initial balance and interest rate.

        Args:
            initial_balance (float): The starting balance. Defaults to 0.
            interest_rate (float): The interest rate as a percentage. Defaults to 4.
        """
        super().__init__(initial_balance)
        if interest_rate <= 0:
            raise ValueError("Interest rate must be positive.")
        self._interest_rate = interest_rate

    def apply_interest(self):
        """
        Increase the account balance by the specified interest rate.
        """
        self.deposit(self._balance * self._interest_rate / 100)


# Test functions

def test_account():
    """Test the BankAccount class functionality."""
    account = BankAccount()
    account.deposit(10000)
    account.withdraw(2000)
    assert account.get_balance() == 8000
    assert account.withdraw(9000) == "Insufficient funds."

    account = BankAccount(3000)
    account.deposit(1000)
    account.withdraw(2000)
    assert account.get_balance() == 2000
    assert account.withdraw(3000) == "Insufficient funds."

    try:
        account.deposit(-500)
    except ValueError as e:
        assert str(e) == "Deposit amount must be positive."

    try:
        account.withdraw(-100)
    except ValueError as e:
        assert str(e) == "Withdrawal amount must be positive."

def test_savings_account():
    """Test the SavingsAccount class functionality."""
    account = SavingsAccount(initial_balance=10000)
    account.apply_interest()
    assert account.get_balance() == 10400

    account = SavingsAccount(initial_balance=10000, interest_rate=2)
    account.apply_interest()
    assert account.get_balance() == 10200

    try:
        SavingsAccount(initial_balance=1000, interest_rate=-5)
    except ValueError as e:
        assert str(e) == "Interest rate must be positive."

# Run tests
if __name__ == "__main__":
    test_account()
    test_savings_account()
    print("All tests passed successfully.")

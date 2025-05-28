# PD4 - ATM simulator

# Write a program simulating the operation of an ATM. The while loop will ask
# the user to select an operation (e.g. deposit, withdrawal, checking the account balance) and it will be done
# continues until the user selects "exit".

# Import libraries
import time

# Welcome message
print("Welcome in ATM.")

# Initiate balance and operation variables
balance = 1000
operation = "c"

# While loop for operations
while operation != "e":
    operation = str(input("What would you like to do: d - deposit; w - withdrawal; c - check the balance; e - exit: "))
    if operation == "d":
        given_money = int(input("How much money you would like to add to your balance: "))
        print("Give me money!")
        balance += given_money
        time.sleep(3)  # Sleep for 3 seconds
        print("Thank you, money has been added to you balance.")
    elif operation == "w":
        withdraw_amount = int(input("How much money you would like to withdraw?: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            time.sleep(3)  # Sleep for 3 seconds
            print(f'Here is your {withdraw_amount} $.')
        else:
            print("You don't have such amount of money on your deposit!")
    elif operation == "c":
        print(f'Your balance is: {balance} $.')

# print goodbye message
print("Thank you for using out ATM!")

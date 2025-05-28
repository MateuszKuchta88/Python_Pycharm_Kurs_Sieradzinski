# PD4 - Password validator

# Define the password in a variable and then write a program that loops through it
# while will prompt the user to enter a password. If the password is correct, the program
# should display the message "Correct password" and if the password is incorrect, the program
# it should display the message "Incorrect password, please try again".

# Define hidden password
password = "Smacznej88@"

# Define auxiliary variable
valid = None

# Take given password from user and check if it's valid
while valid is None:
    password_input = str(input("Enter password: "))
    if password_input == password:
        valid = True
    else:
        print("Incorrect password, please try again")

# print that password is correct
print("Correct password")

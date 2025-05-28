# Project 2 - PESEL number check

# Write a program that will check whether the PESEL number provided by the user is correct

# Take PESEL number from user a make a list of digits out of it
pesel_list = list(str(input("Give me your PESEL number: ")))

# Create list of multiplying factors
multiplier_list = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]

# Initiate var to store total sum of PESEL digits multiplied by factor from multiplier_list
total = 0

for i in range(0, len(pesel_list)):
    total += int(pesel_list[i]) * multiplier_list[i]

print(total) if total % 10 == 0 else print("issue")

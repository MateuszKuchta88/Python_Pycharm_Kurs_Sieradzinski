# Months with Dictionary

#Write a program that will accept the month as an integer from
#user (e.g. 1 for January, 2 for February, etc.) and displayed the name of the month
#corresponding to this number. You can approach this task using match
#or use a dictionary.

#Read number indicating month given by user
month_from_user = int(input("Give me month, where 1 means January, 2 February etc.:"))

#Build dictionary with months
months = {1 : "January", 2 : "February", 3 : "March", 4 : "April",
          5 : "May", 6 : "June", 7 : "July", 8 : "August",
          9 : "September", 10 : "October", 11 : "November", 12 : "December"}

#Conditional for input other that int 1-12 and output
if month_from_user in tuple(range(1, 13)):
    print(f'"Month is {months[month_from_user]}."')
else:
    print(f'"Month is not known."')
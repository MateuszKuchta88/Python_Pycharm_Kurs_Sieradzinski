# Match case

#Write a program that will accept the month as an integer from
#user (e.g. 1 for January, 2 for February, etc.) and displayed the name of the month
#corresponding to this number. You can approach this task using match
#or use a dictionary.

#Read number indicating month given by user
month_from_user = int(input("Give me month, where 1 means January, 2 February etc.:"))

#match case which converts int to month_name
match month_from_user:
    case 1:
        month_name = "January"
    case 2:
        month_name = "February"
    case 3:
        month_name = "March"
    case 4:
        month_name = "April"
    case 5:
        month_name = "May"
    case 6:
        month_name = "June"
    case 7:
        month_name = "July"
    case 8:
        month_name = "August"
    case 9:
        month_name = "September"
    case 10:
        month_name = "October"
    case 11:
        month_name = "November"
    case 12:
        month_name = "December"
    case _:
        month_name = "not known"

print(f'"Chosen month is {month_name}."')
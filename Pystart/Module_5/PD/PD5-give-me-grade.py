# PD5 5 - Give me grade

# TASK DESCRIPTION
# Prepare a function that will take the percentage of points scored from the user, in
# response will return the grade the user received

# Import libraries

# Welcome message
print('\nWelcome in "Give me grade" app.')

# Get data from user
given_percentage = float(input("\nGive me percentage of points you scored: "))

# Testing data
# given_percentage = 56
# print(f"\nUser received {given_percentage}%.")

# Declare variables


# Declare function
def give_me_grade(percentage: float) -> str:
    """
    Function takes percentage as float and returns grade received from exam
    :param percentage: percentage of points scored from exam
    :return: grade as string
    """
    if percentage < 45:
        return 'niedostateczny'
    elif percentage < 55:
        return 'dopuszczający'
    elif percentage < 80:
        return 'dostateczny'
    elif percentage < 90:
        return 'dobry'
    elif percentage < 95:
        return 'bardzo dobry'
    else:
        return 'celujący'


# Call function
ans = give_me_grade(given_percentage)


# Quit if wrong operation

# Process

# Print output message
print(f'{given_percentage}% will give grade "{ans}".')

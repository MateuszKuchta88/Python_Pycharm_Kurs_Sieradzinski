# Module 5 - Count numbers

# TASK DESCRIPTION
# Prepare a function whose declaration will look like this:
# def count_numbers(numbers:list, count_odd:bool = True, count_even:bool = True):
# The purpose of the function will be to answer the question of how many numbers there are
# that meet the requirements specified in the arguments in the list
# transferred in the first interval.

# Import libraries

# Welcome message
print('\nWelcome in "Count numbers" app.')

# Get data from user
given_list = list(str(input("\nGive me list of numbers to process, divided with with ',': ")).split(","))
given_count_odd = str(input("Do you want to count odd numbers? (True/False): "))
given_count_even = str(input("Do you want to count even numbers? (True/False): "))

# Testing data
# given_list = [4, 75, 54, 23, 0, 52]
# print(f'\nList of numbers where odd and even numbers will be counted is: {given_list}.')

# Declare variables
# given_count_odd = True
# given_count_even = True


# Declare function
def count_numbers(numbers: list, count_odd: str = True, count_even: str = True) -> int:
    """
    Function used to sum either odd, or even numbers of given list
    :param numbers: List of numbers to process
    :param count_odd: Bool-like value to define if number of odd numbers should be returned
    :param count_even: Bool-like value to define if number of even numbers should be returned
    :return: Integer(s) in sentence are returned
    """
    nof_evens = 0
    nof_odds = 0
    if count_even == "True":
        if count_odd == "True":
            for number in numbers:
                if int(number) % 2 == 0:
                    nof_evens += 1
                else:
                    nof_odds += 1
            print(f'\nThere are {nof_evens} even numbers and {nof_odds} odd numbers in list {numbers}.')
            return 0
        else:
            for number in numbers:
                if int(number) % 2 == 0:
                    nof_evens += 1
            print(f'\nThere are {nof_evens} even numbers in list {numbers}.')
            return 0
    else:
        if count_odd == "True":
            for number in numbers:
                if int(number) % 2 == 1:
                    nof_odds += 1
            print(f'\nThere are {nof_odds} odd numbers in list {numbers}.')
            return 0
        else:
            print("\nNo calculation was done as requested.")
            return 0


# Call function
count_numbers(numbers=given_list, count_odd=given_count_odd, count_even=given_count_even)
# count_numbers(numbers=given_list, count_even=False)
# count_numbers(numbers=given_list, count_odd=False)
# count_numbers(numbers=given_list)

# Quit if wrong operation

# Process

# Print output message
# print(f'Factorial of {given_number} is {answer}.')

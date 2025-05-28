# PD5 14 - check PIN

# TASK DESCRIPTION
# The PIN can only consist of four digits. Write a function that returns true
# or false depending on whether this requirement is met.

# Import libraries


# Testing data
g_pin = '5099'


# Declare function
def check_pin(pin: str) -> bool:
    """
    Function takes given string and checks if it can be PIN (4 digits)
    :param pin: given string to be checked if it's pin
    :return: Bool value if it's PIN
    """
    for char in pin:
        if not char.isdigit():
            return False
    if len(pin) == 4:
        return True
    else:
        return False


# Print output message
print(f'Answer is {check_pin(g_pin)}.')

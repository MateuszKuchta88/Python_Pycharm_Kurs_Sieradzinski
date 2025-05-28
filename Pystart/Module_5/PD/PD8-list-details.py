# PD5 8 - List details

# TASK DESCRIPTION
# Prepare a function that will return a dictionary containing:
#  total - number of elements
#  mean - the average of elements
#  max - the highest value
#  min - the smallest value

# Import libraries


# Testing data
given_list = [3, 6, 34, 65, 12]


# Declare variables


# Declare function
def list_details(g_list: list) -> dict:
    """
    Funtion takes list of floats and returns it basic details: size, min value, max value and average of values
    :param g_list: given list of values
    :return: dictionary with details
    """
    return {"total": len(g_list), "mean": sum(g_list)/len(g_list), "min": min(g_list), "max": max(g_list)}


# Process

# Print output message
print(f'Answer is {list_details(given_list)}')

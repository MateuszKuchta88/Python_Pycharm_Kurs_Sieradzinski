# PD5 7 - Miles \ Kilometers conversion

# TASK DESCRIPTION
# Prepare a function to convert the units: miles to kilometers and
# the second one converting kilometers to miles

# Import libraries


# Testing data
miles_km = 10
km_miles = 100


# Declare variables


# Declare function
def miles_km_convert(value: float, miles_to_km: bool = True) -> float:
    """
    Function takes value in km or miles and converts it to miles or kilometers, based on declaration
    :param value: distance to convert
    :param miles_to_km: logical indication if given value is in miles and should be converted to km; otherwise km->miles
    :return: converted value
    """
    miles_to_km_factor = 1.609344
    km_to_miles_factor = 1/1.609344
    result = miles_to_km_factor * value if miles_to_km else km_to_miles_factor * value
    return result


# Process

# Print output message
print(f'Answer is {miles_km_convert(miles_km, False):.3f}')

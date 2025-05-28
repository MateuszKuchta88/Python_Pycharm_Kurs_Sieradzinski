# PD6 2 - budget

# TASK DESCRIPTION
# The "ecommerce" module is to have the calculate_brutto and calculate_netto functions
#  with the VAT value equal to 0.23 by default, as well as the calculate_discount function,
#  which will receive a list of discounts, e.g. 0.1, 0.2, 0.3 and will be able to subtract them as
#  percentages.
# Remember about testing!

# Import libraries


# Declare function(s)
def calculate_brutto(value: float, vat: float = 0.23) -> float:
    if 1 > vat >= 0:
        return value / (1 - vat)
    else:
        return -1


def calculate_netto(value: float, vat: float = 0.23) -> float:
    if 1 >= vat >= 0:
        return value * (1 - vat)
    else:
        return -1


def calculate_rabat(discounts: list) -> float:
    output = 1
    for discount in discounts:
        if 1 >= discount >= 0:
            output = output * (1 - discount)
        else:
            return -1
    return output

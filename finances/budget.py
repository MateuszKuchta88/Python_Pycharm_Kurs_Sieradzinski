# PD6 2 - budget

# TASK DESCRIPTION
# The "budget" module has a calculate_expences(expences:list) function that sums up the list of expenses
# and calculate_monthly_budget(total_income, total_expences)
# Remember about testing!

# Import libraries


# Declare function(s)
def calculate_expences(expences: list):
    total = 0
    items = {"glass": 2.15,
             "fan": 6.2,
             "fork": 1.05,
             "plate": 4.35}
    for e in expences:
        if e in items.keys():
            total += items[e]
        else:
            return f"There is sth wrong in your basket. We don't have {e} in our store"
    return total


def calculate_monthly_budget(total_income, total_expences):
    return total_income - total_expences

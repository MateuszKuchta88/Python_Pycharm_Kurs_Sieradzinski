# Module 9 - Index error

# TASK DESCRIPTION
# Prepare a list that contains 10 items. Ask the user which one
# values should be returned. If the user references the value
# which does not exist (IndexError), then display a message that there is no such value
# has.

# Import libraries


# Declare function

x = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
i = int(input("Which element of prepared list should be returned: "))
try:
    print(x[i - 1])
except IndexError:
    print(f"Prepared list has only {len(x)} elements.")

# Tests


# Print output message

# Module 9 - Dictionary error

# TASK DESCRIPTION
# Prepare a dictionary containing 3 values. Check what happens if
# you try to reference a key that does not exist in this dictionary. Try it
# handle such a situation by catching such an exception

# Import libraries


# Declare function

x = {'key1': 1, 'key2': 2, 'key3': 3}
i = str(input("Which element of prepared dictionary should be returned: "))
try:
    print(x[i])
except KeyError:
    print(f"Prepared dictionary does not contain such key.")

# Tests


# Print output message

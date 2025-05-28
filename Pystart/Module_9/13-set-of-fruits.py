# Module 9 - Dictionary error

# TASK DESCRIPTION
# Ask the user for the names of 10 fruits if the fruit is already there
# list, an exception should be thrown and the program should stop asking.

# Import libraries


# Declare function
s = []
try:
    while len(s) < 10:
        i = str(input(f"Give me {10 - len(s)} fruits you have not given yet: "))
        for fruit in s:
            if not fruit != i:
                raise Exception('You gave this fruit already.')
        s.append(i)
    print(s)
except Exception as e:
    print(e)

# Tests


# Print output message

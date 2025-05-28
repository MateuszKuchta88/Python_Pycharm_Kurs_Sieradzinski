# Module 9 - Dictionary error

# TASK DESCRIPTION
# Ask the user for any text the user would like to reverse
# (Display from end to beginning).
# If the user provides an empty string, an exception should be thrown.

# Import libraries


# Declare function
while True:
    try:
        i = str(input("Which text would you like to reverse: "))
        if i == '':
            raise Exception('You gave an empty string! Try again!')
        print(i[::-1])
    except Exception as e:
        print(e)

# Tests


# Print output message

# Module 5 - Repeat with delimiter

# TASK DESCRIPTION
# Write a function that takes one positional argument (text) and
# two named arguments (delimiter and repeat) with defaults
# with the values "," and 1. The function should return repeated text
# appropriate number of times and separated by the given delimiter.

# Import libraries

# Welcome message
print('\nWelcome in "Repeat with delimiter" app.')

# Get data from user
g_text = str(input("\nGive me text you want to repeat: "))

print("\nGive me delimiter you want to use to divide repeated strings, "
      "if you want to have it different than default (default = ',').")
g_delimit = str(input("If you want it to remain default, just click Enter: "))

print("\nGive me number of times you want to repeat given text, "
      "if you want to have it different than default (default = 1).")
nof_reps = str(input("If you want it to remain default, just click Enter: "))


# Testing data
# g_text = 'Simple text'
# g_delimit= ','
# nof_reps = 3
# print(f'\nProgram will give you text {g_text} repeated {nof_reps} times delimited with "{g_delimit}".\n')

# Declare variables


# Declare function
def repeat(text, delimit=',', reps='1'):
    result = []
    for _ in range(int(reps)):
        result.append(text)
    return delimit.join(result)


# Call function
if g_delimit:
    ans = repeat(text=g_text, delimit=g_delimit, reps=nof_reps) if nof_reps else repeat(text=g_text, delimit=g_delimit)
else:
    ans = repeat(text=g_text, reps=nof_reps) if nof_reps else repeat(text=g_text)

# Quit if wrong operation

# Process

# Print output message
print(f'\nResult of operation is "{ans}".\n')

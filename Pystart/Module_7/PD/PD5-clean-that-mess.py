# PD7 5 - Write name and surname to txt file

# TASK DESCRIPTION
# There are many lines in the balagan.txt file containing the phrase "Java" and "Java Script".
# Replace all Java expressions with Python, and lines containing Java Script
# leave line unchanged.

# Import libraries

# Declare function

# Program
with open('balagan1.txt', 'w', encoding='utf8') as to_write, open('balagan.txt', 'r', encoding='utf8') as to_read:
    for line in to_read:
        if 'Java' in line and 'Java Script' not in line:
            to_write.write(line.replace("Java", "Python"))
        else:
            to_write.write(line)

# Print output message

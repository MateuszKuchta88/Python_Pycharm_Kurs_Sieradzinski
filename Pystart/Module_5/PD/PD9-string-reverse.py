# PD5 9 - Reverse string

# TASK DESCRIPTION
# Write a function that receives text and then writes each word of it to
# the reverse form, e.g. Programuję w Pythonie, will replace it with eijumargorP in einohtyP

# Import libraries


# Testing data
g_str = "Programuję w Pythonie"


# Declare variables


# Declare function
def string_reverse(sentence: str) -> str:
    """
    Function takes each word out of given sentence, revert it and returns concat of all words in given sentence
    :param sentence: string with words
    :return: sentence with each word reversed
    """
    new_str = ""
    for item in sentence.split(" "):
        new_str += "".join(list(item)[::-1]) + " "
    return new_str.rstrip()


# Process

# Print output message
print(f'Answer is "{string_reverse(g_str)}".')

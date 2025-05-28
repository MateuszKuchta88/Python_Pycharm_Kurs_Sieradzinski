# Module 6 - Which word occurs most often

# TASK DESCRIPTION
# Write a function that takes a list of words and returns the word that
# occurs most often. The function should take arguments
# named *args and ignore_case with a default value of True which
# will indicate whether to ignore case when counting
# speeches.

# Import libraries


# Testing data
# g_str = 'aaa'


# Declare function
def words_most_often(*args, ignore_case: bool = True) -> dict:
    work_dict = {}
    for word in args:
        word = word.lower() if ignore_case else word
        work_dict[word] = work_dict.get(word, 0) + 1
    for word, occur in work_dict.items():
        if occur == max(work_dict.values()):
            return word


# Print output message
print(f'Answer is {words_most_often("AaA", "aaa", "bbb", "CCC", ignore_case=False)}.')

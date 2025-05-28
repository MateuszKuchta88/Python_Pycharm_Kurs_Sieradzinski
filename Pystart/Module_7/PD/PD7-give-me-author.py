# PD7 7 - Give me author

# TASK DESCRIPTION
# Using the API provided by Wolnelektury, download all of them
#  works of a specific author. The author's name and surname should be provided
# as a response to the user's question. Save the result to a file named:
#  author-name-lastname.json

# Import libraries
from requests import get
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# Declare function
given_author = str(input("Give me author: "))
given_author = given_author.split()
given_author_cap = []
for word in given_author:
    given_author_cap.append(word.capitalize())
given_author = ' '.join(given_author_cap)
given_author_minus = '-'.join(given_author_cap)
file_name = given_author_minus + '.txt'

# print(file_name)
# Program

with open(file_name, 'w', encoding='utf8') as to_write:
    url_ini = "https://wolnelektury.pl/api/authors/"
    author_formatted = given_author_minus.lower()
    author_normal = given_author
    books = "/books/?format=json"
    url = url_ini + author_formatted + books
    print(url)

    for reading in get(url).json():
        if reading.get("author") == author_normal:
            print(f'{reading.get("title")}')
            to_write.write(reading.get("title") + '\n')

# Print output message
#     for name in login_sum_time.keys():
#         lst = login_sum_time[name]
#         print(f'{name} was logged in for {lst.hours} hours, {lst.minutes} minutes and {lst.seconds} seconds.')

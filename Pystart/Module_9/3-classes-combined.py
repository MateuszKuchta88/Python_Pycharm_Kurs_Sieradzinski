# Module 9 - Combine classes

# TASK DESCRIPTION
# Prepare the classes that reproduce data, and then create
# objects according to this one structure.

# Import libraries
from datetime import date

# Testing data


# Declare function

class Author:
    def __init__(self, first_name: str, surname_name: str, birth_date: date):
        self.first_name = first_name
        self.surname_name = surname_name
        self.birth_date = birth_date


class Book:
    def __init__(self, title: str, book_type: str, description: str, book_summary: str, rating: float):
        self.title = title
        self.book_type = book_type
        self.authors = []
        self.description = description
        self.book_summary = book_summary
        self.rating = rating

    def add_author(self, author: Author):
        self.authors.append(author)


# Tests
author_1 = Author('Bonifacy', 'Smith', date(1910, 10, 10))
author_2 = Author('John', 'Smith', date(1905, 5, 15))
book_1 = Book('Przykładowy tytuł', 'Kryminał', 'Opis książki', 'Krótkie streszczenie', 5.0)
book_1.add_author(author_1)
book_1.add_author(author_2)

# Print output message

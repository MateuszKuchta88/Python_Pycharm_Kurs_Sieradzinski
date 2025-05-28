# Module 9 - Combine classes (code improved with gpt)

# TASK DESCRIPTION
# Prepare the classes that reproduce data, and then create
# objects according to this one structure.

from datetime import date

# Classes
class Author:
    """
    Represents an author with a first name, surname, and birth date.

    Attributes:
        first_name (str): The first name of the author.
        surname_name (str): The surname of the author.
        birth_date (date): The birthdate of the author.
    """

    def __init__(self, first_name: str, surname_name: str, birth_date: date):
        self.first_name = first_name
        self.surname_name = surname_name
        self.birth_date = birth_date

    def __str__(self):
        return f"{self.first_name} {self.surname_name} (born {self.birth_date})"


class Book:
    """
    Represents a book with a title, type, description, summary, rating, and authors.

    Attributes:
        title (str): The title of the book.
        book_type (str): The genre or type of the book.
        description (str): A detailed description of the book.
        book_summary (str): A short summary of the book.
        rating (float): The book's rating.
        authors (list): A list of authors who contributed to the book.
    """

    def __init__(self, title: str, book_type: str, description: str, book_summary: str, rating: float):
        self.title = title
        self.book_type = book_type
        self.authors = []
        self.description = description
        self.book_summary = book_summary
        self.rating = rating

    def add_author(self, author: Author):
        """
        Adds an author to the book's list of authors.

        Args:
            author (Author): An instance of the Author class to be added.
        """
        self.authors.append(author)

    def __str__(self):
        authors_str = ", ".join(str(author) for author in self.authors)
        return (f"Title: {self.title}\n"
                f"Type: {self.book_type}\n"
                f"Description: {self.description}\n"
                f"Summary: {self.book_summary}\n"
                f"Rating: {self.rating}\n"
                f"Authors: {authors_str}")


# Testing the classes
if __name__ == "__main__":
    # Create authors
    author_1 = Author('Bonifacy', 'Smith', date(1910, 10, 10))
    author_2 = Author('John', 'Smith', date(1905, 5, 15))

    # Create a book and add authors
    book_1 = Book('Przykładowy tytuł', 'Kryminał', 'Opis książki', 'Krótkie streszczenie', 5.0)
    book_1.add_author(author_1)
    book_1.add_author(author_2)

    # Print book details
    print(book_1)

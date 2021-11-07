import datetime
from Library import Library


class Book:
    def __init__(self, library: Library, publication_date: datetime.date,
                 author_name: str, author_surname: str,
                 number_of_pages: int):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self):
        return f"The book is owned by library in {self._library.city} on" \
               f" {self._library.street}, date of publication is " \
               f"{self._publication_date}, author is {self._author_name}" \
               f" {self._author_surname}."

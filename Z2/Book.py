
from datetime import date

class Book():
    def __init__(self,library: Library,publication_date: date,author_name: str,author_surname: str,number_of_pages: int):
       self._library=library
       self._publication_date=publication_date
       self._author_name=author_name
       self._author_surname=author_surname
       self._number_of_pages=number_of_pages
    def __str__(self):
         return f"Library {self._library}, publication date: {self._publication_date}, author name and surname: {self._author_name + ' ' + self._author_surname}, number of pages: {self._number_of_pages}."



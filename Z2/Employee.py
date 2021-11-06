import datetime


class Employee:
    def __init__(self, first_name: str, last_name: str,
                 hire_date: datetime.date, birth_date: datetime.date,
                 city: str, street: str, zip_code: str, phone: int):
        self.first_name = first_name
        self.last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self):
        return f"Employee: {self.first_name}{self.last_name}, hire date:" \
               f" {self._hire_date}. birth date: {self._birth_date}, city: " \
               f"{self._city}, street: {self._street}, zip code:" \
               f" {self._zip_code}, phone {self._phone}."

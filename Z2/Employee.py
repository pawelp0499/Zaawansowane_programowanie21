
from datetime import date

class Employee():
    def __init__(self,first_name: str,last_name: str,hire_date: date,birth_date: date,city: str,street: str,zip_code: int,phone: int):
       self._first_name=first_name
       self._last_name=last_name
       self._hire_date=hire_date
       self._birth_date=birth_date
       self._city=city
       self._street=street
       self._zip_code=zip_code
       self._phone=phone

    def __str__(self):
      return f"Employee's name: {self._first_name}, surname: {self._last_name}, date of hiring: {self._hire_date}, birth date: {self._birth_date}, city: {self._city}, street: {self._street}, zip code: {self._zip_code}, phone number: {self._phone}."
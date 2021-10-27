class Library:
    def __init__(self,city: str,street: str,zip_code: str,open_hours: str,phone: int):
       self._city=city
       self._street=street
       self._zip_code=zip_code
       self._open_hours=open_hours
       self._phone=phone

    def __str__(self):
      return f'Library in city: {self._city}, on {self._street} street, zip code: {self._zip_code}, open hours: {self._open_hours}, phone number: {self._phone}.'


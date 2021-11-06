class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str,
                 phone: int):
        self.city = city
        self.street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self):
        return f"Library in {self.city} on {self.street} street, zip code:" \
               f" {self._zip_code}, open hours: {self._open_hours}, " \
               f"phone number: {self._phone}."

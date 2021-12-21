import datetime


class Uzytkownik:
    def __init__(self, login: str, imie: str, nazwisko: str,
                 data_rejestracji: datetime.date):
        self._login = login
        self._imie = imie
        self._nazwisko = nazwisko
        self._data_rejestracji = data_rejestracji

    @property
    def login(self) -> str:
        return self._login

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def data_rejestracji(self) -> datetime.date:
        return self._data_rejestracji

    def __str__(self) -> str:
        return f"Login użytkownika: {self._login}\n " \
               f"imię: {self._imie}\n" \
               f"nazwisko: {self._nazwisko}\n"\
               f"data rejestracji: {self._data_rejestracji}."

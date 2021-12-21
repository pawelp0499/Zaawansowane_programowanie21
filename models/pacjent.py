import datetime
from uzytkownik import Uzytkownik


class Pacjent(Uzytkownik):
    def __init__(self, login: str, imie: str, nazwisko: str,
                 data_rejestracji: datetime.date, wiek: int):
        super().__init__(login, imie, nazwisko, data_rejestracji)
        self._wiek = wiek

    @property
    def wiek(self) -> int:
        return self._wiek

    def __str__(self) -> str:
        return super().__str__() + f", a jego wiek to {self._wiek}."

import datetime
from uzytkownik import Uzytkownik


class Dietetyk(Uzytkownik):
    def __init__(self, login: str, imie: str, nazwisko: str,
                 data_rejestracji: datetime.date, staz_pracy: int):
        super().__init__(login, imie, nazwisko, data_rejestracji)
        self._staz_pracy = staz_pracy

    @property
    def staz_pracy(self) -> int:
        return self._staz_pracy

    def __str__(self) -> str:
        return super().__str__() + f", jego staż to {self._staz_pracy} lat."

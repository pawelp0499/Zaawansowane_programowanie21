from dieta import Dieta


class Zamowienie:
    def __init__(self, dieta: str, ilosc: int,
                 cenajednostkowa: float, adreswysylki: str, platnosc: str):
        self._dieta = dieta
        self._ilosc = ilosc
        self._cenajednostkowa = cenajednostkowa
        self._adreswysylki = adreswysylki
        self._platnosc = platnosc

    @property
    def dieta(self) -> str:
        return self._dieta

    @dieta.setter
    def dieta(self, value: str):
        self._dieta = value

    @property
    def ilosc(self) -> int:
        return self._ilosc

    @ilosc.setter
    def ilosc(self, value: int):
        self._ilosc = value

    @property
    def cenajednostkowa(self) -> float:
        return self._cenajednostkowa

    @cenajednostkowa.setter
    def cenajednostkowa(self, value: float):
        self._cenajednostkowa = value

    @property
    def platnosc(self) -> str:
        return self._platnosc

    @platnosc.setter
    def platnosc(self, value: str):
        self._platnosc = value

    def __str__(self) -> str:
        return f"Dieta {self._dieta} " \
               f"w ilosci {self._ilosc}" \
               f"w cenie {self._cenajednostkowa}," \
               f" adres klienta {self._adreswysylki}," \
               f" adres wysyłki to {self._platnosc}"

    def oblicz_wartosc_zamowienia(self) -> float:
        return round((self._ilosc * self._cenajednostkowa), 2)

    def zwroc_kalorie(self) -> float:
        return Dieta.kcal

class Dieta:
    def __init__(self, nazwa: str, cena: float, okres_czasu: str,
                 kcal: float):
        self._nazwa = nazwa
        self._cena = cena
        self._okres_czasu = okres_czasu
        self._kcal = kcal

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def cena(self) -> float:
        return self._cena

    @property
    def okres_czasu(self) -> str:
        return self._okres_czasu

    @property
    def kcal(self) -> float:
        return self._kcal

    def __str__(self) -> str:
        return f"Jest to {self._nazwa} kosztująca {self._cena} zł," \
               f" trwająca {self._okres_czasu} i posiadająca {self._kcal} kcal."

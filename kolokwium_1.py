class Zamowienie:
    def __init__(self, produkt: str, ilosc: int, cenajednostkowa: float,
                 pracownik: str, adreswysylki: str, platnosc: str):
        self._produkt = produkt
        self._ilosc = ilosc
        self._cenajednostkowa = cenajednostkowa
        self._pracownik = pracownik
        self._adreswysylki = adreswysylki
        self._platnosc = platnosc

    @property
    def produkt(self):
        return self._produkt

    @produkt.setter
    def produkt(self, value: str):
        self._produkt = value

    @property
    def ilosc(self):
        return self._ilosc

    @ilosc.setter
    def ilosc(self, value: int):
        self._ilosc = value

    @property
    def cenajednostkowa(self):
        return self._cenajednostkowa

    @cenajednostkowa.setter
    def cenajednostkowa(self, value: float):
        self._cenajednostkowa = value

    @property
    def pracownik(self):
        return self._pracownik

    @pracownik.setter
    def pracownik(self, value: str):
        self._pracownik = value

    @property
    def adreswysylki(self):
        return self._adreswysylki

    @adreswysylki.setter
    def adreswysylki(self, value: str):
        self._adreswysylki = value

    @property
    def platnosc(self):
        return self._platnosc

    @platnosc.setter
    def platnosc(self, value: str):
        self._platnosc = value

    def __str__(self):
        return f"Zamówienie dotyczy produktu {self._produkt} " \
               f"o cenie jednostkowej wynoszącej: {self._cenajednostkowa} zł " \
               f"w ilości {self._ilosc}, obsługuje je pracownik {self._pracownik}," \
               f" adres wysyłki to {self._adreswysylki}, a sposób płatności: {self._platnosc}."

    def oblicz_wartosc_zamowienia(self) -> float:
        return round((self._ilosc * self._cenajednostkowa), 2)

    def zwroc_adres(self) -> str:
        return f"Ares klienta: {self._adreswysylki}."


class Produkt:
    def __init__(self, nazwa: str, rozmiar: str, zastosowanie: str, rokprodukcji: int, krajprodukcji: str):
        self._nazwa = nazwa
        self._rozmiar = rozmiar
        self._zastosowanie = zastosowanie
        self._rokprodukcji = rokprodukcji
        self._krajprodukcji = krajprodukcji

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def rozmiar(self):
        return self._rozmiar

    @property
    def zastosowanie(self):
        return self._zastosowanie

    @property
    def rokprodukcji(self):
        return self._rokprodukcji

    @property
    def krajprodukcji(self):
        return self._krajprodukcji

    def __str__(self):
        return f"Produkt: {self._nazwa}, " \
               f"o rozmiarze {self._rozmiar}, stosowany do: {self._zastosowanie}," \
               f"wyprodukowany w roku: {self._rokprodukcji} w kraju {self._krajprodukcji}."


class Magazyn:
    def __init__(self, nazwa: str, miasto: str, iloscpracownikow: int,
                 powierzchnia: int, rokzalozenia: int):
        self._nazwa = nazwa
        self._miasto = miasto
        self._iloscpracownikow = iloscpracownikow
        self._powierzchnia = powierzchnia
        self._rokzalozenia = rokzalozenia

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def miasto(self):
        return self._miasto

    @property
    def iloscpracownikow(self):
        return self._iloscpracownikow

    @property
    def powierzchnia(self):
        return self._powierzchnia

    @property
    def rokzalozenia(self):
        return self._rokzalozenia

    def __str__(self):
        return f"Magazyn: {self._nazwa}, " \
               f"w {self._miasto}, w którym pracuje: {self._iloscpracownikow} pracownikow," \
               f"jego powierzchnia to: {self._powierzchnia} m2, założony w roku {self._rokzalozenia}."


class KlientDetaliczny:
    def __init__(self, imie: str, nazwisko: str, wiek: int, miasto: str, branza: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek
        self._miasto = miasto
        self._branza = branza

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def wiek(self):
        return self._wiek

    @property
    def miasto(self):
        return self._miasto

    @property
    def branza(self):
        return self._branza

    def __str__(self):
        return f"Klient to {self._imie} {self._nazwisko}" \
               f" w wieku {self._wiek} z miast {self._miasto}," \
               f" reprezentujący branżę {self._branza}."


class KlientBiznesowy(KlientDetaliczny):
    def __init__(self, imie: str, nazwisko: str,
                 wiek: int, miasto: str, branza: str, vat: float):
        super().__init__(imie, nazwisko, wiek, miasto, branza)
        self._vat = vat

    @property
    def vat(self):
        return self._vat

    def __str__(self):
        return super().__str__() + f"," \
                                   f" kwota vat wynosi: {self._vat}. "


zamowienie = Zamowienie("Intel i5", 2, 812.121,
                        "Jan Kowalski", "Bogucicka 2, 00-000 Katowice", "pobranie")
print(zamowienie.__str__())

# print(zamowienie.oblicz_wartosc_zamowienia())
# print(zamowienie.zwroc_adres())
# wywołanie metod zaimplementowanych w klasie zamówienie.

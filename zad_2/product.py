import datetime


class Product:
    def __init__(self, name: str, size: str, unit_price: float, production_date: datetime.date, country: str):
        self._name = name
        self._size = size
        self._unit_price = unit_price
        self._production_date = production_date
        self._country = country

    @property
    def name(self) -> str:
        return self._name

    @property
    def size(self) -> str:
        return self._size

    @property
    def unit_price(self) -> float:
        return self._unit_price

    @property
    def production_date(self) -> datetime.date:
        return self._production_date

    @property
    def country(self) -> str:
        return self._country

    def __str__(self):
        return f"Product: {self._name}, " \
               f"size {self._size}, price: {self._unit_price}," \
               f"date of production: {self._production_date} in country: {self._country}."

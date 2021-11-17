from customer import Customer
from product import Product


class Order:
    def __init__(self):
        self._product = None
        self._quantity = None
        self._unit_price = None
        self._employee = None
        self._address = None
        self._payment = None

    @property
    def product(self) -> str:
        return self._product

    @product.setter
    def product(self, value: Product):
        self._product = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        self._quantity = value

    @property
    def unit_price(self) -> float:
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value: Product):
        self._unit_price = value

    @property
    def employee(self) -> str:
        return self._employee

    @employee.setter
    def employee(self, value: str):
        self._employee = value

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: Customer):
        self._address = value

    @property  # payment method
    def payment(self) -> str:
        return self._payment

    @payment.setter
    def payment(self, value: str):
        self._payment = value

    def __str__(self):
        return f"Ordered product is {self._product}, " \
               f"unit price: {self._unit_price} zł, " \
               f"quantity: {self._quantity}, employee: {self._employee}, " \
               f" customer's address: {self._address}, payment method is {self._payment}."

    def oblicz_wartosc_zamowienia(self) -> float:
        return round((self._quantity * self._unit_price), 2)

    def zwroc_adres(self) -> str:
        return f"Customer's address: {self._address}."

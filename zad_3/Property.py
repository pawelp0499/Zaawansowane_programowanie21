class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    @property
    def area(self) -> float:
        return self._area

    @area.setter
    def area(self, value: float) -> None:
        self._area = value

    @property
    def rooms(self) -> int:
        return self._rooms

    @rooms.setter
    def rooms(self, value: int) -> None:
        self._rooms = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        self._price = value

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: float) -> None:
        self._address = value

    def __str__(self):
        return f'Details about property: an area of {self.area}' \
               f' square meters, {self.rooms} rooms, price is' \
               f' {self.price}, address: {self.address}'

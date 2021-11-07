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
        return f'Details about property: an area of {self.area} ' \
               f'square meters, {self.rooms} rooms, price is {self.price},' \
               f' address: {self.address}'


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str,
                 plot: int):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    @property
    def plot(self) -> int:
        return self._plot

    @plot.setter
    def plot(self, value: int) -> None:
        self._plot = value

    def __str__(self):
        return super().__str__() + f", Plot: {self._plot}."


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float,
                 address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    @property
    def floor(self) -> int:
        return self._floor

    @floor.setter
    def floor(self, value) -> None:
        self._floor = value

    def __str__(self):
        return super().__str__() + f", Floors: {self._floor}."


house = House(124.5, 4, 125000, "Bogucicka 1, 00-001 Katowice", 10)
print(house.__str__())

flat = Flat(15000, 3, 121000, "3 Maja 00-001, Katowice", 5)
print(flat.__str__())

from Property import Property


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

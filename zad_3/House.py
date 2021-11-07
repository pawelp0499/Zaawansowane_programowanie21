from Property import Property


class House(Property):
    def __init__(self, area: float, rooms: int, price: float,
                 address: str, plot: int):
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

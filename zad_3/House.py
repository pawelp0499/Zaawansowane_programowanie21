from Property import Property

class House(Property): #child class
    def __init__(self, area, rooms, price, address, plot: int):
      super().__init__(area, rooms, price, address)
      self._plot=plot

    def __str__(self):
      return f'Property is house with an area of {self._area} square meters, {self._rooms} rooms, price is {self._price}, address: {self._address}. Plot: {self._plot}.'
from Property import Property

class Flat(Property): #child class
    def __init__(self, area, rooms, price, address, floor: int):
      super().__init__(area, rooms, price, address)
      self._floor=floor

    def __str__(self):
       return f'Property is flat with an area of {self._area} square meters, {self._rooms} rooms, price is {self._price}, address: {self._address}. Numbers of floors: {self._floor}.'
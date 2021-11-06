#Zad3
class Property: #parent class
   def __init__(self, area: int, rooms: int, price: int, address: str):
       self._area=area
       self._rooms=rooms
       self._price=price
       self._address=address

class House(Property): #child class
    def __init__(self, area, rooms, price, address, plot: int):
      super().__init__(area, rooms, price, address)
      self._plot=plot

    def __str__(self):
      return f'Property is house with an area of {self._area} square meters, {self._rooms} rooms, price is {self._price}, address: {self._address}. Plot: {self._plot}.'

class Flat(Property): #child class
    def __init__(self, area, rooms, price, address, floor: int):
      super().__init__(area, rooms, price, address)
      self._floor=floor

    def __str__(self):
       return f'Property is flat with an area of {self._area} square meters, {self._rooms} rooms, price is {self._price}, address: {self._address}. Numbers of floors: {self._floor}.'

house = House(200,15,500000,"Mikołowska, Katowice",300)
flat = Flat(100,4,350000,"Bogucicka, Katowice",2)

print(house.__str__())
print(flat.__str__())

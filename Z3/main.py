from Property import Property
from House import House
from Flat import Flat

house = House(200,15,500000,"Mikołowska, Katowice",300)
flat = Flat(100,4,350000,"Bogucicka, Katowice",2)

print(house.__str__())
print(flat.__str__())
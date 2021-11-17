import datetime
from customer import Customer
from product import Product
from order import Order

produkt = Product("Item", "small,", 4.51, datetime.date(2013, 5, 9), "Poland")
klient = Customer("Bogucicka 1, 00-000, Katowice", "IT")

zamowienie = Order()
zamowienie.address = klient.address
zamowienie.product = produkt.name
zamowienie.quantity = 3
zamowienie.unit_price = produkt.unit_price
print(zamowienie.oblicz_wartosc_zamowienia())
print(zamowienie.zwroc_adres())

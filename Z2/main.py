import datetime
from Student import Student
from Employee import Employee
from Library import Library
from Order import Order
from Book import Book


library1 = Library("Katowice", "Bogucicka", "00-001", "7-18", 123456789)
library2 = Library("Warszawa", "1 Maja", "00-002", "7-16", 234567890)

book1 = Book(library1, datetime.date(2009, 12, 10), "Unknown", "Author", 500)
book2 = Book(library2, datetime.date(2010, 7, 8), "Unknown", "Author", 200)
book3 = Book(library1, datetime.date(2011, 6, 11), "Unknown", "Author", 100)
book4 = Book(library2, datetime.date(2012, 1, 21), "Unknown", "Author", 150)
book5 = Book(library1, datetime.date(2013, 5, 9), "Unknown", "Author", 332)

employee1 = Employee("Jan", "Kowalski", datetime.date(2016, 5, 1), datetime.date(1990, 12, 21), "Katowice", "3 Maja",
                     "00-003", 123123123)
employee2 = Employee("Marcin", "Nowak", datetime.date(2008, 1, 1), datetime.date(1978, 11, 4), "Katowice", "3 Maja",
                     "00-003", 124124124)
employee3 = Employee("Aleksandra", "Wisniewska", datetime.date(2003, 4, 11), datetime.date(1980, 12, 21), "Katowice",
                     "Bogucicka",
                     "00-001", 553123123)
student1 = Student("Adam", 45.5)
student2 = Student("Pawel", 51)

order1 = Order(employee1, student2, datetime.date.today())
order2 = Order(employee3, student1, datetime.date.today())

print(order1.__str__())
print(order2.__str__())

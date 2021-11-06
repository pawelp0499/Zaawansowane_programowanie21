import datetime


class Student:
    def __init__(self, name: str, marks: float):
        self.name = name
        self._marks = marks

    def __str__(self):
        return f"Student's name is {self.name}, score: {self._marks}."


class Employee:
    def __init__(self, first_name: str, last_name: str,
                 hire_date: datetime.date, birth_date: datetime.date,
                 city: str, street: str, zip_code: str, phone: int):
        self.first_name = first_name
        self.last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self):
        return f"Employee: {self.first_name}{self.last_name}, hire date:" \
               f" {self._hire_date}. birth date: {self._birth_date}, city: " \
               f"{self._city}, street: {self._street}, zip code:" \
               f" {self._zip_code}, phone {self._phone}."


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str,
                 phone: int):
        self.city = city
        self.street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self):
        return f"Library in {self.city} on {self.street} street, zip code:" \
               f" {self._zip_code}, open hours: {self._open_hours}, " \
               f"phone number: {self._phone}."


class Order:
    def __init__(self, employee: Employee, student: Student,
                 order_date: datetime.date):
        self._employee = employee
        self._student = student
        self._order_date = order_date

    def __str__(self):
        return f"Order processed by {self._employee.first_name}" \
               f" {self._employee.last_name} for {self._student.name}, date:" \
               f" {self._order_date}."


class Book:
    def __init__(self, library: Library, publication_date: datetime.date,
                 author_name: str, author_surname: str,
                 number_of_pages: int):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self.author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self):
        return f"The book is owned by library in {self._library.city} on" \
               f" {self._library.street}, date of publication is " \
               f"{self._publication_date}, author is {self._author_name}" \
               f" {self.author_surname}."


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

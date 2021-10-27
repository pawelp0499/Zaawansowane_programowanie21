from datetime import date

class Student: 
   def __init__(self, name: str, marks: int):
       self._name=name
       self._marks=marks
   def is_passed(self) -> bool: #(function from previous assignment) with logical output (test result)
      if self.marks > 50:
          return True
      else:
          return False
   def __str__(self):
      return f"Student's name: {self._name}, mark: {self._marks}."

class Library:
    def __init__(self,city: str,street: str,zip_code: str,open_hours: str,phone: int):
       self._city=city
       self._street=street
       self._zip_code=zip_code
       self._open_hours=open_hours
       self._phone=phone

    def __str__(self):
      return f'Library in city: {self._city}, on {self._street} street, zip code: {self._zip_code}, open hours: {self._open_hours}, phone number: {self._phone}.'

class Employee():
    def __init__(self,first_name: str,last_name: str,hire_date: date,birth_date: date,city: str,street: str,zip_code: int,phone: int):
       self._first_name=first_name
       self._last_name=last_name
       self._hire_date=hire_date
       self._birth_date=birth_date
       self._city=city
       self._street=street
       self._zip_code=zip_code
       self._phone=phone

    def __str__(self):
      return f"Employee's name: {self._first_name}, surname: {self._last_name}, date of hiring: {self._hire_date}, birth date: {self._birth_date}, city: {self._city}, street: {self._street}, zip code: {self._zip_code}, phone number: {self._phone}."

class Book():
    def __init__(self,library: Library,publication_date: date,author_name: str,author_surname: str,number_of_pages: int):
       self._library=library
       self._publication_date=publication_date
       self._author_name=author_name
       self._author_surname=author_surname
       self._number_of_pages=number_of_pages
    def __str__(self):
         return f"Library {self._library}, publication date: {self._publication_date}, author name and surname: {self._author_name + ' ' + self._author_surname}, number of pages: {self._number_of_pages}."

class Order():
    def __init__(self,employee: Employee,student: Student,books:Book,order_date):
       self._employee=employee
       self._student=student
       self._books=books
       self._order_date=order_date

    def __str__(self):
      return f'Order processed by:\n {self._employee}, \n for student: \n {self._student}, \n ordered book is \n {self._books}, \n order date: {self._order_date}'

library_1=Library("Katowice", "Słowackiego", "00-000", "7:30-15:30", 123456789)
library_2=Library("Katowice", "1 Maja", "00-000", "7:30-15:30", 234567890)

book_1 = Book(library_1,date(2002,10,1),"Jan","Kowalski",115)
book_2 = Book(library_2,date(2005,7,3),"Jan","Kowalski",300)
book_3 = Book(library_1,date(2008,3,4),"Jan","Kowalski",212)
book_4 = Book(library_2,date(2011,1,2),"Jan","Kowalski",85)
book_5 = Book(library_2,date(2017,7,8),"Jan","Kowalski",452)

employee_1=Employee("Pawel","Worker",date(2021,10,3),date(1999,4,12),"Katowice","Wiosenna","00-000",123456789)
employee_2=Employee("Jakub","Worker",date(2019,1,1),date(1987,5,9),"Katowice","Wiosenna","00-000",123896789)
employee_3=Employee("Aleksandra","Worker",date(2017,12,1),date(1978,3,11),"Katowice","Wiosenna","00-000",123896789)

student_1=Student("Paweł",40)
student_2=Student("Paweł",50)
student_3=Student("Paweł",60)

order_1=Order(employee_2,student_3,book_3,date(2021,7,10))
order_2=Order(employee_3,student_1,book_5,date(2021,6,12))


print(order_1.__str__()) #details about orders 1 and 2
print(order_2.__str__()) 




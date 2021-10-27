
from Employee import Employee
from Student import Student
from Book import Book
from datetime import date

class Order():
    def __init__(self,employee: Employee,student: Student,books:Book,order_date: date):
       self._employee=employee
       self._student=student
       self._books=books
       self._order_date=order_date

    def __str__(self):
      return f'Order processed by:\n {self._employee}, \n for student: \n {self._student}, \n ordered book is \n {self._books}, \n order date: {self._order_date}'
import datetime
from Student import Student
from Employee import Employee


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

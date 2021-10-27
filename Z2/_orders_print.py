
from datetime import date
from Library import Library
from Employee import Employee
from Student import Student
from Book import Book
from Order import Order

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



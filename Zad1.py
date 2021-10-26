#Zad1

class Student:
   def __init__(self,name,marks):
       self.name=name
       self.marks=marks
   def is_passed(self) -> bool:
      if self.marks > 50:
          return True
      else:
          return False

false_object = Student("Pawel",49)
true_object = Student("Pawel",51)
print(false_object.is_passed())
print(true_object.is_passed())
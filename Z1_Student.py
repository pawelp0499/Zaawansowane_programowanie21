#Zad1

class Student:
   def __init__(self, name: str, marks: int):
       self.name=name
       self.marks=marks
   def is_passed(self) -> bool:
      if self.marks > 50:
          return True
      else:
          return False

false_object = Student("Student X",49)
true_object = Student("Student Y",51)
print(false_object.is_passed())
print(true_object.is_passed())
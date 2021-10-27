class Student:
   def __init__(self, name: str, marks: int):
       self._name=name
       self._marks=marks
   def is_passed(self) -> bool:
      if self.marks > 50:
          return True
      else:
          return False
   def __str__(self):
      return f"Student's name: {self._name}, mark: {self._marks}."
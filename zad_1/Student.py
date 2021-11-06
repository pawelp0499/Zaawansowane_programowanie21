class Student:
    def __init__(self, name: str, marks: float):
        self._name = name
        self._marks = marks

    def is_passed(self) -> bool:
        return True if self._marks > 50 else False


student1 = Student("Adam", 45.5)
student2 = Student("Pawel", 51)

print(student1.is_passed())
print(student2.is_passed())

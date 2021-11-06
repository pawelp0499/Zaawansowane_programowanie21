class Student:
    def __init__(self, name: str, marks: float):
        self.name = name
        self._marks = marks

    def __str__(self):
        return f"Student's name is {self.name}, score: {self._marks}."

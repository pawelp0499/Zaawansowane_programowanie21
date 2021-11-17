class Warehouse:
    def __init__(self, name: str, city: str, employees_number: int,
                 area: float, foundation_year: int):
        self._name = name
        self._city = city
        self._employees_number = employees_number
        self._area = area
        self._foundation_year = foundation_year

    @property
    def name(self) -> str:
        return self._name

    @property
    def city(self) -> str:
        return self._city

    @property
    def employees_number(self) -> int:
        return self._employees_number

    @property
    def area(self) -> float:
        return self._area

    @property
    def foundation_year(self) -> int:
        return self._foundation_year

    def __str__(self):
        return f"Warehouse {self._name}, " \
               f"in {self._city}, " \
               f"with {self._employees_number} employees, "\
               f"and area: {self._area} m2, " \
               f"founded in {self._foundation_year}."

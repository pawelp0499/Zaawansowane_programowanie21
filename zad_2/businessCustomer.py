import datetime
from customer import Customer


class BusinessCustomer(Customer):
    def __init__(self, address: str, industry: str,
                 foundation_date: datetime.date, employees_number: int, vat: float):
        super().__init__(address, industry)
        self._foundation_date = foundation_date
        self._employees_number = employees_number
        self._vat = vat

    @property
    def foundation_date(self):
        return self._foundation_date

    @property
    def employees_number(self):
        return self._employees_number

    @property
    def vat(self):
        return self._vat

    def __str__(self):
        return super().__str__() + f" , date of foundation is: {self._foundation_date}," \
                                   f" number of employees: {self._employees_number}," \
                                   f" amount of vat: {self._vat}."

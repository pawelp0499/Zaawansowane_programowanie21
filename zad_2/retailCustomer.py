from customer import Customer


class RetailCustomer(Customer):
    def __init__(self, address: str, industry: str,
                 age: int, surname: str):
        super().__init__(address, industry)
        self._age = age
        self._surname = surname

    @property
    def age(self) -> int:
        return self._age

    @property
    def surname(self) -> str:
        return self._surname

    def __str__(self):
        return super().__str__() + f" , age: {self._age}," \
                                   f" surname: {self._surname}."

class Customer:
    def __init__(self, address: str, industry: str):
        self._address = address
        self._industry = industry

    @property
    def address(self) -> str:
        return self._address

    @property
    def industry(self) -> str:
        return self._industry

    def __str__(self):
        return f"Customer's address: {self._address}," \
               f" from {self._industry} industry."

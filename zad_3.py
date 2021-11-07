def is_even_number(number: int) -> bool:
    return True if number % 2 == 0 else False


value = is_even_number(2)

if value == 1:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

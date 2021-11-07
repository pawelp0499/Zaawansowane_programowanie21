use main.py or possibly all.py

# Labs 4 / Zad 2

2. Stworzyć następujące klasy:

Library (klasa opisująca bibliotekę), posiadająca pola:

◾ city
◾ street
◾ zip_code
◾ open_hours (str)
◾ phone

Order (klasa opisująca zamówienie), posiadająca pola:

◾ employee
◾ student
◾ books
◾ order_date

Employee (klasa opisująca pracownika biblioteki), posiadająca pola:

◾ first_name
◾ last_name
◾ hire_date
◾ birth_date
◾ city
◾ street
◾ zip_code
◾ phone

Book (klasa opisująca książkę), posiadająca pola

◾ library
◾ publication_date
◾ author_name
◾ author_surname
◾ number_of_pages

Dodatkowo:

Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt oraz ewentualne obiekty
znajdujące się w tym obiekcie (np. obiekt Library w obiekcie Book).

Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.

Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3 studentów, oraz 2 zamówienia.
Wyświetlić oba zamówienia ( print )

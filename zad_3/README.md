use main.py or possibly all.py

# Labs 4 / Zad 3

3. Stworzyć następujące klasy:

Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:

◾ area
◾ rooms (int)
◾ price
◾ address

House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola:

- plot (rozmiar działki, int)

Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola:

- floor


Dodatkowo:

◾ Każda z klas dziedziczących ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt.

◾ Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.

◾ Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić.
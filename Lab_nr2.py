
#Zad2
#a)
def funkcja_imiona(imie_1, imie_2, imie_3, imie_4, imie_5): 
   imiona = [imie_1, imie_2, imie_3, imie_4, imie_5]
   for i in imiona:
      print(i)

funkcja_imiona('Pawel','Kuba','Arek','Julka','Ola')

'''
#b)

#i
def funkcja_liczby(liczba_1, liczba_2, liczba_3, liczba_4, liczba_5): 
   liczby = [liczba_1*2, liczba_2*2, liczba_3*2, liczba_4*2, liczba_5*2]
   for i in liczby:
      print(i)

funkcja_liczby(1,2,3,4,5)


#c) 

for number in range(10):
    if number%2 != 1:
        print(number)
        
 #d)
for number in range (1,10,2):
    print(number)

    

list = list(range(0,10))
i = 1
while i < len(list):
    print(list[i])
    i+=2
    

   ''' 
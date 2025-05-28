print('Siemka w programie do sprawdzania czy zadana liczba jest parzysta.')
number = float(input('Podaj liczbę do sprawdzenia: '))
if number == 0:
    print('Podana liczba to zero, więc nie jest ani parzysta, ani nieparzysta.')
elif number%2 == 1:
    print('Podana liczba jest nieparzysta.')
else:
    print('Podana liczba jest parzysta.')
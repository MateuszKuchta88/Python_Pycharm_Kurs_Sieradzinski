nr = int(input('Dej rozmiar trójkąta: '))

for i in range(1, nr + 1):
    for j in range(1, nr + 2 - i):
        print(j, end = ' ')
    print('')
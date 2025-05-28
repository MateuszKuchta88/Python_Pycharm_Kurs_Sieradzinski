n = int(input('Give me positive int number nigga: '))

if n in range(1, 3):
    print(f'Number {n} is a prime number.')
else:
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            print(f'Number {n} is not a prime number.')
            break;
        elif i == 2:
            print(f'Number {n} is a prime number.')

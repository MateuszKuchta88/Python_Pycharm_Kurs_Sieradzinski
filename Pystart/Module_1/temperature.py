# This is script to convert Celsius to Fahrenheit and Fahrenheit to Celsius

k = int(input('If you would like to convert Fahrenheit to Celsius, press 1. If you want to convert Celsius to Fahrenheit, press 2: '))

if k == 1:
    t0 = int(input('Give me the value in Fahrenheit that you would like to convert: '))
    t1 = 'Fahrenheit'
    t2 = 'Celsius'
    t = 5 * (t0 - 32) / 9
elif k == 2:
    t0 = int(input('Give me the value in Celsius that you would like to convert: '))
    t1 = 'Celsius'
    t2 = 'Fahrenheit'
    t = t0 * 1.8 + 32
else:
    print("I don't know what you want to do.")
    quit()

print(f'{t0:.2f} {t1} equals {t:.2f} {t2}.')
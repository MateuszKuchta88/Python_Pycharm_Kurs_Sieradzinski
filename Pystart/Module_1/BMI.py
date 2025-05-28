height = float(input('Dej mi swój wzrost w cm: '))
weight = float(input('Dej mi swoją wagę w kg: '))
BMI = round(weight/((0.01*height)**2),2)
print(f'Twoje BMI to {BMI}')
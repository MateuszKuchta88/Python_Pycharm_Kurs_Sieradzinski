sentence = "12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek."

x = sentence.split(' ')
sum = 0

for i in x:
    if i.isnumeric() == True:
        sum += float(i)

print(sum)
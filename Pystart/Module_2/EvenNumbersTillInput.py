finish = int(input("Give max value of range:"))
l = tuple(range(2,finish,2))
sum = 0
multiply = 1
for i in l:
    sum += i
    multiply *= i
    if i != l[len(l)-1]:
        print(i, end = ",")
    else:
        print(i)

print(f'Sum of these numbers equals {sum}.')
print(f'There is {len(l)} numbers in this tuple.')
print(f'Their mean equals {sum/len(l)}')
print(f'When you multiply all of them it equals {multiply}')
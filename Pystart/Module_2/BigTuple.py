t = tuple(range(12, 1024, 6))

print(len(t))
print(t[0], t[1], t[2])
print(t[len(t) - 2])

for i in range(3, len(t)):
    if (i + 3) % 6 == 0:
        print(t[i])

for i in range(1, len(t)):
    if i % 3 == 0:
        print(t[len(t) - i])

sum = 0
for i in range(1,11):
    sum += t[len(t) - i]
average = sum/10.
print(average)
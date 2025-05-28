s = str(input("Give me sentence nigga: "))
s = s.lower()
# for i in range(0, len(s)):
#     if i % 2 == 0:
#         print(s[i].capitalize(), end = '')
#     else:
#         print(s[i], end = '')

t = s.split(' ')
print(t)
for i in range(0, len(t)):
    if i % 2 == 0:
        print(t[i].upper(), end = ' ')
    else:
        print(t[i], end = ' ')
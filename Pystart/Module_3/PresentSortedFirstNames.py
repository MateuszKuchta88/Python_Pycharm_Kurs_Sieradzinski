full_names = 'Adam Mickiewicz, Zbigniew Nienacki, Adam Asnyk, Michał Anioł, Zbigniew Kot'
not_sorted_list = full_names.split()
sorted_list = []
for i in range(0,len(not_sorted_list),2):
    sorted_list.append(not_sorted_list[i])

sorted_list.sort(reverse=True)
j = 0

while j < len(sorted_list) - 1:
    if sorted_list[j] == sorted_list[j + 1]:
        sorted_list.remove(sorted_list[j + 1])
    else:
        j += 1

print(sorted_list)

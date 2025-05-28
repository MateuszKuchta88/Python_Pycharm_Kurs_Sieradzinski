given_list = []
list_length = 5

for i in range(1, list_length + 1):
    given_list.append(float(input(f'Give me number no {i}: ')))

print(f'Smallest value in given list is {min(given_list)}.')
print(f'Biggest value in given list is {max(given_list)}.')
print(f'Aritmetic average of values in given list is {sum(given_list)/list_length}.')

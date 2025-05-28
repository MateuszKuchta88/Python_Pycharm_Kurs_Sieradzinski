# PD4 - Names counter

# Ask the user for their name until he or she writes "end", the program should
# display a dictionary presenting names along with the number of their occurrences and a unique list of names
# sorted alphabetically.

# Import libraries

# Declare variables
names = {}
names_list = []
update_dict = {}
count_dict = {}

# Welcome message
print('Welcome in "Names counter" app.')

# While loop for operations
print('If you want to finish introducing new names write "end" instead of name.')
while 0 == 0:
    name = str(input("Give me name: "))
    if name == "end":
        break
    names_list.append(name)

for name in names_list:
    if name not in count_dict:
        update_dict = {name: 1}
        count_dict.update(update_dict)
    else:
        count_dict[name] += 1

# print goodbye message
print(f'Here you have {len(count_dict.values())} names with number of their occurrences:')
for name, count in count_dict.items():
    print(f'{name} - {count}')

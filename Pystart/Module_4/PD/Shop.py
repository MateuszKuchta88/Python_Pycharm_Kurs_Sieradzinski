# PD4 - Shop

# Prepare a dictionary containing products. The product is the key and the price is the value. ask
# the user which product he wants to add to the cart and in what quantity. Ask
# until the user responds “summarize”.
# You can store the order value in a single variable or have a list
# (for those interested) products or dictionaries if you want to display a summary.

# Import libraries

# Declare variables
final_dict = {}
total_cost = 0

# Welcome message
print('Welcome in our Shop.')

# Build dictionary
shop_items = {"T-shirt": 50, "shoes": 120, "gloves": 40, "hat": 45, "trousers": 80, "jacket": 130}

# While loop for operations
print('If you want to finish shopping put "summarize" instead of item.')
while 0 == 0:
    print('Find below what you can buy:\nT-shirt 50$\nshoes 120$\ngloves 40$\nhat 45$\ntrousers 80$\njacket 130$')
    item = str(input("What do you want to buy?: "))
    if item == "summarize":
        break
    quantity = int(input("How many of those?: "))
    if item not in final_dict:
        final_dict.update({item: quantity})
    else:
        final_dict[item] += quantity

# print goodbye message
print("You have bought: ")
for item, quantity in final_dict.items():
    if item[-1] == "s":
        print(f'{quantity} {item}, each of them costs {shop_items[item]}$, '
              f'so in total it costs {quantity * shop_items[item]}$;')
    elif quantity != 1:
        print(f'{quantity} {item}s, each of them costs {shop_items[item]}$, '
              f'so in total it costs {quantity * shop_items[item]}$;')
    else:
        print(f'{quantity} {item}, each of them costs {shop_items[item]}$, '
              f'so in total it costs {quantity * shop_items[item]}$;')
    total_cost += quantity * shop_items[item]
print(f'You have to pay {total_cost}$.')

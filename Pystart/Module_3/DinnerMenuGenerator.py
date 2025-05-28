from random import choice

dishes = {
    "soup" : ["tomato soup", "beetroot soup", "chicken soup"],
    "dinner" : ["schnitzel ", "spaghetti", "dumplings"],
    "desser" : ["ice cream", "cookies", "apple pie"]
}

for dish in dishes:
    print(choice(dishes[dish]))
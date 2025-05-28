# Module 9 - Basket with fruits

# TASK DESCRIPTION
# Zosia was walking in the meadow and picking apples.
# Each fruit has:
#  color e.g. red, green, yellow,
#  taste e.g. sweet, sour
#  type e.g. ripe, unripe.
# Prepare a Basket object to which you can add fruits and
# generate a report according to a given feature. e.g. number of fruits by colors.
# Ideally, the report would also be an object :)

# Import libraries
from dataclasses import dataclass
from random import choice


# Testing data


# Declare function
@dataclass
class Apple:
    # def __init__(self, color: str, taste: str, apple_type: str):
    #     self.color = color
    #     self.taste = taste
    #     self.apple_type = apple_type
    color: str
    taste: str
    apple_type: str


class Basket:
    def __init__(self):
        self.apples = []

    def add_apple(self, apple: Apple):
        self.apples.append(apple)


class Report:
    def generate_report(self, basket: Basket, feature: str):
        statistics = {}
        for apple in basket.apples:
            if feature == 'color':
                statistics.update({apple.color: statistics.get(apple.color, 0) + 1})
            elif feature == 'taste':
                statistics.update({apple.taste: statistics.get(apple.taste, 0) + 1})
            elif feature == 'apple_type':
                statistics.update({apple.apple_type: statistics.get(apple.apple_type, 0) + 1})
        return statistics


# Tests
colors = ['red', 'green']
tastes = ['sweet', 'sour']
apple_types = ['old', 'fresh']
basket_1 = Basket()
for _ in range(100):
    basket_1.add_apple(Apple(choice(colors), choice(tastes), choice(apple_types)))

# Print output message
print(Report().generate_report(basket_1, 'color'))
print(Report().generate_report(basket_1, 'taste'))
print(Report().generate_report(basket_1, 'apple_type'))
# Module 9 - Class for cars

# TASK DESCRIPTION
# Prepare a Car class that should store the name
# car, its price and maximum speed. Ask
# user by 5 cars and then display them on
# screen.

# Import libraries


# Testing data


# Declare function

class Car:
    def __init__(self, name: str, price: int, max_speed: int):
        self.name = name
        self.price = price
        self.max_speed = max_speed

# Tests


cars = []
i = 0

while i < 5:
    cars.append(Car(str(input("Give me name of a car: ")), int(input("Give me its price: ")), int(input("Give me its maximum speed: "))))
    i += 1


# Print output message
j = 0
while j < len(cars):
    print(f"Car name: {cars[j].name}.")
    print(f"Car price: {cars[j].price}.")
    print(f"Car maximum speed: {cars[j].max_speed}.\n")
    j += 1

# Module 9 - Class for Cars (code improved with gpt)

# TASK DESCRIPTION
# Prepare a Car class that should store the name
# of the car, its price, and its maximum speed. Ask
# the user for details of 5 cars and then display them on
# the screen.

class Car:
    """
    A class to represent a car.

    Attributes:
        name (str): The name of the car.
        price (int): The price of the car.
        max_speed (int): The maximum speed of the car.
    """
    def __init__(self, name: str, price: int, max_speed: int):
        """
        Initialize the car with a name, price, and maximum speed.

        Args:
            name (str): The name of the car.
            price (int): The price of the car.
            max_speed (int): The maximum speed of the car.
        """
        self.name = name
        self.price = price
        self.max_speed = max_speed

    def __str__(self):
        """
        Return a string representation of the car.

        Returns:
            str: A formatted string describing the car.
        """
        return f"Car name: {self.name}\nCar price: {self.price}\nCar maximum speed: {self.max_speed}\n"


def get_car_details() -> list[Car]:
    """
    Prompt the user to input details for 5 cars.

    Returns:
        list[Car]: A list of Car objects created from user input.
    """
    cars = []
    for i in range(5):
        print(f"\nEnter details for car {i + 1}:")
        name = input("Name: ")
        price = int(input("Price: "))
        max_speed = int(input("Maximum speed: "))
        cars.append(Car(name, price, max_speed))
    return cars


def display_cars(cars: list[Car]) -> None:
    """
    Display details of all cars in the list.

    Args:
        cars (list[Car]): A list of Car objects to display.
    """
    print("\nDetails of the cars:")
    for car in cars:
        print(car)


# Main program
if __name__ == "__main__":
    display_cars(get_car_details())

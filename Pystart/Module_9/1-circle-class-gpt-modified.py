# Module 9 - Class for circle (code improved with chat gpt)

# TASK DESCRIPTION
# Implement the Circle class which should be in the init method
# get the radius of the circle. This class should have two methods
# calculating the area as well as the circumference of a circle. Remember about testing.
# Ask user about the radius of a circle and display its area and circumference.

# Import libraries
from math import pi


class Circle:
    """
    A class representing a circle.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        area() -> float:
            Calculates and returns the area of the circle.
        circumference() -> float:
            Calculates and returns the circumference of the circle.
    """

    def __init__(self, radius: float):
        """
        Initializes a Circle instance with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self) -> float:
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return pi * self.radius ** 2

    def circumference(self) -> float:
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * pi * self.radius


# User input and testing
if __name__ == "__main__":
    try:
        r = float(input("Enter the radius of the circle: "))
        circle = Circle(r)

        # Display results
        print(f"Area of the circle: {circle.area():.2f}")
        print(f"Circumference of the circle: {circle.circumference():.2f}")

    except ValueError as e:
        print(f"Error: {e}")

# Module 9 - Class for circle

# TASK DESCRIPTION
# Implement the Circle class which should be in the init method
# get the radius of the circle. This class should have two methods
# calculating the area as well as the circumference of a circle. Remember about testing.
# Ask user about the radius of a circle and display its area and circumference.

# Import libraries
from math import pi


# Testing data


# Declare function

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return pi * pow(self.radius, 2)

    def circumference(self):
        return 2 * pi * self.radius


# Tests
def test_circle_class():
    circ = Circle(5)
    area = circ.area()
    circumference = circ.circumference()

    assert 78.5 < area < 78.6
    assert 31.4 < circumference < 31.5


c = Circle(float(input("Give me radius of circle: ")))


# Print output message
print(f"Area of circle with given radius equals {c.area():.2f}.")
print(f"Circumference of circle with given radius equals {c.circumference():.2f}.")

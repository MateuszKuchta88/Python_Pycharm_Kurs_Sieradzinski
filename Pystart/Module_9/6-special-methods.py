# Module 9 - Special methods

# TASK DESCRIPTION
# Prepare special methods for adding objects to each other,
# subtraction and comparing them with each other.

# Import libraries


# Testing data


# Declare function
class LengthUnit:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        total = self.value + other.value
        return LengthUnit(total)

    def __sub__(self, other):
        total = self.value - other.value
        return LengthUnit(total)

    def __eq__(self, other):
        return self.value == other.value

    def to_centimeter(self):
        return self.value / 10

    def to_meter(self):
        return self.value / 10 / 100

# Tests


# Print output message

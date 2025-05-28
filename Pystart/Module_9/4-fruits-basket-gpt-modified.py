# Module 9 - Basket with fruits (gpt modified)

# TASK DESCRIPTION
# Zosia was walking in the meadow and picking apples.
# Each fruit has:
#  color e.g. red, green, yellow,
#  taste e.g. sweet, sour
#  type e.g. ripe, unripe.
# Prepare a Basket object to which you can add fruits and
# generate a report according to a given feature. e.g. number of fruits by colors.
# Ideally, the report would also be an object :)

from dataclasses import dataclass
from random import choice
from typing import Dict, List

@dataclass
class Apple:
    """
    Represents an Apple with specific characteristics.

    Attributes:
        color (str): The color of the apple (e.g., red, green, yellow).
        taste (str): The taste of the apple (e.g., sweet, sour).
        apple_type (str): The type of the apple (e.g., ripe, unripe).
    """
    color: str
    taste: str
    apple_type: str

class Basket:
    """
    Represents a basket containing apples.

    Methods:
        add_apple(apple: Apple): Adds an Apple object to the basket.
        get_apples() -> List[Apple]: Returns the list of apples in the basket.
    """

    def __init__(self):
        self.apples: List[Apple] = []

    def add_apple(self, apple: Apple):
        """Adds an Apple to the basket."""
        self.apples.append(apple)

    def get_apples(self) -> List[Apple]:
        """Returns the list of apples in the basket."""
        return self.apples

class Report:
    """
    Generates reports based on a feature of the apples in the basket.

    Methods:
        generate_report(basket: Basket, feature: str) -> Dict[str, int]:
            Generates a statistical report for the given feature.
    """

    def __init__(self):
        self._statistics = None

    def generate_report(self, apple_basket: Basket, feature: str) -> Dict[str, int]:
        """
        Generates a report of apple statistics based on the specified feature.

        Args:
            apple_basket (Basket): The basket containing apples to analyze.
            feature (str): The feature to generate the report on (e.g., 'color', 'taste', 'apple_type').

        Returns:
            Dict[str, int]: A dictionary with the feature as keys and counts as values.
        """
        self._statistics = {}
        for apple in apple_basket.get_apples():
            key = getattr(apple, feature, None)
            if key is not None:
                self._statistics[key] = self._statistics.get(key, 0) + 1
        return self._statistics

# Testing Data
if __name__ == "__main__":
    colors = ['red', 'green', 'yellow']
    tastes = ['sweet', 'sour']
    apple_types = ['ripe', 'unripe']

    # Create a basket and populate it with random apples
    basket = Basket()
    for _ in range(100):
        basket.add_apple(Apple(
            color=choice(colors),
            taste=choice(tastes),
            apple_type=choice(apple_types)
        ))

    # Generate and display reports
    report = Report()

    print("Report by Color:")
    print(report.generate_report(basket, 'color'))

    print("\nReport by Taste:")
    print(report.generate_report(basket, 'taste'))

    print("\nReport by Apple Type:")
    print(report.generate_report(basket, 'apple_type'))

# Unit Tests
import unittest

class TestBasketWithFruits(unittest.TestCase):

    def setUp(self):
        self.basket = Basket()
        self.basket.add_apple(Apple("red", "sweet", "ripe"))
        self.basket.add_apple(Apple("green", "sour", "unripe"))
        self.basket.add_apple(Apple("red", "sweet", "ripe"))
        self.report = Report()

    def test_generate_report_by_color(self):
        expected = {"red": 2, "green": 1}
        self.assertEqual(self.report.generate_report(self.basket, "color"), expected)

    def test_generate_report_by_taste(self):
        expected = {"sweet": 2, "sour": 1}
        self.assertEqual(self.report.generate_report(self.basket, "taste"), expected)

    def test_generate_report_by_type(self):
        expected = {"ripe": 2, "unripe": 1}
        self.assertEqual(self.report.generate_report(self.basket, "apple_type"), expected)

if __name__ == "__main__":
    unittest.main()

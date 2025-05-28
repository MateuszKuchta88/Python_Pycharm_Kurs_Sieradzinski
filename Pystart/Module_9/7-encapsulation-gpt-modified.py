# Module 9 - Encapsulation (gpt modified)

# TASK DESCRIPTION
# Prepare a program that will store a shopping list. Every entry
# is a separate object of the ListItem class. If a given product is already on
# the list should not be added a second time, instead it should be
# its quantity is increased. Store products to be purchased in a variable
# private.
# An object of the List class must have the following methods:
#  addItem(product: Product, quantity: float)
#  removeItem(product:Product, quantity: float)
#  listItems(): list
#  calculateTotalCost()
# Each Product class object has a price and a name

# Import libraries
from typing import Dict, List


class Product:
    """
    Represents a product with a price and a name.

    Attributes:
        price (float): The price of the product.
        name (str): The name of the product.
    """

    def __init__(self, price: float, name: str):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = price
        self.name = name

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"


class ProductsList:
    """
    Represents a shopping list that stores products and their quantities.

    Attributes:
        _products (Dict[str, int]): A private dictionary to store product names and their quantities.
        _total_cost (float): The total cost of all products in the list.
    """

    def __init__(self):
        self._products: Dict[str, int] = {}
        self._total_cost: float = 0.0

    def __str__(self):
        return f"Products: {self._products}, Total cost: ${self._total_cost:.2f}"

    def add_item(self, product: Product, quantity: int):
        """
        Adds a product to the list or updates its quantity.

        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product to add.

        Raises:
            ValueError: If the quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if product.name in self._products:
            self._products[product.name] += quantity
        else:
            self._products[product.name] = quantity

        self._total_cost += product.price * quantity

    def remove_item(self, product: Product, quantity: int):
        """
        Removes a product or decreases its quantity in the list.

        Args:
            product (Product): The product to remove.
            quantity (int): The quantity to remove.

        Raises:
            ValueError: If the product is not in the list or if the quantity is invalid.
        """
        if product.name not in self._products:
            raise ValueError(f"Product '{product.name}' not found in the list.")

        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if self._products[product.name] < quantity:
            raise ValueError(f"Cannot remove {quantity} units of '{product.name}'. Only {self._products[product.name]} available.")

        self._products[product.name] -= quantity
        self._total_cost -= product.price * quantity

        if self._products[product.name] == 0:
            del self._products[product.name]

    def list_items(self) -> List[str]:
        """
        Lists all products and their quantities.

        Returns:
            List[str]: A list of strings describing the products and their quantities.
        """
        return [f"{name}: {quantity}" for name, quantity in self._products.items()]

    def calculate_total_cost(self) -> float:
        """
        Returns the total cost of all products in the list.

        Returns:
            float: The total cost.
        """
        return self._total_cost


# Unit Tests
def run_tests():
    # Create products
    apple = Product(0.8, 'apple')
    banana = Product(1.2, 'banana')
    cookies = Product(4.1, 'cookies')
    milk = Product(3.5, 'milk')

    # Initialize product list
    shopping_list = ProductsList()

    # Test adding items
    shopping_list.add_item(apple, 3)
    shopping_list.add_item(banana, 2)
    shopping_list.add_item(cookies, 1)
    assert shopping_list.calculate_total_cost() == 8.9, "Total cost calculation failed."

    # Test removing items
    shopping_list.remove_item(apple, 1)
    assert 'apple: 2' in shopping_list.list_items(), "Apple quantity update failed."

    shopping_list.remove_item(banana, 2)
    assert 'banana: 2' not in shopping_list.list_items(), "Banana removal failed."

    # Test invalid operations
    try:
        shopping_list.remove_item(milk, 1)
    except ValueError as e:
        assert str(e) == "Product 'milk' not found in the list.", "Error handling failed for removing non-existent product."

    try:
        shopping_list.add_item(cookies, 0)
    except ValueError as e:
        assert str(e) == "Quantity must be positive.", "Error handling failed for adding zero quantity."

    print("All tests passed.")


# Run tests

run_tests()

# Module 9 - Encapsulation

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


# Declare function
class Product:
    def __init__(self, price: float, name: str):
        self.price = price
        self.name = name


class ProductsList:
    def __init__(self):
        self.products = {}
        self._total_cost = 0

    def __str__(self):
        return f'{self.products}, total cost = {self._total_cost}'

    def calculate_total_cost(self, product: Product, quantity: int):
        self._total_cost += product.price * quantity

    def add_item(self, product: Product, quantity: int):
        self.products.update({product.name: self.products.get(product.name, 0) + quantity})
        self.calculate_total_cost(product, quantity)

    def remove_item(self, product: Product, quantity: int):
        if self.products[product.name] > quantity:
            self.products.update({product.name: self.products[product.name] - quantity})
        elif self.products[product.name] == quantity:
            self.products.pop(product.name)
        else:
            print(f'No product {product.name} in products list.')
            return
        self.calculate_total_cost(product, -1 * quantity)

    def list_items(self):
        return print(self.products)


# Tests
prod_1 = Product(0.8, 'apple')
prod_2 = Product(1.2, 'banana')
prod_3 = Product(4.1, 'cookies')
prod_4 = Product(3.5, 'milk')
prod_5 = Product(9.3, 'ham')
pl = ProductsList()
pl.add_item(prod_1, 3)
pl.add_item(prod_2, 4)
pl.add_item(prod_3, 2)
pl.add_item(prod_4, 1)
pl.add_item(prod_5, 2)
pl.add_item(prod_2, 0)
pl.add_item(prod_4, 2)
pl.remove_item(prod_1, 1)
pl.remove_item(prod_4, 4)
pl.remove_item(prod_4, 3)
pl.list_items()


# Print output message
print(pl)
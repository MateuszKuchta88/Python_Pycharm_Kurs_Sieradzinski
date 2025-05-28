# PD8 2 - Shopping list (chat GPT improved initial code)

# TASK DESCRIPTION
# Ask the user for product names until he writes "end".
#  Then save to a file named ddmmyyyy.txt
#  only the unique names of the products he introduced.

import datetime
from pathlib import Path


def load_existing_shopping_list(file_path):
    """
    Load the existing shopping list from a file, if it exists.
    Args:
        file_path (Path): The path to the file containing the shopping list.
    Returns:
        set: A set of unique product names from the file.
    """
    if file_path.exists():
        with file_path.open('r', encoding='utf8') as file:
            return {line.strip() for line in file}
    return set()


def save_shopping_list(file_path, shopping_list):
    """
    Save the shopping list to a file.
    Args:
        file_path (Path): The path to the file where the shopping list will be saved.
        shopping_list (set): A set of unique product names to be written to the file.
    """
    with file_path.open('w', encoding='utf8') as file:
        for product in shopping_list:
            file.write(f"{product}\n")


def get_user_input():
    """
    Continuously prompt the user to input product names for the shopping list.
    The user can type 'end' (case-insensitive) to finish the input process.
    Duplicate entries are automatically removed by using a set.
    Returns:
        set: A set of product names entered by the user.
    """
    shopping_list = set()
    while True:
        product = input("Enter a product name (or type 'end' to finish): ").strip()
        if product.lower() == 'end':
            break
        shopping_list.add(product)
    return shopping_list


def main():
    """
    The main function that orchestrates the shopping list program.
    It:
    - Loads an existing shopping list from a file based on the current date.
    - Prompts the user to input additional products.
    - Updates the shopping list with new products.
    - Saves the updated shopping list back to the file.
    - Prints confirmation and the final list path.
    """
    today = datetime.date.today().strftime('%d%m%Y')
    file_path = Path(f"{today}.txt")

    # Load existing shopping list
    shopping_list = load_existing_shopping_list(file_path)
    print(f"Current shopping list: {shopping_list}")

    # Get user input
    new_products = get_user_input()
    shopping_list.update(new_products)

    # Save the updated shopping list
    save_shopping_list(file_path, shopping_list)
    print(f"Shopping list saved to {file_path}")


if __name__ == "__main__":
    main()

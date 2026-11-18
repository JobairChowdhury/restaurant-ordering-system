"""
menu.py
-------
This module stores the restaurant menu and the functions related to it.

Requirement shown here:
- Dictionaries (the MENU uses a dictionary inside a dictionary)
- Data types (str for names, float for prices, int for item codes)
- Functions
"""

# Name of the restaurant (string variable)
RESTAURANT_NAME = "Python Bites Restaurant"

# Service tax rate (float variable) - 6% tax
TAX_RATE = 0.06

# The menu is a dictionary.
# Key   -> item code (int)
# Value -> another dictionary holding the item's name, price and category
MENU = {
    1: {"name": "Nasi Lemak", "price": 8.50, "category": "Main"},
    2: {"name": "Chicken Rice", "price": 7.00, "category": "Main"},
    3: {"name": "Fried Noodles", "price": 9.00, "category": "Main"},
    4: {"name": "Beef Burger", "price": 12.50, "category": "Main"},
    5: {"name": "French Fries", "price": 5.00, "category": "Side"},
    6: {"name": "Chicken Wings (6 pcs)", "price": 10.00, "category": "Side"},
    7: {"name": "Iced Lemon Tea", "price": 3.50, "category": "Drink"},
    8: {"name": "Teh Tarik", "price": 2.80, "category": "Drink"},
    9: {"name": "Mineral Water", "price": 1.50, "category": "Drink"},
    10: {"name": "Chocolate Cake", "price": 6.50, "category": "Dessert"},
}


def display_menu():
    """Print the full menu in a neat table."""
    print("\n" + "=" * 50)
    print(f"{RESTAURANT_NAME:^50}")
    print("=" * 50)
    print(f"{'Code':<6}{'Item':<26}{'Category':<10}{'Price (RM)':>8}")
    print("-" * 50)

    # Loop through every item in the menu dictionary
    for code, item in MENU.items():
        print(f"{code:<6}{item['name']:<26}{item['category']:<10}{item['price']:>8.2f}")

    print("=" * 50)


def is_valid_item(code):
    """Return True if the item code exists in the menu, otherwise False."""
    return code in MENU


def get_item(code):
    """Return the item dictionary for a given code (or None if not found)."""
    return MENU.get(code)

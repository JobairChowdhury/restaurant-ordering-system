"""
order.py
--------
Functions that manage the customer's order (the "cart").

The order is stored as a dictionary:
    key   -> item code (int)
    value -> quantity ordered (int)
Example: {1: 2, 7: 1}  means 2 x Nasi Lemak and 1 x Iced Lemon Tea

Requirement shown here:
- Functions (add, remove, view, calculate, receipt)
- Lists and dictionaries
- Loops and decision making
"""

from menu import MENU, TAX_RATE, RESTAURANT_NAME, display_menu, is_valid_item, get_item
from utils import get_int_input, get_float_input, get_yes_no


def add_item(order):
    """Ask the user which item and how many, then add it to the order."""
    display_menu()
    code = get_int_input("Enter item code to add: ", 1, max(MENU.keys()))

    # Extra safety check (decision making)
    if not is_valid_item(code):
        print("  [Error] That item code does not exist.")
        return

    quantity = get_int_input("Enter quantity (1-20): ", 1, 20)

    # If the item is already in the order, increase the quantity
    if code in order:
        order[code] += quantity
    else:
        order[code] = quantity

    item = get_item(code)
    print(f"  Added {quantity} x {item['name']} to your order.")


def remove_item(order):
    """Remove an item (or reduce its quantity) from the order."""
    if not order:  # an empty dictionary counts as False
        print("  Your order is empty. Nothing to remove.")
        return

    view_order(order)
    code = get_int_input("Enter item code to remove: ", 1, max(MENU.keys()))

    if code not in order:
        print("  [Error] That item is not in your order.")
        return

    current_qty = order[code]
    qty_to_remove = get_int_input(f"How many to remove (1-{current_qty}): ", 1, current_qty)

    order[code] -= qty_to_remove
    if order[code] == 0:
        del order[code]  # remove the item completely

    print(f"  Removed {qty_to_remove} x {get_item(code)['name']}.")


def calculate_totals(order):
    """
    Work out subtotal, tax and grand total.
    Returns the three values as a tuple.
    """
    subtotal = 0.0
    for code, quantity in order.items():
        subtotal += MENU[code]["price"] * quantity

    tax = subtotal * TAX_RATE
    total = subtotal + tax
    return subtotal, tax, total


def view_order(order):
    """Show what is currently in the order with prices."""
    if not order:
        print("  Your order is empty.")
        return

    print("\n" + "-" * 50)
    print("YOUR CURRENT ORDER")
    print("-" * 50)
    print(f"{'Code':<6}{'Item':<24}{'Qty':>5}{'Amount (RM)':>15}")

    for code, quantity in order.items():
        item = MENU[code]
        line_total = item["price"] * quantity
        print(f"{code:<6}{item['name']:<24}{quantity:>5}{line_total:>15.2f}")

    subtotal, tax, total = calculate_totals(order)
    print("-" * 50)
    print(f"{'Subtotal:':<35}{subtotal:>15.2f}")
    print(f"{'Service tax (6%):':<35}{tax:>15.2f}")
    print(f"{'TOTAL:':<35}{total:>15.2f}")
    print("-" * 50)


def checkout(order, customer_name, order_history):
    """
    Take payment, print the receipt and save the order to history.
    Returns True if checkout finished, False if cancelled.
    """
    if not order:
        print("  Your order is empty. Please add items first.")
        return False

    view_order(order)
    if not get_yes_no("Confirm and pay for this order? (y/n): "):
        print("  Checkout cancelled.")
        return False

    subtotal, tax, total = calculate_totals(order)

    # Ask for payment until the customer gives enough money
    cash = get_float_input(f"Total is RM {total:.2f}. Enter cash amount: RM ")
    while cash < total:
        print(f"  [Error] Not enough. You still need RM {total - cash:.2f} more.")
        cash = get_float_input("Enter cash amount again: RM ")

    change = cash - total
    print_receipt(order, customer_name, subtotal, tax, total, cash, change)

    # Save a copy of this order to the history list
    order_history.append({
        "customer": customer_name,
        "items": dict(order),  # copy, so clearing the order does not erase history
        "total": total,
    })

    order.clear()  # empty the cart for the next order
    return True


def print_receipt(order, customer_name, subtotal, tax, total, cash, change):
    """Print the final receipt."""
    print("\n" + "*" * 50)
    print(f"{RESTAURANT_NAME:^50}")
    print(f"{'OFFICIAL RECEIPT':^50}")
    print("*" * 50)
    print(f"Customer: {customer_name}")
    print("-" * 50)

    for code, quantity in order.items():
        item = MENU[code]
        print(f"{quantity} x {item['name']:<30}RM {item['price'] * quantity:>8.2f}")

    print("-" * 50)
    print(f"{'Subtotal:':<38}RM {subtotal:>8.2f}")
    print(f"{'Service tax (6%):':<38}RM {tax:>8.2f}")
    print(f"{'TOTAL:':<38}RM {total:>8.2f}")
    print(f"{'Cash paid:':<38}RM {cash:>8.2f}")
    print(f"{'Change:':<38}RM {change:>8.2f}")
    print("*" * 50)
    print(f"{'Thank you! Please come again.':^50}")
    print("*" * 50)


def show_history(order_history):
    """Show all orders that were paid during this session (uses a list)."""
    if len(order_history) == 0:
        print("  No orders have been completed yet.")
        return

    print("\n" + "=" * 50)
    print("ORDER HISTORY (this session)")
    print("=" * 50)

    grand_total = 0.0
    # enumerate gives us a counter (1, 2, 3...) together with each order
    for number, past_order in enumerate(order_history, start=1):
        item_count = sum(past_order["items"].values())
        print(f"#{number}  {past_order['customer']:<20}{item_count:>3} item(s)   RM {past_order['total']:>8.2f}")
        grand_total += past_order["total"]

    print("-" * 50)
    print(f"Total sales: RM {grand_total:.2f}")
    print("=" * 50)

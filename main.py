"""
main.py
-------
Restaurant Ordering System - START THE PROGRAM FROM THIS FILE.

"""

from menu import display_menu, RESTAURANT_NAME
from order import add_item, remove_item, view_order, checkout, show_history
from utils import get_int_input, get_non_empty_text, get_yes_no


def show_main_menu():
    """Print the list of options the user can choose from."""
    print("\n========== MAIN MENU ==========")
    print("1. View food menu")
    print("2. Add item to order")
    print("3. Remove item from order")
    print("4. View current order")
    print("5. Checkout and pay")
    print("6. View order history")
    print("7. Exit")
    print("===============================")


def main():
    """Main program loop."""
    print("*" * 50)
    print(f"Welcome")
    print("*" * 50)

    customer_name = get_non_empty_text("Please enter your name: ")

    order = {}           # current order (dictionary: item code -> quantity)
    order_history = []   # list of completed orders
    running = True       # boolean that controls the main loop

    while running:
        show_main_menu()
        choice = get_int_input("Choose an option (1-7): ", 1, 7)

        # Decision making: run the function that matches the choice
        if choice == 1:
            display_menu()
        elif choice == 2:
            add_item(order)
        elif choice == 3:
            remove_item(order)
        elif choice == 4:
            view_order(order)
        elif choice == 5:
            paid = checkout(order, customer_name, order_history)
            # After paying, allow a new customer to order
            if paid and get_yes_no("Is there a new customer? (Yes/No): "):
                customer_name = get_non_empty_text("Enter new customer's name: ")
        elif choice == 6:
            show_history(order_history)
        elif choice == 7:
            # Warn the user if they still have unpaid items
            if order and not get_yes_no("You have unpaid items. Exit anyway? (YES/NO): "):
                continue
            running = False

    print(f"\nGoodbye, {customer_name}! Thank you for visiting.")


# This makes sure main() only runs when this file is started directly
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Happens if the user presses Ctrl + C
        print("\n\nProgram stopped by user. Goodbye!")

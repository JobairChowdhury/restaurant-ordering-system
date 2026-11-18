"""
utils.py
--------
Helper functions for reading and checking what the user types.

Requirement shown here:
- Input and output
- Error handling (try / except for basic validation)
- Loops (keep asking until the input is valid)
- Decision making (if / else)
"""


def get_int_input(prompt, min_value=None, max_value=None):
    """
    Ask the user for a whole number.
    Keeps asking until the user enters a valid number within the allowed range.
    """
    while True:
        user_input = input(prompt).strip()

        try:
            number = int(user_input)  # may raise ValueError, e.g. "abc"
        except ValueError:
            print("  [Error] Please enter a whole number (e.g. 1, 2, 3).")
            continue  # go back to the top of the loop and ask again

        # Check the range
        if min_value is not None and number < min_value:
            print(f"  [Error] Number must be at least {min_value}.")
        elif max_value is not None and number > max_value:
            print(f"  [Error] Number must not be more than {max_value}.")
        else:
            return number  # valid input -> leave the loop


def get_float_input(prompt, min_value=0.0):
    """Ask the user for a decimal number (used for cash payment)."""
    while True:
        user_input = input(prompt).strip()

        try:
            number = float(user_input)
        except ValueError:
            print("  [Error] Please enter a valid amount (e.g. 50 or 50.00).")
            continue

        if number < min_value:
            print(f"  [Error] Amount must be at least RM {min_value:.2f}.")
        else:
            return number


def get_non_empty_text(prompt):
    """Ask for text and make sure the user does not leave it empty."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("  [Error] This field cannot be empty.")
        else:
            return text


def get_yes_no(prompt):
    """Ask a yes/no question. Returns True for yes and False for no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  [Error] Please type 'y' for yes or 'n' for no.")

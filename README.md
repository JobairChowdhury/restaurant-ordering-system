# Restaurant Ordering System (Python)

A simple menu-driven Restaurant Ordering System written in Python for the
**Applied Python Programming** assignment.

## Features
- View the food menu with prices
- Add items to an order (with quantity)
- Remove items from an order
- View the current order with subtotal, 6% service tax and total
- Checkout with cash payment and change calculation
- Print a receipt
- View order history and total sales for the session
- Input validation (wrong inputs do not crash the program)

## Project Files
| File | Purpose |
|------|---------|
| `main.py`  | Starts the program and shows the main menu (menu-driven interface) |
| `menu.py`  | Stores the restaurant menu (dictionary) and menu functions |
| `order.py` | Functions to add, remove, view, calculate and checkout orders |
| `utils.py` | Input helper functions with error handling (try/except) |

## How to Run
1. Install Python 3 from https://www.python.org/downloads/
2. Open a terminal in this folder
3. Run:
   ```
   python main.py
   ```
   (On Mac use `python3 main.py`)

## Requirements Checklist
| Requirement | Where it is used |
|-------------|------------------|
| GitHub repository | This repository |
| Variables and data types | `str`, `int`, `float`, `bool`, `dict`, `list` in all files |
| Input and output | `input()` in `utils.py`, `print()` everywhere |
| Decision making (if/else) | Main menu choice in `main.py`, checks in `order.py` |
| Loops | `while` loop in `main.py` and `utils.py`, `for` loops in `menu.py` / `order.py` |
| Functions (minimum 3) | More than 15 functions, e.g. `add_item()`, `calculate_totals()`, `checkout()` |
| Modular programming (min 2 files) | 4 Python files that import each other |
| Lists and/or dictionaries | `MENU` dictionary, `order` dictionary, `order_history` list |
| Error handling | `try/except ValueError` in `utils.py`, `KeyboardInterrupt` in `main.py` |
| Menu-driven interface | Main menu with options 1–7 in `main.py` |
| Meaningful comments | Docstrings and comments in every file |

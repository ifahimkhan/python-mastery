"""
=====================================================================
 PRACTICE 03.B - Receipt printer
=====================================================================
 GOAL   : Use defaults, keyword-only options and *args to format a
          shop receipt with aligned columns.
 RUN    : uv run python -m course.l03_functions.practice.receipt.receipt
 OUTPUT :
          ******************************
          Coffee                    3.50
          Croissant x 2             5.00
          Orange juice              4.25
          ------------------------------
          Subtotal                 12.75
          Tip (10%)                 1.27
          TOTAL                    14.02
          ******************************
 DESIGN : line() formats one row, subtotal() adds prices, tip() rounds
          down to the cent. main() only glues them together.
 NOTE   : Real money code uses decimal.Decimal instead of float (level 09),
          because floats are approximate (lesson 01.3).
 EXTEND : Add a keyword-only `currency: str = ""` that goes before every price.
=====================================================================
"""

WIDTH = 30
TIP_RATE = 0.10
CENTS = 100
NOISE_DIGITS = 6


def line(label: str, price: float, *, quantity: int = 1, width: int = WIDTH) -> str:
    """One receipt row: label on the left, price on the right."""
    if quantity > 1:
        label = f"{label} x {quantity}"
    amount = f"{price * quantity:.2f}"
    return f"{label:<{width - len(amount)}}{amount}"


def subtotal(*prices: float) -> float:
    total = 0.0
    for price in prices:
        total += price
    return total


def tip(amount: float, rate: float = TIP_RATE) -> float:
    """Tip rounded DOWN to the cent, so the shop never asks for too much."""
    # round() first removes float noise: 0.7 * 0.1 * 100 is 6.999999999999999,
    # and int() alone would turn that into 6 cents instead of 7.
    cents = round(amount * rate * CENTS, NOISE_DIGITS)
    return int(cents) / CENTS


def rule(char: str = "*", width: int = WIDTH) -> str:
    return char * width


def main() -> None:
    coffee, croissant, juice = 3.50, 2.50, 4.25
    croissants = 2

    print(rule())
    print(line("Coffee", coffee))
    print(line("Croissant", croissant, quantity=croissants))
    print(line("Orange juice", juice))
    print(rule("-"))

    before_tip = subtotal(coffee, croissant * croissants, juice)
    tip_amount = tip(before_tip)
    print(line("Subtotal", before_tip))
    print(line(f"Tip ({TIP_RATE:.0%})", tip_amount))
    print(line("TOTAL", before_tip + tip_amount))
    print(rule())


if __name__ == "__main__":
    main()

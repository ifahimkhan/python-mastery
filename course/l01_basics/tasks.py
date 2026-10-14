"""The list of Level 01 exercises.

Both ``exercises/exercises.py`` (your answers) and ``solutions/solutions.py``
(reference answers) implement this Protocol, so the SAME tests check both.

You don't need to understand ``Protocol`` or ``class`` yet (level 06), or the
type hints such as ``-> str`` (level 03). Just read the description of each
method, then fill in its body in exercises/exercises.py.
"""

from typing import Protocol


class BasicsTasks(Protocol):
    def greet(self, name: str) -> str:
        """Ex 1. Return "Hello, <name>!".  greet("Python") == "Hello, Python!" """
        ...

    def seconds_in_days(self, days: int) -> int:
        """Ex 2. Number of seconds in ``days`` days.  seconds_in_days(1) == 86400"""
        ...

    def average(self, a: int, b: int, c: int) -> float:
        """Ex 3. Average of three whole numbers, WITH decimals.  average(1, 2, 2) == 1.666..."""
        ...

    def is_even(self, n: int) -> bool:
        """Ex 4. True if ``n`` is even. Works for negatives and zero too."""
        ...

    def initials(self, first_name: str, last_name: str) -> str:
        """Ex 5. Initials in upper case with dots.  initials("ada", "lovelace") == "A.L."

        Both names are non-empty.
        """
        ...

    def last_digit(self, n: int) -> int:
        """Ex 6. Last digit of ``n``, always 0..9.  last_digit(-147) == 7"""
        ...

    def inches_to_cm(self, inches: float) -> float:
        """Ex 7. Convert inches to centimeters (1 inch = 2.54 cm)."""
        ...

    def describe(self, name: str, age: int) -> str:
        """Ex 8. Describe a person and their age next year.

        describe("Sam", 41) == "Sam is 41 years old and will be 42 next year."
        """
        ...

    def format_price(self, amount: float) -> str:
        """Ex 9. Dollar sign, thousands separators, exactly 2 decimals.

        format_price(1234.5) == "$1,234.50"    format_price(0) == "$0.00"
        """
        ...

    def reverse_text(self, text: str) -> str:
        """Ex 10. The text backwards.  reverse_text("stressed") == "desserts" """
        ...

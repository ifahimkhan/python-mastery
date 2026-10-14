"""
=====================================================================
 LEVEL 01 - EXERCISES (your turn!)
=====================================================================
 HOW    : Replace each `raise NotImplementedError(...)` line with your
          answer, usually a single `return ...` line.
          Keep everything else as it is.
 CHECK  : uv run pytest -m exercise tests/l01_basics
          or open tests/l01_basics/test_exercises.py and click the
          green arrow next to the class name.
 STUCK? : Re-read the lesson in the hint. Still stuck? Peek at
          ../solutions/solutions.py, but try first!
 NOTE   : `class`, `self` and `def` are explained in levels 03 and 06.
          For now, only change the body of each method.
=====================================================================
"""


class BasicsExercises:
    # Hint: lesson05_fstrings (f-strings)
    def greet(self, name: str) -> str:
        raise NotImplementedError('Ex 1: return "Hello, <name>!"')

    # Hint: lesson03_numbers (Python ints never overflow). 1 day = 24 * 60 * 60 seconds.
    def seconds_in_days(self, days: int) -> int:
        raise NotImplementedError("Ex 2: seconds in `days` days")

    # Hint: lesson03_numbers (/ versus //)
    def average(self, a: int, b: int, c: int) -> float:
        raise NotImplementedError("Ex 3: average WITH decimals")

    # Hint: lesson06_operators (% remainder, comparisons give True/False)
    def is_even(self, n: int) -> bool:
        raise NotImplementedError("Ex 4: is n even?")

    # Hint: lesson04_strings (indexing with [0], upper())
    def initials(self, first_name: str, last_name: str) -> str:
        raise NotImplementedError('Ex 5: "A.L." style initials')

    # Hint: lesson06_operators (% with negative numbers) + abs() from lesson03_numbers
    def last_digit(self, n: int) -> int:
        raise NotImplementedError("Ex 6: last digit, never negative")

    # Hint: lesson03_numbers (float math) + lesson02_variables (constants)
    def inches_to_cm(self, inches: float) -> float:
        raise NotImplementedError("Ex 7: 1 inch = 2.54 cm")

    # Hint: lesson05_fstrings (expressions inside {...})
    def describe(self, name: str, age: int) -> str:
        raise NotImplementedError('Ex 8: "Sam is 41 years old and will be 42 next year."')

    # Hint: lesson05_fstrings (format specs: , and .2f)
    def format_price(self, amount: float) -> str:
        raise NotImplementedError('Ex 9: "$1,234.50" style price')

    # Hint: lesson04_strings (slicing with a step)
    def reverse_text(self, text: str) -> str:
        raise NotImplementedError("Ex 10: the text backwards")

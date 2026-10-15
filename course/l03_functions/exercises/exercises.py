"""
=====================================================================
 LEVEL 03 - EXERCISES (your turn!)
=====================================================================
 HOW    : Replace each `raise NotImplementedError(...)` line with your
          answer. Keep the def lines exactly as they are: the parameter
          kinds (defaults, *, *args, **kwargs) are part of the exercise.
 CHECK  : uv run pytest -m exercise tests/l03_functions
          or open tests/l03_functions/test_exercises.py and click the
          green arrow next to the class name.
 STUCK? : Re-read the lesson in the hint. Still stuck? Peek at
          ../solutions/solutions.py, but try first!
 NOTE   : These are methods of a class (level 06), so a method calls
          itself as `self.to_binary(...)`, not `to_binary(...)`.
=====================================================================
"""

from collections.abc import Callable


class FunctionsExercises:
    # Hint: lesson02_defaults (default values)
    def greet(self, name: str, greeting: str = "Hello") -> str:
        raise NotImplementedError('Ex 1: "<greeting>, <name>!"')

    # Hint: lesson03_args_kwargs (*args is a tuple you can loop over)
    def total(self, *numbers: int) -> int:
        raise NotImplementedError("Ex 2: add up all the numbers")

    # Hint: lesson03_args_kwargs (looping over **kwargs with .items())
    def make_tag(self, tag: str, text: str, **attributes: str) -> str:
        raise NotImplementedError('Ex 3: <tag name="value">text</tag>')

    # Hint: lesson04_parameter_kinds (keyword-only flags after *)
    def format_name(self, first: str, last: str, *, upper: bool = False) -> str:
        raise NotImplementedError('Ex 4: "Ada Lovelace" or "ADA LOVELACE"')

    # Hint: lesson01_basics (returning several values) + l01_basics/lesson03_numbers (divmod)
    def split_seconds(self, total_seconds: int) -> tuple[int, int, int]:
        raise NotImplementedError("Ex 5: return hours, minutes, seconds")

    # Hint: lesson06_recursion (binary)
    def to_binary(self, n: int) -> str:
        raise NotImplementedError("Ex 6: binary digits, recursively")

    # Hint: lesson06_recursion (Euclid's gcd)
    def gcd(self, a: int, b: int) -> int:
        raise NotImplementedError("Ex 7: greatest common divisor, recursively")

    # Hint: lesson07_type_hints (X | None) + lesson01_basics (early return)
    def safe_divide(self, a: float, b: float) -> float | None:
        raise NotImplementedError("Ex 8: a / b, or None when b is 0")

    # Hint: lesson07_type_hints (functions as values)
    def apply_twice(self, func: Callable[[int], int], value: int) -> int:
        raise NotImplementedError("Ex 9: func applied twice")

    # Hint: lesson03_args_kwargs (args is a tuple, kwargs a dict: len() works on both)
    def count_args(self, *args: object, **kwargs: object) -> str:
        raise NotImplementedError('Ex 10: "<n> positional, <m> keyword"')

"""The list of Level 03 exercises.

Both ``exercises/exercises.py`` (your answers) and ``solutions/solutions.py``
(reference answers) implement this Protocol, so the SAME tests check both.
Each exercise practises one kind of parameter or return value, so read the
SIGNATURE (the def line) as carefully as the description.
"""

from collections.abc import Callable
from typing import Protocol


class FunctionsTasks(Protocol):
    def greet(self, name: str, greeting: str = "Hello") -> str:
        """Ex 1. greet("Ada") == "Hello, Ada!"   greet("Ada", "Hi") == "Hi, Ada!" """
        ...

    def total(self, *numbers: int) -> int:
        """Ex 2. Sum of any number of arguments.  total(1, 2, 3) == 6, total() == 0"""
        ...

    def make_tag(self, tag: str, text: str, **attributes: str) -> str:
        """Ex 3. An HTML tag with optional attributes, in the order given.

        make_tag("p", "Hi") == "<p>Hi</p>"
        make_tag("a", "Home", href="/") == '<a href="/">Home</a>'
        """
        ...

    def format_name(self, first: str, last: str, *, upper: bool = False) -> str:
        """Ex 4. "Ada Lovelace", or "ADA LOVELACE" when upper=True.

        ``upper`` must be keyword-only: format_name("a", "b", True) is a TypeError.
        """
        ...

    def split_seconds(self, total_seconds: int) -> tuple[int, int, int]:
        """Ex 5. Hours, minutes and seconds.  split_seconds(3725) == (1, 2, 5)"""
        ...

    def to_binary(self, n: int) -> str:
        """Ex 6. Binary digits of n >= 0, using recursion.  to_binary(13) == "1101" """
        ...

    def gcd(self, a: int, b: int) -> int:
        """Ex 7. Greatest common divisor of a, b >= 0, using recursion.  gcd(48, 18) == 6"""
        ...

    def safe_divide(self, a: float, b: float) -> float | None:
        """Ex 8. a / b, or None when b is 0.  safe_divide(1, 4) == 0.25"""
        ...

    def apply_twice(self, func: Callable[[int], int], value: int) -> int:
        """Ex 9. Call ``func`` on ``value``, then on the result.

        apply_twice(lambda n: n + 3, 1) == 7    (lambda: a one-line function, level 07)
        """
        ...

    def count_args(self, *args: object, **kwargs: object) -> str:
        """Ex 10. count_args(1, 2, x=3) == "2 positional, 1 keyword" """
        ...

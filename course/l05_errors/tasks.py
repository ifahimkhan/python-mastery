"""The list of Level 05 exercises.

Both ``exercises/exercises.py`` (your answers) and ``solutions/solutions.py``
(reference answers) implement this Protocol, so the SAME tests check both.
The exception class below is shared: your answers raise it, the tests catch it.
"""

from collections.abc import Callable
from typing import Protocol


class InsufficientFundsError(Exception):
    """Raised by Ex 7 when a withdrawal is larger than the balance."""

    def __init__(self, balance: int, amount: int) -> None:
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        super().__init__(f"need {self.shortfall} more (balance {balance}, asked {amount})")


class ErrorsTasks(Protocol):
    def first_non_none(self, *values: int | None) -> int | None:
        """Ex 1. The first value that is not None, or None if there is none.

        first_non_none(None, 0, 5) == 0    (0 is a real value!)
        """
        ...

    def parse_int(self, text: str) -> int | None:
        """Ex 2. ``text`` as an int, or None if int() can't read it.

        parse_int(" -7 ") == -7    parse_int("seven") is None
        """
        ...

    def divide(self, a: float, b: float) -> float:
        """Ex 3. a / b. Raise ValueError("cannot divide by zero") when b is 0."""
        ...

    def parse_age(self, text: str) -> int:
        """Ex 4. A whole number from 0 to 150.

        Raise ValueError("not a number: <text>") if int() fails, chained with
        `from`, and ValueError("age out of range: <age>") if it is outside 0..150.
        """
        ...

    def safe_sum(self, items: list[str]) -> int:
        """Ex 5. Sum of the items that are whole numbers; skip the rest.

        safe_sum(["1", "x", "2"]) == 3
        """
        ...

    def get_nested(self, data: dict[str, dict[str, int]], outer: str, inner: str) -> int | None:
        """Ex 6. data[outer][inner], or None if either key is missing."""
        ...

    def withdraw(self, balance: int, amount: int) -> int:
        """Ex 7. The new balance. Raise ValueError for a negative amount,
        and InsufficientFundsError(balance, amount) if amount > balance."""
        ...

    def retry(self, func: Callable[[], int], attempts: int) -> int:
        """Ex 8. Call func() until it returns without a ValueError, at most
        ``attempts`` times. Return its result. If every attempt fails,
        re-raise the LAST ValueError. Other exceptions are not retried."""
        ...

    def validate_all(self, values: list[int]) -> None:
        """Ex 9. Raise ExceptionGroup("invalid values", [...]) holding one
        ValueError("negative value at index <i>: <value>") per negative value.
        Do nothing if all values are fine."""
        ...

    def describe_error(self, func: Callable[[], object]) -> str:
        """Ex 10. Call func(). Return "ok" if it worked, otherwise
        "<ExceptionType>: <message>", e.g. "ZeroDivisionError: division by zero".
        Only catch Exception (never BaseException)."""
        ...

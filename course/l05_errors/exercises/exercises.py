"""
=====================================================================
 LEVEL 05 - EXERCISES (your turn!)
=====================================================================
 HOW    : Replace each `raise NotImplementedError(...)` line with your
          answer. Several exercises are ABOUT raising: read the exact
          exception type and message each one asks for in ../tasks.py.
 CHECK  : uv run pytest -m exercise tests/l05_errors
          or open tests/l05_errors/test_exercises.py and click the
          green arrow next to the class name.
 STUCK? : Re-read the lesson in the hint. Still stuck? Peek at
          ../solutions/solutions.py, but try first!
=====================================================================
"""

from collections.abc import Callable

from course.l05_errors.tasks import InsufficientFundsError  # noqa: F401 - you'll need it in Ex 7


class ErrorsExercises:
    # Hint: lesson01_none (`is not None` versus truthiness)
    def first_non_none(self, *values: int | None) -> int | None:
        raise NotImplementedError("Ex 1: first value that is not None")

    # Hint: lesson02_exceptions (try / except ValueError)
    def parse_int(self, text: str) -> int | None:
        raise NotImplementedError("Ex 2: int(text), or None")

    # Hint: lesson03_raising (guard clauses with raise)
    def divide(self, a: float, b: float) -> float:
        raise NotImplementedError('Ex 3: a / b, ValueError("cannot divide by zero")')

    # Hint: lesson03_raising (raise ... from ...)
    def parse_age(self, text: str) -> int:
        raise NotImplementedError("Ex 4: 0..150, two different ValueErrors")

    # Hint: lesson05_eafp_lbyl (EAFP in a loop)
    def safe_sum(self, items: list[str]) -> int:
        raise NotImplementedError("Ex 5: add up the items that are numbers")

    # Hint: lesson05_eafp_lbyl (port_eafp)
    def get_nested(self, data: dict[str, dict[str, int]], outer: str, inner: str) -> int | None:
        raise NotImplementedError("Ex 6: data[outer][inner], or None")

    # Hint: lesson04_custom_exceptions (raising a custom exception with data)
    def withdraw(self, balance: int, amount: int) -> int:
        raise NotImplementedError("Ex 7: new balance, or raise InsufficientFundsError")

    # Hint: lesson03_raising (re-raising) + lesson02_exceptions (except ... as error)
    def retry(self, func: Callable[[], int], attempts: int) -> int:
        raise NotImplementedError("Ex 8: retry on ValueError, re-raise the last one")

    # Hint: lesson06_exception_groups (collect, then raise ExceptionGroup)
    def validate_all(self, values: list[int]) -> None:
        raise NotImplementedError("Ex 9: one ValueError per negative value, in a group")

    # Hint: lesson02_exceptions (except Exception as error, type(error).__name__)
    def describe_error(self, func: Callable[[], object]) -> str:
        raise NotImplementedError('Ex 10: "ok" or "<Type>: <message>"')

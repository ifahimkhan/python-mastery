"""Reference answers for Level 05. Try the exercises first!

Each answer explains WHY it is written this way.
"""

from collections.abc import Callable

from course.l05_errors.tasks import InsufficientFundsError

MIN_AGE = 0
MAX_AGE = 150


class ErrorsSolutions:
    # `is not None`, NOT truthiness: 0 is falsy but it IS a value.
    # `values[0] or values[1]` would skip a 0.
    def first_non_none(self, *values: int | None) -> int | None:
        for value in values:
            if value is not None:
                return value
        return None

    # EAFP: let int() decide what a valid number is (signs, spaces...).
    def parse_int(self, text: str) -> int | None:
        try:
            return int(text)
        except ValueError:
            return None

    # A guard clause with a clear message beats the generic ZeroDivisionError.
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("cannot divide by zero")
        return a / b

    # `from error` keeps int()'s original ValueError as __cause__, so the
    # traceback shows both what we decided and what int() complained about.
    def parse_age(self, text: str) -> int:
        try:
            age = int(text)
        except ValueError as error:
            raise ValueError(f"not a number: {text}") from error
        if not MIN_AGE <= age <= MAX_AGE:
            raise ValueError(f"age out of range: {age}")
        return age

    # The try block holds ONLY the line that can fail; continue skips the rest.
    def safe_sum(self, items: list[str]) -> int:
        total = 0
        for item in items:
            try:
                total += int(item)
            except ValueError:
                continue
        return total

    # One try covers both lookups: a KeyError from either means "missing".
    def get_nested(self, data: dict[str, dict[str, int]], outer: str, inner: str) -> int | None:
        try:
            return data[outer][inner]
        except KeyError:
            return None

    # Check the cheap, generic problem first, then the domain-specific one.
    # The custom exception carries the numbers, so callers don't parse text.
    def withdraw(self, balance: int, amount: int) -> int:
        if amount < 0:
            raise ValueError(f"amount must not be negative, got {amount}")
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
        return balance - amount

    # Remember the last error; re-raise it once every attempt has failed.
    # Only ValueError is caught, so any other error escapes at once.
    def retry(self, func: Callable[[], int], attempts: int) -> int:
        last_error: ValueError | None = None
        for _ in range(attempts):
            try:
                return func()
            except ValueError as error:
                last_error = error
        if last_error is None:
            raise ValueError("attempts must be at least 1")
        raise last_error

    # Collect every problem first, then raise them together.
    def validate_all(self, values: list[int]) -> None:
        problems = [
            ValueError(f"negative value at index {index}: {value}")
            for index, value in enumerate(values)
            if value < 0
        ]
        if problems:
            raise ExceptionGroup("invalid values", problems)

    # `except Exception` (not a bare except) lets Ctrl+C and exit() through.
    def describe_error(self, func: Callable[[], object]) -> str:
        try:
            func()
        except Exception as error:
            return f"{type(error).__name__}: {error}"
        return "ok"

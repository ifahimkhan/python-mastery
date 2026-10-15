"""Shared checks for Level 05.

Subclasses decide WHICH implementation is tested: the learner's exercises
or the reference solutions.
"""

from collections.abc import Callable

import pytest

from course.l05_errors.tasks import ErrorsTasks, InsufficientFundsError


def _fails_then_succeeds(failures: int, result: int) -> tuple[Callable[[], int], list[int]]:
    """A function that raises ValueError `failures` times, then returns `result`.

    The list counts how often it was called.
    """
    calls: list[int] = []

    def flaky() -> int:
        calls.append(1)
        if len(calls) <= failures:
            raise ValueError(f"failure {len(calls)}")
        return result

    return flaky, calls


def _raise_type_error() -> int:
    raise TypeError("not retryable")


def _divide_by_zero() -> object:
    return 1 / 0


def _missing_key() -> object:
    empty: dict[str, int] = {}
    return empty["x"]


def _interrupt() -> object:
    raise KeyboardInterrupt


class ErrorsContract:
    tasks: ErrorsTasks  # set by the subclass

    def test_ex1_first_non_none_keeps_falsy_values(self) -> None:
        assert self.tasks.first_non_none(None, 5, 7) == 5
        assert self.tasks.first_non_none(None, 0, 5) == 0, "Hint: 0 is falsy but NOT None"
        assert self.tasks.first_non_none(None, None) is None
        assert self.tasks.first_non_none() is None, "No values at all: None"

    def test_ex2_parse_int(self) -> None:
        assert self.tasks.parse_int("42") == 42
        assert self.tasks.parse_int(" -7 ") == -7, "Hint: let int() decide; it accepts this"
        assert self.tasks.parse_int("seven") is None
        assert self.tasks.parse_int("") is None
        assert self.tasks.parse_int("4.5") is None

    def test_ex3_divide(self) -> None:
        assert self.tasks.divide(10, 4) == pytest.approx(2.5)
        with pytest.raises(ValueError, match="cannot divide by zero"):
            self.tasks.divide(1, 0)

    def test_ex4_parse_age_accepts_the_valid_range(self) -> None:
        assert self.tasks.parse_age("0") == 0
        assert self.tasks.parse_age("36") == 36
        assert self.tasks.parse_age("150") == 150

    def test_ex4_parse_age_rejects_text_with_a_chained_error(self) -> None:
        with pytest.raises(ValueError, match="not a number: abc") as caught:
            self.tasks.parse_age("abc")
        assert isinstance(caught.value.__cause__, ValueError), (
            "Hint: raise ValueError(...) from error, to keep int()'s error as the cause"
        )

    def test_ex4_parse_age_rejects_out_of_range(self) -> None:
        with pytest.raises(ValueError, match="age out of range: 151"):
            self.tasks.parse_age("151")
        with pytest.raises(ValueError, match="age out of range: -1"):
            self.tasks.parse_age("-1")

    def test_ex5_safe_sum_skips_non_numbers(self) -> None:
        assert self.tasks.safe_sum(["1", "x", "2"]) == 3
        assert self.tasks.safe_sum(["-5", "5", "five"]) == 0
        assert self.tasks.safe_sum([]) == 0

    def test_ex6_get_nested(self) -> None:
        data = {"server": {"port": 8080}}
        assert self.tasks.get_nested(data, "server", "port") == 8080
        assert self.tasks.get_nested(data, "server", "host") is None, "Missing inner key"
        assert self.tasks.get_nested(data, "db", "port") is None, "Missing outer key"

    def test_ex7_withdraw_returns_the_new_balance(self) -> None:
        assert self.tasks.withdraw(100, 30) == 70
        assert self.tasks.withdraw(100, 100) == 0, "Taking everything is allowed"

    def test_ex7_withdraw_raises_the_custom_error(self) -> None:
        with pytest.raises(InsufficientFundsError) as caught:
            self.tasks.withdraw(70, 120)
        assert caught.value.shortfall == 50, "Hint: raise InsufficientFundsError(balance, amount)"

    def test_ex7_withdraw_rejects_negative_amounts(self) -> None:
        with pytest.raises(ValueError):
            self.tasks.withdraw(100, -5)

    def test_ex8_retry_returns_after_failures(self) -> None:
        flaky, calls = _fails_then_succeeds(failures=2, result=42)
        assert self.tasks.retry(flaky, attempts=3) == 42
        assert len(calls) == 3, "Two failures, then one success: three calls"

    def test_ex8_retry_stops_at_the_first_success(self) -> None:
        flaky, calls = _fails_then_succeeds(failures=0, result=7)
        assert self.tasks.retry(flaky, attempts=5) == 7
        assert len(calls) == 1, "Don't call again after it worked"

    def test_ex8_retry_reraises_the_last_error(self) -> None:
        flaky, calls = _fails_then_succeeds(failures=5, result=0)
        with pytest.raises(ValueError, match="failure 3"):
            self.tasks.retry(flaky, attempts=3)
        assert len(calls) == 3, "Hint: stop after `attempts` calls"

    def test_ex8_retry_does_not_retry_other_errors(self) -> None:
        with pytest.raises(TypeError):
            self.tasks.retry(_raise_type_error, attempts=3)

    def test_ex9_validate_all_accepts_good_values(self) -> None:
        self.tasks.validate_all([0, 1, 2])
        self.tasks.validate_all([])

    def test_ex9_validate_all_groups_every_problem(self) -> None:
        with pytest.raises(ExceptionGroup) as caught:
            self.tasks.validate_all([3, -1, 4, -5])
        messages = [str(error) for error in caught.value.exceptions]
        assert messages == ["negative value at index 1: -1", "negative value at index 3: -5"], (
            "Hint: one ValueError per negative value, in order"
        )
        assert all(isinstance(error, ValueError) for error in caught.value.exceptions)

    def test_ex10_describe_error(self) -> None:
        assert self.tasks.describe_error(lambda: 1) == "ok"
        assert self.tasks.describe_error(_divide_by_zero) == "ZeroDivisionError: division by zero"
        assert self.tasks.describe_error(_missing_key) == "KeyError: 'x'", (
            "Hint: f'{type(error).__name__}: {error}'"
        )

    def test_ex10_describe_error_lets_keyboard_interrupt_through(self) -> None:
        # Checked after the normal cases, so an unsolved stub can't pass it.
        self.tasks.describe_error(lambda: 1)
        with pytest.raises(KeyboardInterrupt):
            self.tasks.describe_error(_interrupt)

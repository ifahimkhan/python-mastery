"""Shared checks for Level 01.

Subclasses decide WHICH implementation is tested: the learner's exercises
or the reference solutions.
"""

import pytest

from course.l01_basics.tasks import BasicsTasks


class BasicsContract:
    tasks: BasicsTasks  # set by the subclass

    def test_ex1_greet_builds_a_greeting(self) -> None:
        assert self.tasks.greet("Python") == "Hello, Python!", "Hint: f'Hello, {name}!'"
        assert self.tasks.greet("") == "Hello, !", "An empty name still gets the punctuation"

    def test_ex2_seconds_in_days_handles_big_values(self) -> None:
        assert self.tasks.seconds_in_days(1) == 86_400, "Hint: 1 day = 24 * 60 * 60 seconds"
        assert self.tasks.seconds_in_days(0) == 0, "Zero days have zero seconds"
        assert self.tasks.seconds_in_days(30_000) == 2_592_000_000, "Hint: days * 86400"

    def test_ex3_average_keeps_decimals(self) -> None:
        assert self.tasks.average(1, 2, 3) == pytest.approx(2.0)
        assert self.tasks.average(1, 2, 2) == pytest.approx(5 / 3), (
            "Hint: // drops the decimals, / keeps them"
        )
        assert self.tasks.average(-1, -1, -1) == pytest.approx(-1.0), "Negatives work too"
        assert isinstance(self.tasks.average(1, 2, 3), float), "Hint: / always gives a float"

    def test_ex4_is_even_handles_negatives_and_zero(self) -> None:
        assert self.tasks.is_even(0) is True, "Zero is even"
        assert self.tasks.is_even(10) is True
        assert self.tasks.is_even(-4) is True, "Negative numbers can be even"
        assert self.tasks.is_even(7) is False
        assert self.tasks.is_even(-3) is False, "Hint: compare n % 2 with 0"

    def test_ex5_initials_are_upper_case_with_dots(self) -> None:
        assert self.tasks.initials("ada", "lovelace") == "A.L.", "Hint: name[0].upper()"
        assert self.tasks.initials("Grace", "Hopper") == "G.H."
        assert self.tasks.initials("x", "y") == "X.Y.", "One-letter names work too"

    def test_ex6_last_digit_is_never_negative(self) -> None:
        assert self.tasks.last_digit(123) == 3
        assert self.tasks.last_digit(0) == 0
        assert self.tasks.last_digit(7) == 7
        assert self.tasks.last_digit(-147) == 7, "Hint: -147 % 10 == 3 in Python; use abs() first"

    def test_ex7_inches_to_cm_converts(self) -> None:
        assert self.tasks.inches_to_cm(1.0) == pytest.approx(2.54)
        assert self.tasks.inches_to_cm(12.0) == pytest.approx(30.48), "Hint: inches * 2.54"
        assert self.tasks.inches_to_cm(0.0) == pytest.approx(0.0)

    def test_ex8_describe_uses_an_expression(self) -> None:
        assert self.tasks.describe("Sam", 41) == "Sam is 41 years old and will be 42 next year.", (
            "Hint: put {age + 1} inside the f-string"
        )
        assert self.tasks.describe("Mia", 0) == "Mia is 0 years old and will be 1 next year."

    def test_ex9_format_price_uses_separators_and_two_decimals(self) -> None:
        assert self.tasks.format_price(1234.5) == "$1,234.50", "Hint: f'${amount:,.2f}'"
        assert self.tasks.format_price(0) == "$0.00", "Zero still shows two decimals"
        assert self.tasks.format_price(1_000_000) == "$1,000,000.00"
        assert self.tasks.format_price(9.999) == "$10.00", "Hint: .2f rounds to 2 decimals"

    def test_ex10_reverse_text_walks_backwards(self) -> None:
        assert self.tasks.reverse_text("stressed") == "desserts", "Hint: a slice with step -1"
        assert self.tasks.reverse_text("") == "", "Empty text reversed is still empty"
        assert self.tasks.reverse_text("a") == "a"

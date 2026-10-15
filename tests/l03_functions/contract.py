"""Shared checks for Level 03.

Subclasses decide WHICH implementation is tested: the learner's exercises
or the reference solutions.
"""

import pytest

from course.l03_functions.tasks import FunctionsTasks


def _add_three(n: int) -> int:
    return n + 3


def _square(n: int) -> int:
    return n * n


class FunctionsContract:
    tasks: FunctionsTasks  # set by the subclass

    def test_ex1_greet_has_a_default_greeting(self) -> None:
        assert self.tasks.greet("Ada") == "Hello, Ada!", "Hint: greeting defaults to 'Hello'"
        assert self.tasks.greet("Ada", "Hi") == "Hi, Ada!"
        assert self.tasks.greet(name="Grace", greeting="Hey") == "Hey, Grace!"

    def test_ex2_total_takes_any_number_of_arguments(self) -> None:
        assert self.tasks.total() == 0, "Hint: no arguments means an empty tuple: total 0"
        assert self.tasks.total(5) == 5
        assert self.tasks.total(1, 2, 3) == 6
        assert self.tasks.total(-1, 1, -1) == -1

    def test_ex3_make_tag_without_attributes(self) -> None:
        assert self.tasks.make_tag("p", "Hi") == "<p>Hi</p>"
        assert self.tasks.make_tag("b", "") == "<b></b>"

    def test_ex3_make_tag_keeps_attribute_order(self) -> None:
        assert self.tasks.make_tag("a", "Home", href="/") == '<a href="/">Home</a>', (
            'Hint: each attribute becomes  name="value"  with a space in front'
        )
        result = self.tasks.make_tag("img", "", src="cat.png", alt="A cat")
        assert result == '<img src="cat.png" alt="A cat"></img>', "Keep the order given"

    def test_ex4_format_name_with_a_keyword_only_flag(self) -> None:
        assert self.tasks.format_name("Ada", "Lovelace") == "Ada Lovelace"
        assert self.tasks.format_name("Ada", "Lovelace", upper=True) == "ADA LOVELACE"
        # Checked last: the unsolved stub already has the *, so this part alone
        # would pass before the exercise is done.
        try:
            self.tasks.format_name("Ada", "Lovelace", True)  # type: ignore[call-arg]
        except TypeError:
            pass
        else:
            pytest.fail("Hint: keep the bare * before `upper` so it is keyword-only")

    def test_ex5_split_seconds_returns_three_values(self) -> None:
        assert self.tasks.split_seconds(3725) == (1, 2, 5), "Hint: divmod by 3600, then by 60"
        assert self.tasks.split_seconds(0) == (0, 0, 0)
        assert self.tasks.split_seconds(59) == (0, 0, 59)
        assert self.tasks.split_seconds(86_399) == (23, 59, 59)

    def test_ex6_to_binary(self) -> None:
        assert self.tasks.to_binary(0) == "0", "Hint: base case for n < 2"
        assert self.tasks.to_binary(1) == "1"
        assert self.tasks.to_binary(2) == "10"
        assert self.tasks.to_binary(13) == "1101"
        assert self.tasks.to_binary(255) == "11111111"

    def test_ex7_gcd(self) -> None:
        assert self.tasks.gcd(48, 18) == 6
        assert self.tasks.gcd(18, 48) == 6, "Order doesn't matter"
        assert self.tasks.gcd(7, 0) == 7, "Hint: gcd(a, 0) == a is the base case"
        assert self.tasks.gcd(17, 5) == 1
        assert self.tasks.gcd(0, 0) == 0

    def test_ex8_safe_divide_returns_none_for_zero(self) -> None:
        assert self.tasks.safe_divide(1, 4) == pytest.approx(0.25)
        assert self.tasks.safe_divide(-9, 3) == pytest.approx(-3.0)
        assert self.tasks.safe_divide(1, 0) is None, "Hint: check b == 0 before dividing"
        assert self.tasks.safe_divide(0, 5) == pytest.approx(0.0), "0 divided by 5 is fine"

    def test_ex9_apply_twice_calls_the_function_twice(self) -> None:
        assert self.tasks.apply_twice(_add_three, 1) == 7, "Hint: func(func(value))"
        assert self.tasks.apply_twice(_square, 3) == 81

    def test_ex10_count_args(self) -> None:
        assert self.tasks.count_args() == "0 positional, 0 keyword"
        assert self.tasks.count_args(1, 2, x=3) == "2 positional, 1 keyword"
        assert self.tasks.count_args("a", None, [], a=1, b=2) == "3 positional, 2 keyword"

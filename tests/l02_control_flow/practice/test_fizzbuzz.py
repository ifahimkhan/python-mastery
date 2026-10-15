from collections.abc import Callable

import pytest

from course.l02_control_flow.practice.fizzbuzz.fizzbuzz import (
    all_ways_agree,
    fizzbuzz_build,
    fizzbuzz_if,
    fizzbuzz_match,
)

WAYS = [fizzbuzz_if, fizzbuzz_match, fizzbuzz_build]


@pytest.mark.parametrize("fizzbuzz", WAYS, ids=lambda way: way.__name__)
@pytest.mark.parametrize(
    ("n", "expected"),
    [(1, "1"), (3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz"), (30, "FizzBuzz"), (98, "98")],
)
def test_each_way_gives_the_classic_answers(
    fizzbuzz: Callable[[int], str], n: int, expected: str
) -> None:
    assert fizzbuzz(n) == expected


def test_all_ways_agree_up_to_a_thousand() -> None:
    assert all_ways_agree(1000) is True

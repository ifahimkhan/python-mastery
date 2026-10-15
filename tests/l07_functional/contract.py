"""Shared checks for Level 07.

Subclasses decide WHICH implementation is tested: the learner's exercises
or the reference solutions.
"""

import itertools
from collections.abc import Callable, Iterator

import pytest

from course.l07_functional.tasks import FunctionalTasks


def _double(value: int) -> int:
    return value * 2


def _add_one(value: int) -> int:
    return value + 1


def _naturals() -> Iterator[int]:
    return itertools.count(1)


def _counted_square() -> tuple[Callable[[int], int], list[int]]:
    """A squaring function that records every argument it is called with."""
    calls: list[int] = []

    def slow_square(value: int) -> int:
        calls.append(value)
        return value * value

    return slow_square, calls


def _word_maker() -> Callable[[], str]:
    """Returns "w0", then "w1", "w2", ... on each call."""
    numbers = itertools.count()

    def next_word() -> str:
        return f"w{next(numbers)}"

    return next_word


class FunctionalContract:
    tasks: FunctionalTasks  # set by the subclass

    def test_ex1_compose_applies_inner_first(self) -> None:
        assert self.tasks.compose(_double, _add_one)(5) == 12, "Hint: outer(inner(x))"
        assert self.tasks.compose(_add_one, _double)(5) == 11
        assert self.tasks.compose(_double, _double)(0) == 0

    def test_ex2_make_multiplier(self) -> None:
        triple = self.tasks.make_multiplier(3)
        times_zero = self.tasks.make_multiplier(0)
        assert triple(7) == 21
        assert triple(-2) == -6
        assert times_zero(99) == 0, "Hint: each multiplier remembers its own factor"

    def test_ex3_accumulator_keeps_a_running_total(self) -> None:
        acc = self.tasks.make_accumulator()
        assert acc(10) == 10
        assert acc(5) == 15, "Hint: nonlocal total"
        assert acc(-15) == 0

    def test_ex3_accumulators_are_independent(self) -> None:
        first = self.tasks.make_accumulator()
        second = self.tasks.make_accumulator()
        first(100)
        assert second(1) == 1, "Hint: create `total` INSIDE make_accumulator"

    def test_ex4_memoize_calls_once_per_argument(self) -> None:
        slow_square, calls = _counted_square()
        fast = self.tasks.memoize(slow_square)
        assert [fast(3), fast(3), fast(4), fast(3)] == [9, 9, 16, 9]
        assert calls == [3, 4], "Hint: store results in a dict and check it first"

    def test_ex4_memoize_caches_zero_results(self) -> None:
        slow_square, calls = _counted_square()
        fast = self.tasks.memoize(slow_square)
        fast(0)
        fast(0)
        assert calls == [0], "Hint: test `value in results`, not the truthiness of a result"

    def test_ex4_memoize_keeps_the_name(self) -> None:
        slow_square, _ = _counted_square()
        fast = self.tasks.memoize(slow_square)
        assert getattr(fast, "__name__", None) == "slow_square", "Hint: @functools.wraps(func)"

    def test_ex5_repeat_collects_results(self) -> None:
        repeated = self.tasks.repeat(3)(_word_maker())
        assert repeated() == ["w0", "w1", "w2"], "Hint: call func() `times` times"
        assert repeated() == ["w3", "w4", "w5"]
        assert getattr(repeated, "__name__", None) == "next_word", "Hint: @functools.wraps(func)"

    def test_ex5_repeat_rejects_bad_times(self) -> None:
        assert self.tasks.repeat(1)(_word_maker())() == ["w0"]
        with pytest.raises(ValueError):
            self.tasks.repeat(0)

    def test_ex6_countdown(self) -> None:
        assert list(self.tasks.countdown(3)) == [3, 2, 1]
        assert list(self.tasks.countdown(0)) == []
        assert list(self.tasks.countdown(-2)) == []

    def test_ex6_countdown_is_an_iterator(self) -> None:
        countdown = self.tasks.countdown(1)
        assert iter(countdown) is countdown, "Hint: return a generator, or self from __iter__"
        assert next(countdown) == 1
        with pytest.raises(StopIteration):
            next(countdown)

    def test_ex7_fibonacci(self) -> None:
        first_ten = list(itertools.islice(self.tasks.fibonacci(), 10))
        assert first_ten == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_ex7_fibonacci_is_endless(self) -> None:
        hundredth = next(itertools.islice(self.tasks.fibonacci(), 100, None))
        assert hundredth == 354_224_848_179_261_915_075, "Hint: while True: yield ..."

    def test_ex8_flatten(self) -> None:
        assert list(self.tasks.flatten([[1, 2], [], [3]])) == [1, 2, 3]
        assert list(self.tasks.flatten([])) == []
        assert list(self.tasks.flatten([range(3), (7,)])) == [0, 1, 2, 7]

    def test_ex8_flatten_is_lazy(self) -> None:
        flat = self.tasks.flatten([[0], _naturals()])
        assert list(itertools.islice(flat, 4)) == [0, 1, 2, 3], (
            "Hint: yield from, don't build a list (the second iterable never ends)"
        )

    def test_ex9_running_max(self) -> None:
        assert self.tasks.running_max([3, 1, 4, 1, 5]) == [3, 3, 4, 4, 5]
        assert self.tasks.running_max([-5, -9, -2]) == [-5, -5, -2]
        assert self.tasks.running_max([]) == []
        assert self.tasks.running_max(iter([2, 1])) == [2, 2], "Any iterable, not just lists"

    def test_ex10_climb_stairs_small(self) -> None:
        assert [self.tasks.climb_stairs(n) for n in range(6)] == [1, 1, 2, 3, 5, 8]

    def test_ex10_climb_stairs_is_fast(self) -> None:
        assert self.tasks.climb_stairs(90) == 4_660_046_610_375_530_309, (
            "Hint: @functools.cache, or the test times out after 5 seconds"
        )

    def test_ex10_climb_stairs_rejects_negative(self) -> None:
        self.tasks.climb_stairs(1)
        with pytest.raises(ValueError):
            self.tasks.climb_stairs(-1)

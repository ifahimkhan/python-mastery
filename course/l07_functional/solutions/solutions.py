"""Reference answers for Level 07. Try the exercises first!

Each answer explains WHY it is written this way.
"""

import functools
import itertools
from collections.abc import Callable, Iterable, Iterator

from course.l07_functional.tasks import IntFunc


# Ex 10 helper. The cache lives on a module-level function, not on the
# method: @cache on a method would also keep every `self` alive forever.
@functools.cache
def _ways(steps: int) -> int:
    if steps <= 1:
        return 1
    return _ways(steps - 1) + _ways(steps - 2)


class FunctionalSolutions:
    # The inner function captures outer and inner: a closure.
    def compose(self, outer: IntFunc, inner: IntFunc) -> IntFunc:
        def composed(value: int) -> int:
            return outer(inner(value))

        return composed

    # Each call to make_multiplier creates a NEW closure with its own factor.
    def make_multiplier(self, factor: int) -> IntFunc:
        def multiply(value: int) -> int:
            return value * factor

        return multiply

    # nonlocal: we REBIND total, so Python must know it is the outer one.
    def make_accumulator(self) -> IntFunc:
        total = 0

        def add(amount: int) -> int:
            nonlocal total
            total += amount
            return total

        return add

    # The dict is created once per decorated function and captured by wrapper.
    # `in` (not .get) so that a cached result of 0 still counts as cached.
    def memoize(self, func: IntFunc) -> IntFunc:
        results: dict[int, int] = {}

        @functools.wraps(func)
        def wrapper(value: int) -> int:
            if value not in results:
                results[value] = func(value)
            return results[value]

        return wrapper

    # Three layers: repeat(times) -> decorator(func) -> wrapper().
    # The check runs in the outer layer, so a bad `times` fails at once.
    def repeat(self, times: int) -> Callable[[Callable[[], str]], Callable[[], list[str]]]:
        if times < 1:
            raise ValueError(f"times must be at least 1, got {times}")

        def decorator(func: Callable[[], str]) -> Callable[[], list[str]]:
            @functools.wraps(func)
            def wrapper() -> list[str]:
                return [func() for _ in range(times)]

            return wrapper

        return decorator

    # A generator function is the shortest way to write an iterator.
    # (A class with __iter__/__next__ from lesson 04 works too.)
    def countdown(self, start: int) -> Iterator[int]:
        current = start
        while current > 0:
            yield current
            current -= 1

    # Endless is fine: the caller decides how many to take (islice).
    def fibonacci(self) -> Iterator[int]:
        current, following = 0, 1
        while True:
            yield current
            current, following = following, current + following

    # yield from pulls items one at a time, so an endless inner iterable is
    # fine. (itertools.chain.from_iterable(nested) does the same.)
    def flatten(self, nested: Iterable[Iterable[int]]) -> Iterator[int]:
        for inner in nested:
            yield from inner

    # accumulate applies max between the running result and each new item.
    def running_max(self, numbers: Iterable[int]) -> list[int]:
        return list(itertools.accumulate(numbers, max))

    # Ways to reach n = ways to reach n-1 (then 1 step) + n-2 (then 2 steps).
    # Without the cache this makes ~10**18 calls for 90 steps.
    def climb_stairs(self, steps: int) -> int:
        if steps < 0:
            raise ValueError(f"steps must not be negative, got {steps}")
        return _ways(steps)

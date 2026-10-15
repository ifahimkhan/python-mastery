"""The list of Level 07 exercises.

Both ``exercises/exercises.py`` (your answers) and ``solutions/solutions.py``
(reference answers) implement this Protocol, so the SAME tests check both.
Many answers here RETURN A FUNCTION or an ITERATOR instead of a plain value.
"""

from collections.abc import Callable, Iterable, Iterator
from typing import Protocol

IntFunc = Callable[[int], int]  # "a function from int to int", to keep hints short


class FunctionalTasks(Protocol):
    def compose(self, outer: IntFunc, inner: IntFunc) -> IntFunc:
        """Ex 1. A function that computes outer(inner(x)).

        compose(double, add_one)(5) == 12    (add one first, then double)
        """
        ...

    def make_multiplier(self, factor: int) -> IntFunc:
        """Ex 2. A function that multiplies its argument by ``factor``.

        make_multiplier(3)(7) == 21
        """
        ...

    def make_accumulator(self) -> IntFunc:
        """Ex 3. A function that adds each argument to a running total and
        returns the total so far. Each accumulator has its own total.

        acc = make_accumulator(); acc(10) == 10; acc(5) == 15
        """
        ...

    def memoize(self, func: IntFunc) -> IntFunc:
        """Ex 4. A decorator: return a wrapper that calls ``func`` only once
        per argument and remembers the result. Keep func's __name__
        (use functools.wraps)."""
        ...

    def repeat(self, times: int) -> Callable[[Callable[[], str]], Callable[[], list[str]]]:
        """Ex 5. A decorator WITH an argument: the decorated function, when
        called, runs the original ``times`` times and returns the list of
        results. Raise ValueError right away if times < 1. Keep __name__."""
        ...

    def countdown(self, start: int) -> Iterator[int]:
        """Ex 6. An iterator over start, start - 1, ..., 1 (nothing if start < 1).

        list(countdown(3)) == [3, 2, 1]
        """
        ...

    def fibonacci(self) -> Iterator[int]:
        """Ex 7. An ENDLESS iterator over 0, 1, 1, 2, 3, 5, 8, ..."""
        ...

    def flatten(self, nested: Iterable[Iterable[int]]) -> Iterator[int]:
        """Ex 8. Every item of every inner iterable, in order, LAZILY: it must
        work even if an inner iterable is endless.

        list(flatten([[1, 2], [], [3]])) == [1, 2, 3]
        """
        ...

    def running_max(self, numbers: Iterable[int]) -> list[int]:
        """Ex 9. The biggest value seen so far, at each position.

        running_max([3, 1, 4, 1, 5]) == [3, 3, 4, 4, 5]
        """
        ...

    def climb_stairs(self, steps: int) -> int:
        """Ex 10. In how many ways can you climb ``steps`` stairs taking 1 or
        2 at a time? climb_stairs(0) == 1, climb_stairs(3) == 3
        (1+1+1, 1+2, 2+1). Must be fast for 90 steps. Raise ValueError
        for a negative number."""
        ...

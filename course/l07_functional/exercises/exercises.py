"""
=====================================================================
 LEVEL 07 - EXERCISES (your turn!)
=====================================================================
 HOW    : Replace each `raise NotImplementedError(...)` line with your
          answer. Many answers RETURN A FUNCTION: define it inside the
          method with `def`, then `return` it (without calling it).
          For iterators, a method with `yield` is the easiest way.
 CHECK  : uv run pytest -m exercise tests/l07_functional
          or open tests/l07_functional/test_exercises.py and click the
          green arrow next to the class name.
 STUCK? : Re-read the lesson in the hint. Still stuck? Peek at
          ../solutions/solutions.py, but try first!
=====================================================================
"""

import functools  # noqa: F401 - you'll need it in Ex 4, 5 and 10
import itertools  # noqa: F401 - you'll need it in Ex 9
from collections.abc import Callable, Iterable, Iterator

from course.l07_functional.tasks import IntFunc


class FunctionalExercises:
    # Hint: lesson01_higher_order (make_adder returns a function)
    def compose(self, outer: IntFunc, inner: IntFunc) -> IntFunc:
        raise NotImplementedError("Ex 1: return a function computing outer(inner(x))")

    # Hint: lesson02_closures (make_greeter)
    def make_multiplier(self, factor: int) -> IntFunc:
        raise NotImplementedError("Ex 2: return a function that multiplies by factor")

    # Hint: lesson02_closures (make_counter and nonlocal)
    def make_accumulator(self) -> IntFunc:
        raise NotImplementedError("Ex 3: return a function that keeps a running total")

    # Hint: lesson03_decorators (a wrapper + functools.wraps) + l04_collections/lesson03_dicts
    def memoize(self, func: IntFunc) -> IntFunc:
        raise NotImplementedError("Ex 4: a wrapper that remembers results in a dict")

    # Hint: lesson03_decorators (a decorator with arguments: @repeat(times=2))
    def repeat(self, times: int) -> Callable[[Callable[[], str]], Callable[[], list[str]]]:
        raise NotImplementedError("Ex 5: repeat(times) -> decorator(func) -> wrapper()")

    # Hint: lesson04_iterators (Countdown) or lesson05_generators (yield)
    def countdown(self, start: int) -> Iterator[int]:
        raise NotImplementedError("Ex 6: start, start - 1, ..., 1")

    # Hint: lesson05_generators (naturals: an endless generator)
    def fibonacci(self) -> Iterator[int]:
        raise NotImplementedError("Ex 7: yield 0, 1, 1, 2, 3, 5, ... forever")

    # Hint: lesson05_generators (yield from)
    def flatten(self, nested: Iterable[Iterable[int]]) -> Iterator[int]:
        raise NotImplementedError("Ex 8: every item of every inner iterable, lazily")

    # Hint: lesson06_itertools (accumulate with max)
    def running_max(self, numbers: Iterable[int]) -> list[int]:
        raise NotImplementedError("Ex 9: the biggest value so far, at each position")

    # Hint: lesson07_functools (@functools.cache) + l03_functions/lesson06_recursion
    def climb_stairs(self, steps: int) -> int:
        raise NotImplementedError("Ex 10: ways(n) = ways(n - 1) + ways(n - 2), cached")

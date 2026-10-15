"""
=====================================================================
 LEVEL 08 - EXERCISES (your turn!)
=====================================================================
 HOW    : Replace each `raise NotImplementedError(...)` line with your
          answer. The signatures are already typed: keep them, and make
          `uv run mypy` pass too, without Any or `# type: ignore`.
 CHECK  : uv run pytest -m exercise tests/l08_typing
          uv run mypy course/l08_typing/exercises
          or open tests/l08_typing/test_exercises.py and click the
          green arrow next to the class name.
 STUCK? : Re-read the lesson in the hint. Still stuck? Peek at
          ../solutions/solutions.py, but try first!
=====================================================================
"""

import functools  # noqa: F401 - you'll need it in Ex 9
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Literal, TypeGuard, assert_never, overload  # noqa: F401 - Ex 6

from course.l08_typing.tasks import Direction, Json, StackLike, SupportsLessThan, User


# Hint: lesson02_generics (class Stack[T]) + l05_errors/lesson03_raising
class Stack[T]:
    """Ex 2. Write __init__, push, pop, peek and __len__."""


class TypingExercises:
    # Hint: lesson02_generics (first[T])
    def first_or_default[T](self, items: Sequence[T], default: T) -> T:
        raise NotImplementedError("Ex 1: items[0], or default when empty")

    # Hint: lesson02_generics (Stack[T])
    def make_stack[T](self) -> StackLike[T]:
        raise NotImplementedError("Ex 2: write class Stack[T], then return Stack[T]()")

    # Hint: lesson04_protocols (smallest with a SupportsLessThan bound)
    def largest[T: SupportsLessThan](self, items: Iterable[T]) -> T | None:
        raise NotImplementedError("Ex 3: the largest item using only <, or None")

    # Hint: lesson02_generics (two type parameters) + l04_collections/lesson03_dicts
    def group_by[T, K](self, items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
        raise NotImplementedError("Ex 4: {key(item): [items...]} in order")

    # Hint: lesson05_typeddict_literal (TypedDict) + lesson01_type_basics (isinstance narrowing)
    def parse_user(self, data: Mapping[str, object]) -> User:
        raise NotImplementedError("Ex 5: check name, age, optional email; build a User")

    # Hint: lesson06_overloads (match + assert_never)
    def move(self, position: tuple[int, int], direction: Direction) -> tuple[int, int]:
        raise NotImplementedError("Ex 6: one step in the direction")

    # Hint: lesson06_overloads (parse). The overloads are done: write the last body.
    @overload
    def parse_number(self, text: str, *, as_float: Literal[True]) -> float: ...
    @overload
    def parse_number(self, text: str, *, as_float: Literal[False] = ...) -> int: ...
    def parse_number(self, text: str, *, as_float: bool = False) -> int | float:
        raise NotImplementedError("Ex 7: float(text) or int(text)")

    # Hint: lesson06_overloads (is_str_list)
    def is_str_list(self, values: list[object]) -> TypeGuard[list[str]]:
        raise NotImplementedError("Ex 8: True if every value is a str")

    # Hint: lesson07_callables (logged with ParamSpec) + l05_errors/lesson02_exceptions
    def with_fallback[**P, R](self, func: Callable[P, R], fallback: R) -> Callable[P, R]:
        raise NotImplementedError("Ex 9: a wrapper returning fallback on Exception")

    # Hint: lesson01_type_basics (the Json alias, isinstance narrowing)
    def get_path(self, data: Json, path: Sequence[str | int]) -> Json:
        raise NotImplementedError("Ex 10: walk dict keys and list indexes, else None")

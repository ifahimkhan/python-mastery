"""The list of Level 08 exercises.

Both ``exercises/exercises.py`` (your answers) and ``solutions/solutions.py``
(reference answers) implement this Protocol, so the SAME tests check both.

In this level the TYPES are half of the answer: `uv run mypy` must stay
clean for your exercises file, so no `Any`, no `# type: ignore`.
"""

from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, Literal, NotRequired, Protocol, TypedDict, TypeGuard, overload

type Json = dict[str, Json] | list[Json] | str | int | float | bool | None
type Direction = Literal["up", "down", "left", "right"]


class User(TypedDict):
    name: str
    age: int
    email: NotRequired[str]


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


class StackLike[T](Protocol):
    def push(self, item: T) -> None: ...

    def pop(self) -> T: ...

    def peek(self) -> T | None: ...

    def __len__(self) -> int: ...


class TypingTasks(Protocol):
    def first_or_default[T](self, items: Sequence[T], default: T) -> T:
        """Ex 1. The first item, or ``default`` if ``items`` is empty."""
        ...

    def make_stack[T](self) -> StackLike[T]:
        """Ex 2. A new, empty generic Stack. push() adds on top, pop() removes
        and returns the top item (IndexError("pop from empty stack") if
        empty), peek() returns the top item without removing it (None if
        empty), and len() is the number of items."""
        ...

    def largest[T: SupportsLessThan](self, items: Iterable[T]) -> T | None:
        """Ex 3. The largest item using only ``<``, or None if there are none.
        On a tie, keep the first one. Don't use max()."""
        ...

    def group_by[T, K](self, items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
        """Ex 4. Group items by key(item), keeping their order.

        group_by(["ant", "bee", "ape"], first_letter) == {"a": ["ant", "ape"], "b": ["bee"]}
        """
        ...

    def parse_user(self, data: Mapping[str, object]) -> User:
        """Ex 5. Turn untrusted data into a User.

        "name" must be a str and "age" an int (True/False do NOT count).
        "email" is optional, but if present it must be a str.
        Otherwise raise TypeError("<key> must be <type>"), e.g.
        TypeError("age must be int"). Ignore any other keys.
        """
        ...

    def move(self, position: tuple[int, int], direction: Direction) -> tuple[int, int]:
        """Ex 6. One step from (x, y). "up" adds 1 to y, "right" adds 1 to x.

        Use match and finish with assert_never, so mypy checks every case.
        """
        ...

    @overload
    def parse_number(self, text: str, *, as_float: Literal[True]) -> float: ...
    @overload
    def parse_number(self, text: str, *, as_float: Literal[False] = ...) -> int: ...
    def parse_number(self, text: str, *, as_float: bool = False) -> int | float:
        """Ex 7. float(text) when as_float is True, else int(text)."""
        ...

    def is_str_list(self, values: list[object]) -> TypeGuard[list[str]]:
        """Ex 8. True if every value is a str (True for an empty list too)."""
        ...

    def with_fallback[**P, R](self, func: Callable[P, R], fallback: R) -> Callable[P, R]:
        """Ex 9. A wrapper that calls func with the same arguments and returns
        its result, or ``fallback`` if it raises an Exception. Keep __name__.
        """
        ...

    def get_path(self, data: Json, path: Sequence[str | int]) -> Json:
        """Ex 10. Follow ``path`` into nested JSON data: a str step is a dict
        key, an int step a list index (0 or more). Return None as soon as a
        step doesn't fit (missing key, index out of range, wrong kind).

        get_path({"a": [10, {"b": 2}]}, ["a", 1, "b"]) == 2
        """
        ...

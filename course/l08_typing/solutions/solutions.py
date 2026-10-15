"""Reference answers for Level 08. Try the exercises first!

Each answer explains WHY it is written this way.
"""

import functools
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Literal, TypeGuard, assert_never, overload

from course.l08_typing.tasks import Direction, Json, StackLike, SupportsLessThan, User


# Ex 2. A generic class: Stack[int] only accepts and returns ints.
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T | None:
        return self._items[-1] if self._items else None

    def __len__(self) -> int:
        return len(self._items)


def _require[T](data: Mapping[str, object], key: str, kind: type[T]) -> T:
    """data[key] if it is exactly a `kind`, else TypeError. Shared by Ex 5."""
    value = data.get(key)
    # bool is a subclass of int, so isinstance(True, int) is True: refuse it
    # explicitly. isinstance(value, kind) also narrows value to T for mypy.
    if isinstance(value, bool) or not isinstance(value, kind):
        raise TypeError(f"{key} must be {kind.__name__}")
    return value


class TypingSolutions:
    # T links the two: a Sequence[str] with a str default gives a str back.
    def first_or_default[T](self, items: Sequence[T], default: T) -> T:
        return items[0] if items else default

    def make_stack[T](self) -> StackLike[T]:
        return Stack[T]()

    # The bound promises `<` exists, so the loop type-checks for any T.
    # Strict `<` keeps the FIRST of equal items.
    def largest[T: SupportsLessThan](self, items: Iterable[T]) -> T | None:
        best: T | None = None
        for item in items:
            if best is None or best < item:
                best = item
        return best

    # setdefault creates the list the first time a key is seen.
    def group_by[T, K](self, items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
        groups: dict[K, list[T]] = {}
        for item in items:
            groups.setdefault(key(item), []).append(item)
        return groups

    # Untrusted input: check every field, then build the TypedDict.
    # The optional key is only added when it is present.
    def parse_user(self, data: Mapping[str, object]) -> User:
        user: User = {
            "name": _require(data, "name", str),
            "age": _require(data, "age", int),
        }
        if "email" in data:
            user["email"] = _require(data, "email", str)
        return user

    # assert_never makes mypy complain if Direction ever gains a value
    # that this match does not handle.
    def move(self, position: tuple[int, int], direction: Direction) -> tuple[int, int]:
        x, y = position
        match direction:
            case "up":
                return x, y + 1
            case "down":
                return x, y - 1
            case "left":
                return x - 1, y
            case "right":
                return x + 1, y
            case _:
                assert_never(direction)

    # The overloads tell mypy the precise return type; only the last def runs.
    @overload
    def parse_number(self, text: str, *, as_float: Literal[True]) -> float: ...
    @overload
    def parse_number(self, text: str, *, as_float: Literal[False] = ...) -> int: ...
    def parse_number(self, text: str, *, as_float: bool = False) -> int | float:
        return float(text) if as_float else int(text)

    # all() of nothing is True, which is what we want for [].
    def is_str_list(self, values: list[object]) -> TypeGuard[list[str]]:
        return all(isinstance(value, str) for value in values)

    # ParamSpec: the wrapper has EXACTLY func's parameters, so mypy still
    # checks every call. Only Exception is caught (never Ctrl+C).
    def with_fallback[**P, R](self, func: Callable[P, R], fallback: R) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return func(*args, **kwargs)
            except Exception:
                return fallback

        return wrapper

    # Each isinstance check narrows `current`, so indexing is type-safe.
    # bool is checked first because it is also an int.
    def get_path(self, data: Json, path: Sequence[str | int]) -> Json:
        current = data
        for step in path:
            if isinstance(step, str) and isinstance(current, dict):
                if step not in current:
                    return None
                current = current[step]
            elif (
                isinstance(step, int)
                and not isinstance(step, bool)
                and isinstance(current, list)
                and 0 <= step < len(current)
            ):
                current = current[step]
            else:
                return None
        return current

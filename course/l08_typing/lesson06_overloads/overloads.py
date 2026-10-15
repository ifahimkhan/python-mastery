"""
=====================================================================
 LESSON 08.6 - Overloads, type guards and exhaustiveness
=====================================================================
 GOAL   : Give one function several precise signatures with @overload,
          teach mypy your own checks with TypeGuard, and make mypy prove
          that a match handles every case with assert_never.
 RUN    : uv run python -m course.l08_typing.lesson06_overloads.overloads
 OUTPUT :
          parse: 43 1.25
          double: 42 abab
          join_if_text: a, b | (not all text)
          icons: ['[+]', '[!]', '[x]']
          corners: {'circle': 0, 'square': 4}
 NEXT   : lesson07_callables/callables.py
=====================================================================
"""

from enum import Enum
from typing import Literal, TypeGuard, assert_never, overload


# -- 1. CONCEPT: @overload: the return type depends on the arguments -------
@overload
def parse(text: str, as_float: Literal[True]) -> float: ...
@overload
def parse(text: str, as_float: Literal[False] = ...) -> int: ...
def parse(text: str, as_float: bool = False) -> int | float:
    # Only this last version runs. The @overload lines exist for mypy.
    return float(text) if as_float else int(text)


@overload
def double(value: int) -> int: ...
@overload
def double(value: str) -> str: ...
def double(value: int | str) -> int | str:
    return value * 2


# -- 2. CONCEPT: TypeGuard: "if this returns True, the value is X" ----------
def is_str_list(values: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(value, str) for value in values)


def join_if_text(values: list[object]) -> str:
    if is_str_list(values):
        return ", ".join(values)  # mypy now knows: list[str]
    return "(not all text)"


# -- 3. CONCEPT: assert_never: proof that every case is handled -------------
class Shape(Enum):
    CIRCLE = "circle"
    SQUARE = "square"


type Status = Literal["ok", "warning", "error"]


def icon(status: Status) -> str:
    match status:
        case "ok":
            return "[+]"
        case "warning":
            return "[!]"
        case "error":
            return "[x]"
        case _:
            assert_never(status)  # mypy: only reachable if a case is missing


def corners(shape: Shape) -> int:
    if shape is Shape.CIRCLE:
        return 0
    if shape is Shape.SQUARE:
        return 4
    assert_never(shape)


def main() -> None:
    whole = parse("42")  # mypy: int
    fraction = parse("2.5", as_float=True)  # mypy: float
    print("parse:", whole + 1, fraction / 2)
    print("double:", double(21), double("ab"))

    print("join_if_text:", join_if_text(["a", "b"]), "|", join_if_text(["a", 1]))
    print("icons:", [icon(status) for status in ("ok", "warning", "error")])
    print("corners:", {shape.value: corners(shape) for shape in Shape})

    # -- 4. WHY ------------------------------------------------------------
    # Without overloads, parse() would return `int | float` and every
    # caller would need a check. Overloads keep one function but give
    # each call the precise type. assert_never turns "I forgot a case"
    # from a runtime surprise into a mypy error.

    # -- 5. PITFALL ------------------------------------------------------
    # - The implementation (last def) must accept every overload, and the
    #   overloads themselves are never run.
    # - A TypeGuard function is trusted blindly: if it says True wrongly,
    #   mypy believes it anyway.
    # - Add "TRIANGLE" to Shape and run mypy:
    #   Argument 1 to "assert_never" has incompatible type
    #   "Literal[Shape.TRIANGLE]"; expected "Never"

    # -- 6. TRY IT -----------------------------------------------------
    # a) Add "info" to Status. Run mypy before fixing icon().
    # b) Write is_int_list(values: list[object]) -> TypeGuard[list[int]].
    # c) Add an overload double(value: list[int]) -> list[int].


if __name__ == "__main__":
    main()

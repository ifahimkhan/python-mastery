"""
=====================================================================
 LESSON 08.1 - Type checking basics
=====================================================================
 GOAL   : Know what mypy checks and what Python ignores, narrow a union
          with is None / isinstance, choose object over Any, and name
          complex types with `type` aliases.
 RUN    : uv run python -m course.l08_typing.lesson01_type_basics.type_basics
 OUTPUT :
          distance: 5.0
          shout: ADA NOBODY
          describe: int 42 | str HI | list of 2
          safe_length: 3 0
          Any let this through: object of type 'int' has no len()
          runtime doesn't care: not an int
          distance hints: {'a': Point, 'b': Point, 'return': <class 'float'>}
          Point alias is: tuple[float, float]
          cast: Ada
 NOTE   : Check this file yourself: uv run mypy course/l08_typing
 NEXT   : lesson02_generics/generics.py
=====================================================================
"""

from typing import Any, cast

# -- 1. CONCEPT: type aliases give a long type a short name ---------------
type Point = tuple[float, float]
type Matrix = list[list[float]]
type Json = dict[str, Json] | list[Json] | str | int | float | bool | None  # it can refer to itself


def distance(a: Point, b: Point) -> float:
    return float(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5)


# -- 2. CONCEPT: narrowing: mypy follows your checks ----------------------
def shout(name: str | None) -> str:
    # Here name is `str | None`: name.upper() would be an error.
    if name is None:
        return "NOBODY"
    return name.upper()  # here mypy KNOWS it is a str


def describe(value: int | str | list[int]) -> str:
    if isinstance(value, int):
        return f"int {value + 1}"  # int here
    if isinstance(value, str):
        return f"str {value.upper()}"  # str here
    return f"list of {len(value)}"  # only list[int] is left


# -- 3. CONCEPT: object vs Any ---------------------------------------------
def safe_length(value: object) -> int:
    # `object` accepts anything, but you must CHECK before using it.
    if isinstance(value, str | list | dict):
        return len(value)
    return 0


def unsafe_length(value: Any) -> int:
    # `Any` switches checking OFF: mypy allows anything, even mistakes.
    return len(value)  # crashes at runtime for 42; mypy stays silent


def main() -> None:
    print("distance:", distance((0, 0), (3, 4)))
    print("shout:", shout("ada"), shout(None))
    print("describe:", describe(41), "|", describe("hi"), "|", describe([1, 2]))
    print("safe_length:", safe_length("abc"), safe_length(42))

    try:
        unsafe_length(42)
    except TypeError as error:
        print("Any let this through:", error)

    # Hints are NOT checked when the program runs. Python ignores them:
    wrong: int = "not an int"  # type: ignore[assignment]  # mypy would refuse this
    print("runtime doesn't care:", wrong)

    # Annotations are still stored, for tools to read:
    print("distance hints:", distance.__annotations__)
    print("Point alias is:", Point.__value__)

    # cast() tells mypy "trust me". It does NOTHING at runtime.
    data: object = {"name": "Ada"}
    record = cast(dict[str, str], data)
    print("cast:", record["name"])

    # -- 4. WHY ------------------------------------------------------------
    # Type hints are checked by a separate tool (mypy, or PyCharm as you
    # type) BEFORE the code runs. They catch None mistakes, typos and
    # wrong arguments in code paths your tests never reached.

    # -- 5. PITFALL: forgetting the None case -----------------------------
    # def length(name: str | None) -> int:
    #     return len(name)
    # mypy: Argument 1 to "len" has incompatible type "str | None"; expected "Sized"
    #
    # def f(x: object) -> None:
    #     x.upper()
    # mypy: "object" has no attribute "upper"
    #
    # Prefer `object` + isinstance over `Any`. Use cast() and
    # `# type: ignore[code]` rarely, and always with the error code.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Remove the `if name is None` check in shout() and run uv run mypy.
    # b) Add `reveal_type(value)` inside describe() after each isinstance
    #    and run mypy: it prints the narrowed type. (Remove it afterwards.)
    # c) Write a function that sums every int inside a Json value.


if __name__ == "__main__":
    main()

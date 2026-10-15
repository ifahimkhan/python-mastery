"""
=====================================================================
 LESSON 03.7 - Type hints and functions as values
=====================================================================
 GOAL   : Annotate parameters and return values, use X | None for
          "maybe nothing", check code with mypy, and pass functions
          around like any other value.
 RUN    : uv run python -m course.l03_functions.lesson07_type_hints.type_hints
 OUTPUT :
          area: 12.0
          find_index('banana', 'n') = 2
          find_index('banana', 'z') = None
          'z' not found
          hints are not enforced at run time: abcabc
          shout is a <class 'function'>
          apply(shout, 'hi') = HI!
          apply(whisper, 'HI') = hi...
          apply_n_times(double, 1, 10) = 1024
 NEXT   : practice/text_tools/text_tools.py
=====================================================================
"""

from collections.abc import Callable

DOUBLE_FACTOR = 2


# -- 1. CONCEPT: annotations ------------------------------------------------
# parameter: type   and   -> return type
# Common types: int, float, str, bool, None, and later list[int] (level 04).
def rectangle_area(width: float, height: float) -> float:
    return width * height


# -- 2. CONCEPT: X | None means "an X, or nothing" -------------------------
# The return type tells callers they MUST handle the None case.
def find_index(text: str, char: str) -> int | None:
    for index, current in enumerate(text):
        if current == char:
            return index
    return None


# -- 3. PITFALL: hints are not checked while the program runs ---------------
def repeat(text: str, times: int) -> str:
    return text * times


# -- 4. CONCEPT: functions are values --------------------------------------
# A function can be stored in a variable and passed to another function.
# Callable[[str], str] means "a function taking one str and returning a str".
def shout(text: str) -> str:
    return text.upper() + "!"


def whisper(text: str) -> str:
    return text.lower() + "..."


def apply(func: Callable[[str], str], text: str) -> str:
    return func(text)  # call whatever function we were given


def double(n: int) -> int:
    return n * DOUBLE_FACTOR


def apply_n_times(func: Callable[[int], int], value: int, times: int) -> int:
    for _ in range(times):
        value = func(value)
    return value


def main() -> None:
    print("area:", rectangle_area(3, 4.0))  # an int is fine where a float is expected

    print("find_index('banana', 'n') =", find_index("banana", "n"))
    print("find_index('banana', 'z') =", find_index("banana", "z"))
    position = find_index("banana", "z")
    if position is None:  # `is None`, not `== None` (level 05)
        print("'z' not found")
    else:
        print("'z' found at", position + 1)  # mypy knows position is an int here

    # repeat("abc", "2") would crash: TypeError: can't multiply sequence by
    # non-int of type 'str'. But repeat(2, "abc") RUNS (2 * "abc" works!),
    # even though both hints are wrong. Only a type checker notices:
    print("hints are not enforced at run time:", repeat(2, "abc"))  # type: ignore[arg-type]

    print("shout is a", type(shout))
    # No brackets after shout: we pass the function itself, we don't call it.
    print("apply(shout, 'hi') =", apply(shout, "hi"))
    print("apply(whisper, 'HI') =", apply(whisper, "HI"))
    print("apply_n_times(double, 1, 10) =", apply_n_times(double, 1, 10))

    # -- 5. WHY: hints are documentation that a tool checks -------------
    # This course runs `uv run mypy` (strict mode) in CI. mypy reads the
    # hints and finds mistakes before the code runs, for example:
    #   rectangle_area("3", 4)
    #   # error: Argument 1 to "rectangle_area" has incompatible type "str";
    #   #        expected "float"  [arg-type]
    #   find_index("abc", "z") + 1
    #   # error: Unsupported operand types for + ("None" and "int")  [operator]
    # PyCharm underlines the same mistakes as you type.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Write first_word(text: str) -> str | None that returns None for "".
    # b) Remove the `# type: ignore` comment above and run `uv run mypy`.
    # c) Write exclaim(text) and pass it to apply(). Then try apply(len, "hi")
    #    and run mypy. Why does it complain?


if __name__ == "__main__":
    main()

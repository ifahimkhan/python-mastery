"""
=====================================================================
 LESSON 03.1 - Function basics
=====================================================================
 GOAL   : Define functions with def, pass arguments, return results,
          and know the difference between printing and returning.
 RUN    : uv run python -m course.l03_functions.lesson01_basics.function_basics
 OUTPUT :
          Hello, Ada!
          Hello, Linus!
          square(7) = 49
          square(square(3)) = 81
          returns: 12
          prints: 12
          print_double gave back: None
          classify(-4) = negative
          classify(0) = zero
          75 minutes = 1 h 15 min
          help: Return the area of a circle with the given radius.
          area of radius 2: 12.57
 NEXT   : lesson02_defaults/defaults_and_keywords.py
=====================================================================
"""

import math

MINUTES_PER_HOUR = 60


# -- 1. CONCEPT: def, parameters and calls -----------------------------
# `name` is a PARAMETER: a placeholder. The value you pass when calling
# ("Ada") is the ARGUMENT. The body only runs when the function is called.
def greet(name: str) -> None:
    print(f"Hello, {name}!")


# -- 2. CONCEPT: return hands a value back ------------------------------
# `-> int` and `: int` are type hints (lesson 03.7). Python doesn't check
# them while running, but mypy and PyCharm do.
def square(n: int) -> int:
    return n * n


# -- 3. PITFALL: print is not return ------------------------------------
def double(n: int) -> int:
    return n * 2  # the caller gets the value and can keep using it


def print_double(n: int) -> None:
    print("prints:", n * 2)  # shows it, but the caller gets nothing back


# -- 4. CONCEPT: return ends the function at once -----------------------
# An "early return" handles a case and leaves; no else needed afterwards.
def classify(n: int) -> str:
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"


# -- 5. CONCEPT: returning several values -------------------------------
# `return a, b` really returns ONE tuple (level 04), which the caller can
# unpack into two names, just like `x, y = 1, 2` (lesson 01.2).
def split_minutes(total: int) -> tuple[int, int]:
    return total // MINUTES_PER_HOUR, total % MINUTES_PER_HOUR


# -- 6. CONCEPT: docstrings ---------------------------------------------
# The first string in a function is its documentation. PyCharm shows it
# when you hover over a call, and help() prints it.
def circle_area(radius: float) -> float:
    """Return the area of a circle with the given radius."""
    return math.pi * radius**2


def main() -> None:
    greet("Ada")
    greet("Linus")

    print("square(7) =", square(7))
    print("square(square(3)) =", square(square(3)))  # results can feed other calls

    print("returns:", double(6))
    # mypy flags the next line on purpose: "does not return a value". That
    # warning catches exactly this mistake before the program even runs.
    result = print_double(6)  # type: ignore[func-returns-value]
    print("print_double gave back:", result)  # a function without return gives None

    print("classify(-4) =", classify(-4))
    print("classify(0) =", classify(0))

    hours, minutes = split_minutes(75)
    print(f"75 minutes = {hours} h {minutes} min")

    print("help:", circle_area.__doc__)
    print(f"area of radius 2: {circle_area(2):.2f}")

    # -- 7. WHY: functions --------------------------------------------
    # A name for a piece of logic: write it once, test it once, reuse it,
    # and read `classify(n)` instead of six lines of ifs.
    # Rule of thumb: a function does ONE thing and fits on one screen.

    # -- 8. PITFALL: calling it wrong ---------------------------------
    #   square()        # TypeError: square() missing 1 required positional argument: 'n'
    #   square(1, 2)    # TypeError: square() takes 1 positional argument but 2 were given
    #   square          # no brackets: just the function object, nothing runs
    # A function must be defined BEFORE the line that calls it runs.

    # -- 9. TRY IT -----------------------------------------------------
    # a) Write cube(n) and print cube(3).
    # b) Write is_adult(age) that returns True from 18 on. Use it in an if.
    # c) Write split_seconds(total) that returns minutes and seconds.


if __name__ == "__main__":
    main()

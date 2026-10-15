"""
=====================================================================
 LESSON 05.3 - Raising exceptions
=====================================================================
 GOAL   : Stop a function with raise when its input makes no sense,
          re-raise errors you can't handle, and chain errors with
          `raise ... from ...`.
 RUN    : uv run python -m course.l05_errors.lesson03_raising.raising
 OUTPUT :
          set_age(30) = 30
          set_age(-5) -> ValueError: age must be 0..150, got -5
          set_age('x') -> TypeError: age must be an int, got str
          load_setting('port') = 8080
          load_setting('host') -> KeyError: "no setting named 'host'"
          caused by: KeyError 'host'
          logged, re-raising: ZeroDivisionError
          assert stops on impossible states: total must not be negative
 NEXT   : lesson04_custom_exceptions/custom_exceptions.py
=====================================================================
"""

MAX_AGE = 150
SETTINGS = {"port": 8080}


# -- 1. CONCEPT: raise ------------------------------------------------------
# A "guard clause" at the top rejects bad input with a clear message.
# Pick the built-in type that fits: ValueError (right type, bad value),
# TypeError (wrong type), KeyError/IndexError (missing key or index).
def set_age(age: object) -> int:
    if not isinstance(age, int):
        raise TypeError(f"age must be an int, got {type(age).__name__}")
    if not 0 <= age <= MAX_AGE:
        raise ValueError(f"age must be 0..{MAX_AGE}, got {age}")
    return age


# -- 2. CONCEPT: raise ... from ... -------------------------------------------
# Translate a low-level error into one that makes sense to the caller,
# while keeping the original as __cause__ (shown in the traceback too).
def load_setting(name: str) -> int:
    try:
        return SETTINGS[name]
    except KeyError as error:
        raise KeyError(f"no setting named {name!r}") from error


# -- 3. CONCEPT: bare raise re-raises -----------------------------------------
# Do something (log, clean up), then let the error continue upwards.
def risky() -> float:
    try:
        return 1 / 0
    except ZeroDivisionError:
        print("logged, re-raising:", end=" ")
        raise  # the SAME exception, with its original traceback


def checked_total(prices: list[int]) -> int:
    total = sum(prices)
    # -- 4. CONCEPT: assert for "this can't happen" ----------------------
    # assert documents an internal assumption. NEVER use it to validate
    # user input: `python -O` switches asserts off.
    assert total >= 0, "total must not be negative"
    return total


def main() -> None:
    print("set_age(30) =", set_age(30))
    for bad in (-5, "x"):
        try:
            set_age(bad)
        except (ValueError, TypeError) as error:
            print(f"set_age({bad!r}) -> {type(error).__name__}: {error}")

    print("load_setting('port') =", load_setting("port"))
    try:
        load_setting("host")
    except KeyError as error:
        print(f"load_setting('host') -> KeyError: {error}")
        cause = error.__cause__
        print("caused by:", type(cause).__name__, cause)

    try:
        risky()
    except ZeroDivisionError as error:
        print(type(error).__name__)

    try:
        checked_total([5, -10])
    except AssertionError as error:
        print("assert stops on impossible states:", error)

    # -- 5. WHY: fail fast, fail loud ---------------------------------
    # Returning None or -1 for bad input pushes the problem to the
    # caller, who may not check. An exception can't be ignored by accident,
    # and its message says exactly what was wrong.

    # -- 6. PITFALL: raising the wrong thing ----------------------------
    #   raise "bad age"          # TypeError: exceptions must derive from BaseException
    #   raise Exception("...")   # too vague: callers can't catch it precisely
    #   except ValueError: raise ValueError("bad")   # without `from`, the
    #   # traceback says "During handling ... another exception occurred",
    #   # which looks like a bug in your error handling.

    # -- 7. TRY IT -----------------------------------------------------
    # a) Write sqrt(x) that raises ValueError for negative numbers.
    # b) Remove `from error` in load_setting and compare the tracebacks
    #    when you call load_setting("host") without try.
    # c) Run this file with `uv run python -O -m ...`. What happens to the assert?


if __name__ == "__main__":
    main()

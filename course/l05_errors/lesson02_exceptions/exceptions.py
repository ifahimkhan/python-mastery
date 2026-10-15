"""
=====================================================================
 LESSON 05.2 - Catching exceptions: try / except / else / finally
=====================================================================
 GOAL   : Catch the errors you expect, let the others through, and
          know exactly when else and finally run.
 RUN    : uv run python -m course.l05_errors.lesson02_exceptions.exceptions
 OUTPUT :
          to_int('42') = 42
          to_int('abc') = None
          10 / 2 = 5.0
          10 / 0 -> cannot divide by zero
          10 / 'x' -> TypeError: unsupported operand type(s) for /: 'int' and 'str'
          parsed 7, no error
          cleanup runs
          cleanup runs
          caught as LookupError: KeyError 'z'
          caught as LookupError: IndexError list index out of range
          ValueError is an Exception: True
          KeyboardInterrupt is an Exception: False
 NEXT   : lesson03_raising/raising.py
=====================================================================
"""


def to_int(text: str) -> int | None:
    # -- 1. CONCEPT: try / except ------------------------------------------
    # Run the risky code in `try`. If a ValueError happens, Python jumps
    # to the matching `except` block instead of crashing.
    try:
        return int(text)
    except ValueError:
        return None


def divide(a: object, b: object) -> str:
    # -- 2. CONCEPT: several except blocks, and `as` -------------------------
    # The first matching block runs. `as error` gives you the exception object.
    try:
        return f"{a / b}"  # type: ignore[operator]
    except ZeroDivisionError:
        return "cannot divide by zero"
    except TypeError as error:
        return f"{type(error).__name__}: {error}"


def parse_and_report(text: str) -> None:
    # -- 3. CONCEPT: else and finally ------------------------------------
    # else    runs only if the try block raised NOTHING.
    # finally runs ALWAYS: after success, after an error, even after return.
    try:
        value = int(text)
    except ValueError:
        pass  # (in real code: report it; see the bare except pitfall below)
    else:
        print(f"parsed {value}, no error")
    finally:
        print("cleanup runs")  # close files, release locks... (level 09)


def first_of(container: dict[str, int] | list[int], key: str | int) -> str:
    # -- 4. CONCEPT: catching a parent class catches its children ---------
    # KeyError and IndexError both inherit from LookupError.
    try:
        container[key]  # type: ignore[index]
    except LookupError as error:
        return f"caught as LookupError: {type(error).__name__} {error}"
    return "found"


def main() -> None:
    print("to_int('42') =", to_int("42"))
    print("to_int('abc') =", to_int("abc"))
    print("10 / 2 =", divide(10, 2))
    print("10 / 0 ->", divide(10, 0))
    print("10 / 'x' ->", divide(10, "x"))
    parse_and_report("7")
    parse_and_report("seven")
    print(first_of({"a": 1}, "z"))
    print(first_of([1, 2], 5))

    # The exception family tree (a small part of it):
    #   BaseException
    #    +-- KeyboardInterrupt, SystemExit   (Ctrl+C, exit(): NOT errors)
    #    +-- Exception                       (everything you normally catch)
    #         +-- ValueError, TypeError, ZeroDivisionError (ArithmeticError)
    #         +-- LookupError -> KeyError, IndexError
    print("ValueError is an Exception:", issubclass(ValueError, Exception))
    print("KeyboardInterrupt is an Exception:", issubclass(KeyboardInterrupt, Exception))

    # -- 5. WHY: catch narrowly ---------------------------------------
    # Catch the specific error you can handle, in the smallest try block
    # possible. Everything else should crash loudly: a crash with a
    # traceback is far easier to fix than wrong results.

    # -- 6. PITFALL: catching everything ---------------------------------
    #   try:
    #       total = price * quantity
    #   except:              # bare except: also swallows Ctrl+C and typos!
    #       total = 0        # bugs now hide as "0"
    # A NameError from a typo would be silently turned into 0. If you
    # really must catch broadly, use `except Exception as error:` and log it.
    # And read tracebacks from the BOTTOM: the last line is the error, the
    # line above it is where it happened.

    # -- 7. TRY IT -----------------------------------------------------
    # a) Call to_int(" 12 "). Does int() accept the spaces?
    # b) Add `return "early"` inside the try of parse_and_report. Does finally still run?
    # c) Catch both ValueError and TypeError in ONE block: except (ValueError, TypeError):


if __name__ == "__main__":
    main()

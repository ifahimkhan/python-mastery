"""
=====================================================================
 LESSON 07.3 - Decorators
=====================================================================
 GOAL   : Write decorators that wrap a function with extra behaviour,
          keep its name with functools.wraps, take arguments, and
          stack several on one function.
 RUN    : uv run python -m course.l07_functional.lesson03_decorators.decorators
 OUTPUT :
          HELLO, ADA!
          name and doc kept: greet / Say hello.
          calling add(2, 3):
            -> add(2, 3)
            <- add returned 5
          cheer('blue') with @repeat(times=2):
            go blue!
            go blue!
          stacked: READY, ADA?!
          without wraps, the name is: wrapper
 NOTE   : Decorators here are typed with ParamSpec, so mypy knows the
          wrapped function keeps its parameters. Level 08 explains it.
 NEXT   : lesson04_iterators/iterators.py
=====================================================================
"""

import functools
from collections.abc import Callable


# -- 1. CONCEPT: a decorator takes a function and returns a new one ------
# @shout above a def means:   greet = shout(greet)
def shout[**P](func: Callable[P, str]) -> Callable[P, str]:
    @functools.wraps(func)  # copy __name__ and __doc__ onto the wrapper
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> str:
        return func(*args, **kwargs).upper() + "!"

    return wrapper


@shout
def greet(name: str) -> str:
    """Say hello."""
    return f"hello, {name}"


# -- 2. CONCEPT: wrappers can run code before and after the call ---------
def log_calls[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"  -> {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"  <- {func.__name__} returned {result!r}")
        return result

    return wrapper


@log_calls
def add(a: int, b: int) -> int:
    return a + b


# -- 3. CONCEPT: a decorator WITH arguments is a function that RETURNS a decorator
def repeat[**P](times: int) -> Callable[[Callable[P, None]], Callable[P, None]]:
    def decorator(func: Callable[P, None]) -> Callable[P, None]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> None:
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(times=2)
def cheer(team: str) -> None:
    print(f"  go {team}!")


# -- 4. CONCEPT: stacking: the decorator nearest the def is applied first --
def exclaim[**P](func: Callable[P, str]) -> Callable[P, str]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> str:
        return func(*args, **kwargs) + "?"

    return wrapper


@shout  # 2nd: shout(exclaim(ask))
@exclaim  # 1st
def ask(name: str) -> str:
    return f"ready, {name}"


def no_wraps[**P](func: Callable[P, str]) -> Callable[P, str]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> str:
        return func(*args, **kwargs)

    return wrapper


@no_wraps
def plain() -> str:
    return "x"


def main() -> None:
    print(greet("ada"))
    print("name and doc kept:", greet.__name__, "/", greet.__doc__)

    print("calling add(2, 3):")
    add(2, 3)

    print("cheer('blue') with @repeat(times=2):")
    cheer("blue")

    print("stacked:", ask("ada"))
    print("without wraps, the name is:", plain.__name__)

    # -- 5. WHY ------------------------------------------------------------
    # Logging, timing, caching, retrying, access checks: behaviour that has
    # nothing to do with WHAT a function computes. A decorator adds it in
    # one line, without touching the function body.

    # -- 6. PITFALL: calling instead of passing -----------------------------
    # @repeat          (forgot the arguments)
    # def cheer(team): ...
    # Now repeat(cheer) runs with times=cheer, and cheer("blue") fails with
    # TypeError: 'function' object cannot be interpreted as an integer
    # (and mypy reports it before you run anything).

    # -- 7. TRY IT -----------------------------------------------------
    # a) Write @count_calls that stores wrapper.calls and adds 1 per call.
    # b) Swap the order of @shout and @exclaim. Predict, then run.
    # c) Remove @functools.wraps from shout. What does greet.__name__ print?


if __name__ == "__main__":
    main()

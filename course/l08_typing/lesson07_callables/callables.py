"""
=====================================================================
 LESSON 08.7 - Typing callables and decorators
=====================================================================
 GOAL   : Type functions passed around as values: Callable, ParamSpec
          for decorators that keep the wrapped signature, and Concatenate
          for decorators that add an argument.
 RUN    : uv run python -m course.l08_typing.lesson07_callables.callables
 OUTPUT :
          apply_to_pair(max): 9
          apply_to_pair(str concat): abcd
          calling area:
            area -> '6 cm2'
          perimeter: 10
          count_users(True): 1
          count_users(False): 2
          queries run: 2
 NEXT   : ../README.md, then the exercises
=====================================================================
"""

import functools
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Concatenate


# -- 1. CONCEPT: Callable[[args], result] -----------------------------------
def apply_to_pair[T, R](func: Callable[[T, T], R], a: T, b: T) -> R:
    return func(a, b)


# -- 2. CONCEPT: the problem ParamSpec solves --------------------------------
# A decorator typed with Callable[..., R] makes mypy FORGET the arguments:
def loose[R](func: Callable[..., R]) -> Callable[..., R]:
    return func


# **P captures ALL parameters (names, types, kinds) of the wrapped function.
# P.args / P.kwargs then mean "exactly those arguments".
def logged[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        result = func(*args, **kwargs)
        print(f"  {func.__name__} -> {result!r}")
        return result

    return wrapper


@logged
def area(width: float, height: float, *, unit: str = "m") -> str:
    return f"{width * height} {unit}2"


@loose
def perimeter(width: float, height: float) -> float:
    return 2 * (width + height)


# -- 3. CONCEPT: Concatenate: the decorator supplies the first argument ----
@dataclass
class Database:
    queries: list[str] = field(default_factory=list)

    def run(self, sql: str) -> int:
        self.queries.append(sql)
        return len(self.queries)


DB = Database()


def with_db[**P, R](func: Callable[Concatenate[Database, P], R]) -> Callable[P, R]:
    """Callers no longer pass the database: the decorator does."""

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(DB, *args, **kwargs)

    return wrapper


@with_db
def count_users(db: Database, active_only: bool) -> int:
    return db.run(f"SELECT COUNT(*) FROM users WHERE active = {active_only}")


def main() -> None:
    print("apply_to_pair(max):", apply_to_pair(max, 3, 9))
    print("apply_to_pair(str concat):", apply_to_pair(str.__add__, "ab", "cd"))

    print("calling area:")
    area(2, 3, unit="cm")
    print("perimeter:", perimeter(2, 3))

    print("count_users(True):", count_users(True))  # no db argument!
    print("count_users(False):", count_users(False))
    print("queries run:", len(DB.queries))

    # -- 4. WHY ------------------------------------------------------------
    # With ParamSpec, area("2", 3) is still an error after decorating, and
    # PyCharm still shows the real parameter names. With the loose version,
    # perimeter("oops") passes mypy and crashes at runtime.

    # -- 5. PITFALL: Callable[..., R] silently turns checking off ------------
    # perimeter("a", "b", "c")    -> mypy says nothing (loose decorator)
    # area("a", 3)                -> mypy: Argument 1 to "area" has
    #                                incompatible type "str"; expected "float"
    # count_users(DB, True)       -> mypy: Too many arguments for "count_users"

    # -- 6. TRY IT -----------------------------------------------------
    # a) Type loose() with ParamSpec, then call perimeter("oops") and run mypy.
    # b) Write @with_prefix(prefix) that adds `prefix` to a str result.
    # c) Remove @functools.wraps from logged. What does area.__name__ become?


if __name__ == "__main__":
    main()

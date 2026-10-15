"""
=====================================================================
 LESSON 08.4 - Protocols in depth
=====================================================================
 GOAL   : Write generic Protocols, check Protocols at runtime with
          @runtime_checkable, and describe callbacks (including keyword
          arguments) with a __call__ Protocol.
 RUN    : uv run python -m course.l08_typing.lesson04_protocols.protocols
 OUTPUT :
          saved and loaded: User(name='Ada') None
          smallest: 3 fig -1.0
          Connection is Closeable:
            connection closed
          str is not Closeable
          int is not Closeable
          report: ['1.2 EUR', '5.0 EUR']
 NEXT   : lesson05_typeddict_literal/typeddict_literal.py
=====================================================================
"""

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any, Protocol, runtime_checkable


# -- 1. CONCEPT: a generic Protocol -----------------------------------------
class Repository[T](Protocol):
    def get(self, key: str) -> T | None: ...

    def save(self, key: str, item: T) -> None: ...


@dataclass(frozen=True)
class User:
    name: str


class InMemoryUsers:  # never mentions Repository, but fits Repository[User]
    def __init__(self) -> None:
        self._data: dict[str, User] = {}

    def get(self, key: str) -> User | None:
        return self._data.get(key)

    def save(self, key: str, item: User) -> None:
        self._data[key] = item


def register(repo: Repository[User], key: str, name: str) -> User:
    user = User(name)
    repo.save(key, user)
    return user


# -- 2. CONCEPT: a bound Protocol for "can be compared with <" --------------
# `other: Any` because int.__lt__ takes an int, str.__lt__ a str, and so on.
# The standard library's own typing (typeshed) writes it exactly like this.
class SupportsLessThan(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


def smallest[T: SupportsLessThan](items: Iterable[T]) -> T:
    iterator = iter(items)
    best = next(iterator)
    for item in iterator:
        if item < best:
            best = item
    return best


# -- 3. CONCEPT: runtime checks with @runtime_checkable ---------------------
@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None: ...


class Connection:
    def close(self) -> None:
        print("  connection closed")


# -- 4. CONCEPT: callback Protocols describe what Callable[...] can't -------
class Formatter(Protocol):
    def __call__(self, value: float, *, decimals: int = 2) -> str: ...


def money(value: float, *, decimals: int = 2) -> str:
    return f"{value:.{decimals}f} EUR"


def report(values: Iterable[float], fmt: Formatter) -> list[str]:
    return [fmt(value, decimals=1) for value in values]


def main() -> None:
    users = InMemoryUsers()
    register(users, "u1", "Ada")
    print("saved and loaded:", users.get("u1"), users.get("nope"))

    print("smallest:", smallest([5, 3, 8]), smallest(["pear", "fig"]), smallest([2.5, -1.0]))

    things: list[object] = [Connection(), "a string", 42]
    for thing in things:
        if isinstance(thing, Closeable):
            print(f"{type(thing).__name__} is Closeable:")
            thing.close()
        else:
            print(f"{type(thing).__name__} is not Closeable")

    print("report:", report([1.234, 5], money))

    # -- 5. WHY ------------------------------------------------------------
    # A Protocol lets code depend on WHAT it needs, not on a concrete class.
    # Tests can pass a tiny fake; production passes the real database class.
    # Neither has to import or inherit from the Protocol.

    # -- 6. PITFALL: runtime_checkable only checks NAMES ----------------------
    # isinstance(x, Closeable) is True if x has ANY attribute called close,
    # even `close = 5`. Signatures and types are not checked at runtime.
    # It is also slow-ish: use it at boundaries, not in hot loops.
    #
    # Callable[[float], str] can't say "with a keyword-only `decimals`":
    # that is what a __call__ Protocol is for.

    # -- 7. TRY IT -----------------------------------------------------
    # a) Write a FakeUsers class that records every save() in a list, and
    #    pass it to register().
    # b) Use smallest() on a list of Dogs (no __lt__). Read mypy's error.
    # c) Write `def plain(value: float) -> str` and pass it to report().
    #    Why does mypy refuse it?


if __name__ == "__main__":
    main()

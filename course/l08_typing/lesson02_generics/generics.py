"""
=====================================================================
 LESSON 08.2 - Generics
=====================================================================
 GOAL   : Write functions and classes that work for ANY type while
          keeping the exact type, and limit that type with a bound or
          a list of allowed types.
 RUN    : uv run python -m course.l08_typing.lesson02_generics.generics
 OUTPUT :
          first: 10 x
          pair_up: {'a': 1, 'b': 2}
          apply_all: [3, 5]
          box: Box(content='42')
          stack pop: b left: 1
          biggest: 7 2.5
          by_name: ['pug', 'boxer']
          type params: (T,) (T,)
 NOTE   : This is the Python 3.12 syntax (`def f[T]`). Older code writes
          T = TypeVar("T") at the top instead; it means the same thing.
 NEXT   : lesson03_variance/variance.py
=====================================================================
"""

from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass, field
from typing import Protocol


# -- 1. CONCEPT: a type parameter links input and output types ------------
def first[T](items: Sequence[T]) -> T:
    return items[0]
    # first([1, 2]) is an int; first(["a"]) is a str. With `-> object`
    # callers would lose that information.


def pair_up[K, V](keys: Iterable[K], values: Iterable[V]) -> dict[K, V]:
    return dict(zip(keys, values, strict=True))


def apply_all[T, R](func: Callable[[T], R], items: Iterable[T]) -> list[R]:
    return [func(item) for item in items]


# -- 2. CONCEPT: generic classes --------------------------------------------
@dataclass
class Box[T]:
    content: T

    def map[R](self, func: Callable[[T], R]) -> "Box[R]":
        return Box(func(self.content))


@dataclass
class Stack[T]:
    _items: list[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)


# -- 3. CONCEPT: limit T with constraints or a bound ------------------------
# Constraints: T must be EXACTLY one of these types.
def biggest[T: (int, float)](a: T, b: T) -> T:
    return a if a > b else b


# A bound: T may be any type that HAS what the Protocol describes.
class HasName(Protocol):
    @property
    def name(self) -> str: ...


@dataclass(frozen=True)
class Dog:
    name: str
    breed: str


def by_name[T: HasName](things: Iterable[T]) -> list[T]:
    return sorted(things, key=lambda thing: thing.name)  # T keeps its full type


def main() -> None:
    print("first:", first([10, 20]), first("xyz"))
    print("pair_up:", pair_up(["a", "b"], [1, 2]))
    print("apply_all:", apply_all(len, ["one", "three"]))

    box = Box(21).map(lambda n: n * 2).map(str)  # Box[int] -> Box[int] -> Box[str]
    print("box:", box)

    stack: Stack[str] = Stack()
    stack.push("a")
    stack.push("b")
    print("stack pop:", stack.pop(), "left:", len(stack))

    print("biggest:", biggest(3, 7), biggest(2.5, 1.0))
    dogs = by_name([Dog("Rex", "boxer"), Dog("Ace", "pug")])
    print("by_name:", [dog.breed for dog in dogs])  # still Dogs: .breed works
    print("type params:", first.__type_params__, Box.__type_params__)

    # -- 4. WHY ------------------------------------------------------------
    # Without generics you choose between precise-but-duplicated code
    # (first_int, first_str, ...) and one loose `object` version that
    # makes every caller cast. A type parameter gives both.

    # -- 5. PITFALL: mixing up types ---------------------------------------
    # n: int = first(["a"])
    # mypy: Incompatible types in assignment (expression has type "str",
    #       variable has type "int")
    # biggest("a", "b")
    # mypy: Value of type variable "T" of "biggest" cannot be "str"
    # stack.push(3)   (stack is Stack[str])  -> mypy: incompatible type "int"

    # -- 6. TRY IT -----------------------------------------------------
    # a) Write last[T](items: Sequence[T]) -> T | None (None if empty).
    # b) Add Stack.peek() -> T | None.
    # c) Make by_name work for any class with a `name` attribute. Try it
    #    with a dataclass Cat(name: str). Does Cat import HasName?


if __name__ == "__main__":
    main()

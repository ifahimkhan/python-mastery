"""
=====================================================================
 LESSON 08.3 - Variance
=====================================================================
 GOAL   : Understand why a list[int] is NOT a list[float] for mypy, why
          a Sequence[int] IS a Sequence[float], and which way callables
          go, so you can choose parameter types that accept the most.
 RUN    : uv run python -m course.l08_typing.lesson03_variance.variance
 OUTPUT :
          names(list[Cat]) via Sequence[Animal]: ['Tom', 'Kit']
          Mapping[str, Cat] as Mapping[str, Animal]: 1
          Animal-greeter used for cats: ['hi Tom', 'hi Kit']
          Cat-greeter: ['hi Tom (9 lives)', 'hi Kit (7 lives)']
          AttributeError: 'Animal' object has no attribute 'lives'
 NEXT   : lesson04_protocols/protocols.py
=====================================================================
"""

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class Animal:
    name: str


@dataclass(frozen=True)
class Cat(Animal):
    lives: int = 9


# -- 1. CONCEPT: mutable containers are INVARIANT --------------------------
def adopt_any_animal(shelter: list[Animal]) -> None:
    shelter.append(Animal("generic"))  # fine for a list[Animal]...


# If mypy allowed adopt_any_animal(cats) for cats: list[Cat], the list of
# Cats would now hold an Animal, and cats[-1].lives would crash.


# -- 2. CONCEPT: read-only views are COVARIANT ------------------------------
def names(animals: Sequence[Animal]) -> list[str]:
    return [animal.name for animal in animals]  # only READS: a Sequence[Cat] is safe


def count_by_name(animals: Mapping[str, Animal]) -> int:
    return len(animals)


# -- 3. CONCEPT: callable PARAMETERS go the other way (CONTRAVARIANT) ------
def greet_every(cats: Sequence[Cat], greeter: Callable[[Cat], str]) -> list[str]:
    return [greeter(cat) for cat in cats]


def greet_animal(animal: Animal) -> str:  # accepts MORE than Cat: safe as a Cat-greeter
    return f"hi {animal.name}"


def greet_cat(cat: Cat) -> str:
    return f"hi {cat.name} ({cat.lives} lives)"


def main() -> None:
    cats = [Cat("Tom"), Cat("Kit", lives=7)]
    print("names(list[Cat]) via Sequence[Animal]:", names(cats))
    print("Mapping[str, Cat] as Mapping[str, Animal]:", count_by_name({"t": Cat("Tom")}))
    print("Animal-greeter used for cats:", greet_every(cats, greet_animal))
    print("Cat-greeter:", greet_every(cats, greet_cat))

    # At runtime nothing stops this, which is exactly the bug mypy prevents:
    shelter: list[Cat] = [Cat("Tom")]
    adopt_any_animal(shelter)  # type: ignore[arg-type]  # mypy refuses it
    try:
        print([cat.lives for cat in shelter])
    except AttributeError as error:
        print("AttributeError:", error)

    # -- 4. WHY ------------------------------------------------------------
    # Rule of thumb for PARAMETERS: ask for the least you need.
    #   only iterate?          Iterable[T]
    #   index or len()?        Sequence[T]
    #   read a dict?           Mapping[K, V]
    #   really change it?      list[T] / dict[K, V]
    # Callers can then pass lists, tuples, ranges, subclasses... RETURN
    # concrete types (list[T]) so callers get everything.

    # -- 5. PITFALL: list[int] where list[float] is expected ----------------
    # def add_float(numbers: list[float]) -> None: numbers.append(1.5)
    # ints: list[int] = [1]; add_float(ints)
    # mypy: Argument 1 to "add_float" has incompatible type "list[int]";
    #       expected "list[float]"
    # note: "list" is invariant -- ... Consider using "Sequence" instead,
    #       which is covariant
    #
    # def on_int(callback: Callable[[int], None]) -> None: callback(1)
    # def takes_bool(flag: bool) -> None: ...
    # on_int(takes_bool)
    # mypy: incompatible type "Callable[[bool], None]"; expected "Callable[[int], None]"
    # (on_int may call it with 5; a bool-only function can't take that.)

    # -- 6. TRY IT -----------------------------------------------------
    # a) Change names() to take list[Animal]. Run mypy. What changes?
    # b) Pass a tuple of Cats to names(). Does mypy accept it? Why?
    # c) Can you pass greet_cat where Callable[[Animal], str] is expected?


if __name__ == "__main__":
    main()

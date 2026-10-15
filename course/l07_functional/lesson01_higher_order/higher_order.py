"""
=====================================================================
 LESSON 07.1 - Lambdas and higher-order functions
=====================================================================
 GOAL   : Write small anonymous functions with lambda, pass them to
          sorted/max/map/filter, and know when a comprehension or a
          named function reads better.
 RUN    : uv run python -m course.l07_functional.lesson01_higher_order.higher_order
 OUTPUT :
          square(7): 49
          apply_twice(square, 3): 81
          apply_twice(+10, 1): 21
          by age: [('Linus', 21), ('Bo', 21), ('Ada', 36), ('Grace', 85)]
          by age, then name: [('Bo', 21), ('Linus', 21), ('Ada', 36), ('Grace', 85)]
          oldest: Grace
          map: [10, 20, 30, 40, 50, 60]
          filter: [2, 4, 6]
          comprehension: [20, 40, 60]
          map with a built-in: ['A', 'B']
          make_adder(5)(10): 15
          any/all: True True
 NEXT   : lesson02_closures/closures.py
=====================================================================
"""

from collections.abc import Callable

PEOPLE = [("Ada", 36), ("Linus", 21), ("Grace", 85), ("Bo", 21)]


# -- 1. CONCEPT: a higher-order function takes or returns a function ------
def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))


def make_adder(amount: int) -> Callable[[int], int]:
    def add(value: int) -> int:
        return value + amount

    return add  # return the function itself, not add(...)


def main() -> None:
    # -- 2. CONCEPT: lambda = a one-expression function without a name ---
    square: Callable[[int], int] = lambda n: n * n  # noqa: E731 - shown once; prefer `def` for named functions
    print("square(7):", square(7))
    print("apply_twice(square, 3):", apply_twice(lambda n: n * n, 3))
    print("apply_twice(+10, 1):", apply_twice(lambda n: n + 10, 1))

    # The most common use: a key= for sorted, min, max.
    print("by age:", sorted(PEOPLE, key=lambda person: person[1]))
    print("by age, then name:", sorted(PEOPLE, key=lambda person: (person[1], person[0])))
    print("oldest:", max(PEOPLE, key=lambda person: person[1])[0])

    # map and filter return LAZY iterators (lesson 04); list() runs them.
    numbers = [1, 2, 3, 4, 5, 6]
    print("map:", list(map(lambda n: n * 10, numbers)))
    print("filter:", list(filter(lambda n: n % 2 == 0, numbers)))
    print("comprehension:", [n * 10 for n in numbers if n % 2 == 0])
    print("map with a built-in:", list(map(str.upper, ["a", "b"])))

    add_five = make_adder(5)
    print("make_adder(5)(10):", add_five(10))
    print("any/all:", any(n > 5 for n in numbers), all(n > 0 for n in numbers))

    # -- 3. WHY ----------------------------------------------------------
    # Passing behaviour as an argument lets ONE function (sorted) serve
    # every ordering you can think of. Lambdas keep tiny one-off rules
    # right where they are used.

    # -- 4. PITFALL: lambdas that grow up ---------------------------------
    # - A lambda holds ONE expression: no statements, no type hints.
    # - `name = lambda ...` is a def in disguise; ruff (E731) and PEP 8 say
    #   use def: it gets a real name in tracebacks.
    # - map(lambda ...) + filter(lambda ...) is usually clearer as a
    #   comprehension. Use map/filter when you already have a named function.

    # -- 5. TRY IT -----------------------------------------------------
    # a) Sort PEOPLE by name length, longest first (reverse=True).
    # b) Use filter with str.isdigit to keep only digits from ["1", "a", "22"].
    # c) Write make_multiplier(n) like make_adder and use it with map().


if __name__ == "__main__":
    main()

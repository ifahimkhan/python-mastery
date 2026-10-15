"""
=====================================================================
 LESSON 07.2 - Closures
=====================================================================
 GOAL   : Understand how an inner function remembers variables of the
          function that made it, keep private state with nonlocal, and
          avoid the late-binding trap in loops.
 RUN    : uv run python -m course.l07_functional.lesson02_closures.closures
 OUTPUT :
          Hello, Ada! Hola, Ada!
          captured: ['Hello']
          first: 1 2 3
          second: 1  (its own count)
          running average: 30.0
          late binding: [2, 2, 2]
          factory fix: [0, 1, 2]
 NEXT   : lesson03_decorators/decorators.py
=====================================================================
"""

from collections.abc import Callable


# -- 1. CONCEPT: a closure = a function + the variables it captured ------
def make_greeter(greeting: str) -> Callable[[str], str]:
    def greet(name: str) -> str:
        return f"{greeting}, {name}!"  # `greeting` lives on after make_greeter returns

    return greet


# -- 2. CONCEPT: nonlocal lets the inner function CHANGE captured state --
def make_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count  # without this, `count += 1` makes a NEW local count
        count += 1
        return count

    return counter


def make_getter(value: int) -> Callable[[], int]:
    def get() -> int:
        return value

    return get


def make_average() -> Callable[[float], float]:
    values: list[float] = []  # mutating a captured list needs no nonlocal

    def add(value: float) -> float:
        values.append(value)
        return sum(values) / len(values)

    return add


def main() -> None:
    hello = make_greeter("Hello")
    hola = make_greeter("Hola")
    print(hello("Ada"), hola("Ada"))
    print("captured:", [cell.cell_contents for cell in hello.__closure__ or ()])

    first, second = make_counter(), make_counter()
    print("first:", first(), first(), first())
    print("second:", second(), " (its own count)")

    average = make_average()
    average(10)
    average(20)
    print("running average:", average(60))

    # -- 3. PITFALL: late binding in a loop ------------------------------
    # The closure captures the VARIABLE i, not its value at that moment.
    late: list[Callable[[], int]] = [lambda: i for i in range(3)]  # noqa: B023 - on purpose
    print("late binding:", [func() for func in late])
    # Fix: build each function in its OWN call, so each captures its own value.
    # (You'll also see the trick `lambda i=i: i`: a default freezes the value.)
    fixed = [make_getter(i) for i in range(3)]
    print("factory fix:", [func() for func in fixed])

    # -- 4. WHY ------------------------------------------------------------
    # A closure is a tiny object with ONE method and private state, with no
    # class needed. Decorators (next lesson) are built from closures.
    # Once you need several methods or visible state, write a class.

    # -- 5. PITFALL: forgetting nonlocal ------------------------------------
    # def counter() -> int:
    #     count += 1
    # UnboundLocalError: cannot access local variable 'count' where it is
    # not associated with a value

    # -- 6. TRY IT -----------------------------------------------------
    # a) Write make_limiter(n): a function that returns True for its first
    #    n calls and False afterwards.
    # b) Give make_counter a `step` parameter.
    # c) Rewrite make_counter as a class with __call__. Which is clearer?


if __name__ == "__main__":
    main()

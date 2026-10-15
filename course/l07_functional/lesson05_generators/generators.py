"""
=====================================================================
 LESSON 07.5 - Generators
=====================================================================
 GOAL   : Write iterators the easy way with `yield`, chain generators
          into lazy pipelines, delegate with `yield from`, and use
          endless generators safely.
 RUN    : uv run python -m course.l07_functional.lesson05_generators.generators
 OUTPUT :
          created, nothing ran yet: generator
            (countdown starts)
          next: 2
          next: 1
            (countdown ends)
          rest: []
          first 5 naturals: [1, 2, 3, 4, 5]
          first 3 even squares: [4, 16, 36]
          errors: ['disk full', 'disk still full']
          flatten: [1, 2, 3]
          sum of squares to 1000: 333833500
 NEXT   : lesson06_itertools/itertools_tour.py
=====================================================================
"""

from collections.abc import Iterable, Iterator

LOG = """INFO start
ERROR disk full
INFO retry
ERROR disk still full
INFO done"""


# -- 1. CONCEPT: a function with `yield` returns a generator -------------
def countdown(start: int) -> Iterator[int]:
    print("  (countdown starts)")
    while start > 0:
        yield start  # hand out one value, then PAUSE here until next()
        start -= 1
    print("  (countdown ends)")


# -- 2. CONCEPT: endless generators are fine, if you only take a few ------
def naturals() -> Iterator[int]:
    n = 1
    while True:
        yield n
        n += 1


def take(count: int, items: Iterable[int]) -> list[int]:
    result: list[int] = []
    for item in items:
        if len(result) == count:
            break
        result.append(item)
    return result


# -- 3. CONCEPT: pipelines: each step pulls one item from the step before --
def lines(text: str) -> Iterator[str]:
    yield from text.splitlines()  # `yield from` = yield every item of an iterable


def only(level: str, rows: Iterable[str]) -> Iterator[str]:
    for row in rows:
        if row.startswith(level):
            yield row


def messages(rows: Iterable[str]) -> Iterator[str]:
    for row in rows:
        yield row.split(" ", 1)[1]


def flatten(nested: Iterable[Iterable[int]]) -> Iterator[int]:
    for inner in nested:
        yield from inner


def main() -> None:
    gen = countdown(2)
    print("created, nothing ran yet:", type(gen).__name__)
    print("next:", next(gen))
    print("next:", next(gen))
    print("rest:", list(gen))

    print("first 5 naturals:", take(5, naturals()))
    print("first 3 even squares:", take(3, (n * n for n in naturals() if n % 2 == 0)))

    pipeline = messages(only("ERROR", lines(LOG)))
    print("errors:", list(pipeline))
    print("flatten:", list(flatten([[1, 2], [], [3]])))

    # A generator expression is a lazy list comprehension: ( ) not [ ].
    print("sum of squares to 1000:", sum(n * n for n in range(1, 1001)))

    # -- 4. WHY ------------------------------------------------------------
    # A generator is an iterator (lesson 04) without the class: Python
    # writes __iter__/__next__ for you and remembers where you paused.
    # Pipelines handle huge inputs with almost no memory, one item at a time.

    # -- 5. PITFALL: generators are used up, and run lazily -----------------
    # gen = countdown(3); list(gen); list(gen)   -> [3, 2, 1] then []
    # A bug inside a generator only shows when you iterate, not when you
    # call it. And list(naturals()) never finishes: always limit endless ones.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Write fibonacci() as an endless generator and take(10, fibonacci()).
    # b) Add a step to the pipeline that upper-cases every message.
    # c) Write chunks(items, size) that yields lists of `size` items.


if __name__ == "__main__":
    main()

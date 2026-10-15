"""
=====================================================================
 LESSON 07.7 - functools
=====================================================================
 GOAL   : Cache results with @cache / @lru_cache, fix some arguments
          with partial, fold a sequence with reduce, and compute an
          attribute once with @cached_property.
 RUN    : uv run python -m course.l07_functional.lesson07_functools.functools_tour
 OUTPUT :
          slow_fib(20) made 21891 calls
          fast_fib(90): 2880067194370816120
          cache info: CacheInfo(hits=88, misses=91, maxsize=None, currsize=91)
          lru_cache(maxsize=2) did 4 real lookups for 6 calls
          square(7), cube(2): 49 8
          int('1011', base=2): 11
          reduce add: 14
          reduce mul: 60
          reduce on empty, with a start: 1
          most numbers have a built-in: 14 5
          total: 60 60 computed 1 time
 NEXT   : ../README.md, then the exercises
=====================================================================
"""

import functools
import operator

CALLS: list[int] = []


# -- 1. CONCEPT: @cache remembers results by argument ---------------------
def slow_fib(n: int) -> int:
    CALLS.append(n)
    return n if n < 2 else slow_fib(n - 1) + slow_fib(n - 2)


@functools.cache
def fast_fib(n: int) -> int:
    return n if n < 2 else fast_fib(n - 1) + fast_fib(n - 2)


@functools.lru_cache(maxsize=2)  # keeps only the 2 most recently used results
def lookup(key: str) -> str:
    CALLS.append(len(key))
    return key.upper()


# -- 4. CONCEPT: @cached_property computes once, on first use --------------
class Report:
    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers
        self.computations = 0

    @functools.cached_property
    def total(self) -> int:
        self.computations += 1
        return sum(self.numbers)


def power(base: int, exponent: int) -> int:
    return int(base**exponent)


def main() -> None:
    slow_fib(20)
    print("slow_fib(20) made", len(CALLS), "calls")
    print("fast_fib(90):", fast_fib(90))
    print("cache info:", fast_fib.cache_info())

    CALLS.clear()
    for key in ["a", "b", "a", "c", "a", "b"]:
        lookup(key)
    print("lru_cache(maxsize=2) did", len(CALLS), "real lookups for 6 calls")

    # -- 2. CONCEPT: partial pre-fills arguments --------------------------
    square = functools.partial(power, exponent=2)
    cube = functools.partial(power, exponent=3)
    print("square(7), cube(2):", square(7), cube(2))
    to_int_base2 = functools.partial(int, base=2)
    print("int('1011', base=2):", to_int_base2("1011"))

    # -- 3. CONCEPT: reduce folds a sequence into one value ---------------
    numbers = [3, 1, 4, 1, 5]
    print("reduce add:", functools.reduce(operator.add, numbers))
    print("reduce mul:", functools.reduce(operator.mul, numbers, 1))
    print("reduce on empty, with a start:", functools.reduce(operator.mul, [], 1))
    print("most numbers have a built-in:", sum(numbers), max(numbers))

    report = Report([10, 20, 30])
    print("total:", report.total, report.total, "computed", report.computations, "time")

    # -- 5. WHY ------------------------------------------------------------
    # Caching turns slow_fib's exponential calls into one call per n.
    # partial names a specialised function without writing a new def.

    # -- 6. PITFALL: what you can and can't cache ---------------------------
    # - Arguments must be hashable: fast_fib([1]) raises
    #   TypeError: unhashable type: 'list'
    # - Never cache functions with side effects or changing answers
    #   (reading the clock, random numbers, the current balance).
    # - @cache never forgets: an unbounded cache can eat memory.
    #   Use lru_cache(maxsize=...) for big inputs.
    # - reduce on an empty sequence WITHOUT a start value raises TypeError.

    # -- 7. TRY IT -----------------------------------------------------
    # a) Remove @functools.cache from fast_fib and try fast_fib(35). Feel it.
    # b) Make print_error = partial(print, "ERROR:") and call it.
    # c) Use reduce to find the longest word in a list (no max()).


if __name__ == "__main__":
    main()

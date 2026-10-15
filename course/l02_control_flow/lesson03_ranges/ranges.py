"""
=====================================================================
 LESSON 02.3 - range(): sequences of whole numbers
=====================================================================
 GOAL   : Describe a run of numbers with range(start, stop, step),
          and remember that stop is never included.
 RUN    : uv run python -m course.l02_control_flow.lesson03_ranges.ranges
 OUTPUT :
          range(5): 0 1 2 3 4
          range(2, 6): 2 3 4 5
          range(0, 20, 5): 0 5 10 15
          range(5, 0, -1): 5 4 3 2 1
          reversed(range(3)): 2 1 0
          len(range(0, 100, 7)) = 15
          7 in range(10): True
          10 in range(10): False
          range(5, 0) is empty: True
          sum(range(1, 101)) = 5050
 NOTE   : `print(*range(5))` hands every number to print() as its own
          argument, so they come out with spaces between them.
 NEXT   : lesson04_for_loops/for_loops.py
=====================================================================
"""


def main() -> None:
    # -- 1. CONCEPT: range(stop), range(start, stop), range(start, stop, step)
    # Like slicing (lesson 01.4): start is included, stop is NOT.
    print("range(5):", *range(5))
    print("range(2, 6):", *range(2, 6))
    print("range(0, 20, 5):", *range(0, 20, 5))
    # A negative step counts down. The stop is still excluded: 0 is not printed.
    print("range(5, 0, -1):", *range(5, 0, -1))
    print("reversed(range(3)):", *reversed(range(3)))

    # -- 2. WHY: a range is tiny, whatever its size ---------------------
    # range() doesn't store the numbers: it computes them when asked.
    # So len() and `in` are instant, even for range(10 ** 12).
    print("len(range(0, 100, 7)) =", len(range(0, 100, 7)))
    print("7 in range(10):", 7 in range(10))
    print("10 in range(10):", 10 in range(10))

    # -- 3. PITFALL: going down needs a negative step -------------------
    # range(5, 0) counts UP from 5 to 0, which is nothing at all:
    print("range(5, 0) is empty:", len(range(5, 0)) == 0)
    # The classic off-by-one: the numbers 1 to 100 are range(1, 101), not range(1, 100).
    print("sum(range(1, 101)) =", sum(range(1, 101)))
    # Ranges take whole numbers only:
    #   range(0, 1, 0.1)   # TypeError: 'float' object cannot be interpreted as an integer
    #   range(0, 5, 0)     # ValueError: range() arg 3 must not be zero

    # -- 4. TRY IT -----------------------------------------------------
    # a) Print the even numbers from 2 to 20, both included.
    # b) Print a countdown from 10 to 0, both included.
    # c) How many numbers below 1000 are multiples of 7? Use len(range(...)).


if __name__ == "__main__":
    main()

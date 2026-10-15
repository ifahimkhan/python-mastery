"""
=====================================================================
 LESSON 04.5 - Comprehensions
=====================================================================
 GOAL   : Build lists, dicts and sets in one readable line, with an
          optional filter, and know when a plain loop is clearer.
 RUN    : uv run python -m course.l04_collections.lesson05_comprehensions.comprehensions
 OUTPUT :
          loop:          [1, 4, 9, 16, 25]
          comprehension: [1, 4, 9, 16, 25]
          evens squared: [4, 16]
          labels: ['odd', 'even', 'odd', 'even', 'odd']
          lengths: {'kiwi': 4, 'apple': 5, 'fig': 3}
          first letters: ['a', 'b', 'c']
          pairs: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
          flat: [1, 2, 3, 4, 5]
          table: [[1, 2, 3], [2, 4, 6]]
          sum of squares: 55
          any negative: False  all positive: True
 NEXT   : lesson06_copying/copying.py
=====================================================================
"""


def main() -> None:
    numbers = [1, 2, 3, 4, 5]

    # -- 1. CONCEPT: [expression for item in iterable] --------------------
    # These two build the same list:
    squares = []
    for n in numbers:
        squares.append(n * n)
    print("loop:         ", squares)
    print("comprehension:", [n * n for n in numbers])

    # -- 2. CONCEPT: filtering with if ---------------------------------
    # [expression for item in iterable if condition]
    print("evens squared:", [n * n for n in numbers if n % 2 == 0])
    # An if/else in the EXPRESSION chooses a value for every item (no filtering):
    print("labels:", ["even" if n % 2 == 0 else "odd" for n in numbers])

    # -- 3. CONCEPT: dict and set comprehensions -------------------------
    fruits = ["kiwi", "apple", "fig"]
    print("lengths:", {fruit: len(fruit) for fruit in fruits})
    print("first letters:", sorted({word[0] for word in ["apple", "bean", "avocado", "corn"]}))

    # -- 4. CONCEPT: several for clauses (read them left to right) ----
    print("pairs:", [(n, letter) for n in [1, 2] for letter in "ab"])
    nested = [[1, 2], [3], [4, 5]]
    print("flat:", [item for row in nested for item in row])  # same order as nested loops
    print("table:", [[row * col for col in range(1, 4)] for row in range(1, 3)])

    # -- 5. CONCEPT: generator expressions -------------------------------
    # Round brackets (or none inside a call) compute items one by one
    # without building a list first (level 07). Ideal with sum/any/all/max.
    print("sum of squares:", sum(n * n for n in numbers))
    any_negative = any(n < 0 for n in numbers)
    all_positive = all(n > 0 for n in numbers)
    print("any negative:", any_negative, " all positive:", all_positive)

    # -- 6. WHY: say WHAT you build, not HOW ---------------------------
    # A comprehension reads like the description of the result: "the
    # square of n for every n in numbers if n is even". Use a plain loop
    # when the body needs several steps, prints, or side effects.

    # -- 7. PITFALL: too clever to read --------------------------------
    #   [x for row in grid if row for x in row if x % 2 if x > 3]
    # Correct, but nobody wants to read it. If a comprehension needs more
    # than one line or more than one condition, write the loop instead.
    # And don't use a comprehension just for side effects:
    #   [print(n) for n in numbers]   # builds a useless list of None

    # -- 8. TRY IT -----------------------------------------------------
    # a) Build ["A!", "B!", "C!"] from "abc".
    # b) Build {n: n ** 3 for ...} for n from 1 to 5.
    # c) Count the words longer than 3 letters in "the quick brown fox" with sum(...).


if __name__ == "__main__":
    main()

"""
=====================================================================
 LESSON 04.6 - Names, references and copies
=====================================================================
 GOAL   : Understand that = never copies, make shallow and deep copies
          on purpose, and avoid changing a caller's list by accident.
 RUN    : uv run python -m course.l04_collections.lesson06_copying.copying
 OUTPUT :
          a = [1, 2, 3, 4]  b = [1, 2, 3, 4]  same object: True
          original: [1, 2, 3]  copy: [1, 2, 3, 99]
          shallow copy shares inner lists: [[1, 2, 99], [3]]
          deep copy is independent:        [[1, 2], [3]]
          bad grid:  [['X', '.', '.'], ['X', '.', '.'], ['X', '.', '.']]
          good grid: [['X', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
          caller's list after add_bonus_in_place: [11, 21]
          caller's list after with_bonus: [11, 21]  result: [21, 31]
          a tuple is safe to share: (1, 2, 3)
 NEXT   : lesson07_collections_module/collections_module.py
=====================================================================
"""

import copy

GRID_SIZE = 3
BONUS = 10


def add_bonus_in_place(scores: list[int]) -> None:
    """Changes the caller's list! Surprising unless the name says so."""
    for i in range(len(scores)):
        scores[i] += BONUS


def with_bonus(scores: list[int]) -> list[int]:
    """Returns a NEW list and leaves the argument alone. Prefer this style."""
    return [score + BONUS for score in scores]


def main() -> None:
    # -- 1. CONCEPT: = gives a second NAME to the SAME object -------------
    a = [1, 2, 3]
    b = a  # no copy!
    b.append(4)
    print("a =", a, " b =", b, " same object:", a is b)

    # -- 2. CONCEPT: shallow copies ---------------------------------------
    # list(x), x.copy() and x[:] build a new OUTER list.
    original = [1, 2, 3]
    duplicate = original.copy()
    duplicate.append(99)
    print("original:", original, " copy:", duplicate)

    # But the items inside are shared. With lists inside a list, that matters:
    nested = [[1, 2], [3]]
    shallow = nested.copy()
    deep = copy.deepcopy(nested)  # copies everything, all the way down
    shallow[0].append(99)
    print("shallow copy shares inner lists:", nested)
    print("deep copy is independent:       ", deep)

    # -- 3. PITFALL: [[...]] * n repeats ONE inner list -------------------
    bad_grid = [["."] * GRID_SIZE] * GRID_SIZE  # three references to one row
    bad_grid[0][0] = "X"
    print("bad grid: ", bad_grid)
    good_grid = [["."] * GRID_SIZE for _ in range(GRID_SIZE)]  # a new row each time
    good_grid[0][0] = "X"
    print("good grid:", good_grid)

    # -- 4. WHY: functions receive the SAME object, not a copy ------------
    scores = [1, 11]
    add_bonus_in_place(scores)
    print("caller's list after add_bonus_in_place:", scores)
    result = with_bonus(scores)
    print("caller's list after with_bonus:", scores, " result:", result)
    # Returning new values (immutable style) keeps surprises away: the
    # caller's data only changes when the caller decides to change it.

    # Immutable values (int, str, tuple) can be shared freely: nobody can
    # change them behind your back.
    point = (1, 2, 3)
    print("a tuple is safe to share:", point)

    # -- 5. PITFALL: changing a list while looping over it ---------------
    #   numbers = [1, 2, 2, 3]
    #   for n in numbers:
    #       if n == 2:
    #           numbers.remove(n)   # skips items: leaves [1, 2, 3]!
    # Build a new list instead: numbers = [n for n in numbers if n != 2]

    # -- 6. TRY IT -----------------------------------------------------
    # a) Run the pitfall above and print the result. Why is one 2 left?
    # b) Make a copy of {"a": [1]} with dict(...), change the inner list, print both.
    # c) Use `is` to check whether list(original) is original.


if __name__ == "__main__":
    main()

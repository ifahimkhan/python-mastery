"""
=====================================================================
 LESSON 04.2 - Tuples and unpacking
=====================================================================
 GOAL   : Group a fixed number of values in a tuple, unpack them into
          names, and know when a tuple beats a list.
 RUN    : uv run python -m course.l04_collections.lesson02_tuples.tuples
 OUTPUT :
          point: (3, 4)  x = 3  y = 4
          rgb: (255, 128, 0)
          single: ('a',) <class 'tuple'>  not a tuple: a <class 'str'>
          name = Ada, born = 1815
          first = 1, rest = [2, 3, 4, 5]
          head = 1, middle = [2, 3, 4], tail = 5
          min and max: (1, 9)
          distance from (0, 0) to (3, 4): 5.0
          pairs: ('Ada', 36) ('Linus', 54)
          Ada is 36
          Linus is 54
          (1, 2) < (1, 3): True
          locations[(52, 13)] = Berlin
 NEXT   : lesson03_dicts/dicts.py
=====================================================================
"""

import math


def min_and_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)  # returns ONE tuple


def distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    ax, ay = a
    bx, by = b
    return math.hypot(bx - ax, by - ay)


def main() -> None:
    # -- 1. CONCEPT: a tuple is an IMMUTABLE sequence ---------------------
    # Round brackets (often optional). Indexing, slicing, len and `in` work
    # like on lists, but you can't change, add or remove items.
    point = (3, 4)
    x, y = point  # unpacking: one name per item
    print("point:", point, " x =", x, " y =", y)
    rgb = 255, 128, 0  # the commas make the tuple, not the brackets
    print("rgb:", rgb)

    # A one-item tuple needs a trailing comma:
    single = ("a",)
    not_a_tuple = "a"
    print("single:", single, type(single), " not a tuple:", not_a_tuple, type(not_a_tuple))

    # -- 2. CONCEPT: unpacking ------------------------------------------
    name, born = ("Ada", 1815)
    print(f"name = {name}, born = {born}")
    # A starred name collects "the rest" into a LIST:
    first, *rest = [1, 2, 3, 4, 5]
    print(f"first = {first}, rest = {rest}")
    head, *middle, tail = [1, 2, 3, 4, 5]
    print(f"head = {head}, middle = {middle}, tail = {tail}")

    print("min and max:", min_and_max([4, 1, 9, 7]))
    print("distance from (0, 0) to (3, 4):", distance((0, 0), (3, 4)))

    # -- 3. CONCEPT: lists of tuples, unpacked in a loop -----------------
    people = [("Ada", 36), ("Linus", 54)]
    print("pairs:", *people)
    for person_name, age in people:
        print(person_name, "is", age)

    # Tuples compare item by item, left to right (handy for sorting):
    print("(1, 2) < (1, 3):", (1, 2) < (1, 3))

    # -- 4. WHY: tuples for fixed records and as dict keys ---------------
    # A list says "some number of similar things"; a tuple says "exactly
    # these parts" (x and y, name and age). Being immutable, tuples are
    # also HASHABLE, so they can be dict keys and set items (lessons 04.3-4).
    locations = {(52, 13): "Berlin", (48, 2): "Paris"}
    print("locations[(52, 13)] =", locations[(52, 13)])

    # -- 5. PITFALL: tuples can't change, and unpacking must fit ---------
    #   point[0] = 10        # TypeError: 'tuple' object does not support item assignment
    #   a, b = (1, 2, 3)     # ValueError: too many values to unpack (expected 2)
    #   a, b, c = (1, 2)     # ValueError: not enough values to unpack (expected 3, got 2)
    # Careful: a tuple holding a LIST can still see that list change.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Swap two variables with a, b = b, a. Which tuple is built here?
    # b) Unpack "2026-10-15".split("-") into year, month, day.
    # c) Sort [("Bob", 30), ("Al", 30), ("Cy", 25)]. How are ties ordered?


if __name__ == "__main__":
    main()

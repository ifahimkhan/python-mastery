"""
=====================================================================
 LESSON 04.4 - Sets
=====================================================================
 GOAL   : Keep unique items, test membership fast, and combine groups
          with union, intersection and difference.
 RUN    : uv run python -m course.l04_collections.lesson04_sets.sets
 OUTPUT :
          unique visitors: ['ada', 'bob', 'cy']
          count: 3
          'bob' in visitors: True
          after add/discard: ['ada', 'cy', 'dee']
          python | rust: ['Ada', 'Bob', 'Cy', 'Dee']
          python & rust: ['Bob', 'Cy']
          python - rust: ['Ada']
          python ^ rust: ['Ada', 'Dee']
          {'Ada'} <= python: True
          duplicates in [1, 2, 2, 3, 3, 3]: True
          seen in order: ['b', 'a', 'n']
          frozenset as dict key: square
 NOTE   : Sets have no order, so this lesson prints sorted(...) to keep
          the output the same on every run.
 NEXT   : lesson05_comprehensions/comprehensions.py
=====================================================================
"""


def main() -> None:
    # -- 1. CONCEPT: a set holds each item at most once -------------------
    log = ["ada", "bob", "ada", "cy", "bob"]  # who came in, in order
    visitors = set(log)  # duplicates vanish
    print("unique visitors:", sorted(visitors))
    print("count:", len(visitors))
    print("'bob' in visitors:", "bob" in visitors)  # instant, like dict keys

    visitors.add("dee")
    visitors.discard("bob")  # no error if missing (remove() would raise KeyError)
    print("after add/discard:", sorted(visitors))

    # -- 2. CONCEPT: set algebra -------------------------------------------
    python = {"Ada", "Bob", "Cy"}
    rust = {"Bob", "Cy", "Dee"}
    print("python | rust:", sorted(python | rust))  # union: in either
    print("python & rust:", sorted(python & rust))  # intersection: in both
    print("python - rust:", sorted(python - rust))  # difference: only in python
    print("python ^ rust:", sorted(python ^ rust))  # in exactly one of them
    print("{'Ada'} <= python:", {"Ada"} <= python)  # subset test

    # -- 3. WHY: sets answer "is it there?" and "any duplicates?" --------
    numbers = [1, 2, 2, 3, 3, 3]
    print(f"duplicates in {numbers}:", len(set(numbers)) != len(numbers))

    # A set remembers what you've already seen, e.g. to keep the FIRST
    # of every letter while keeping the original order:
    seen: set[str] = set()
    ordered: list[str] = []
    for letter in "banana":
        if letter not in seen:
            seen.add(letter)
            ordered.append(letter)
    print("seen in order:", ordered)

    # frozenset is an immutable set, so it can be a dict key or a set item.
    shapes = {frozenset({"4 sides", "equal sides"}): "square"}
    print("frozenset as dict key:", shapes[frozenset({"equal sides", "4 sides"})])

    # -- 4. PITFALL: {} is an empty DICT, and sets have no order -----------
    #   empty = {}             # a dict! An empty set is set()
    #   {1, 2, 3}[0]           # TypeError: 'set' object is not subscriptable
    #   {[1, 2]}               # TypeError: unhashable type: 'list'
    # Printing a set of strings may show a different order on each run.
    # Use sorted() when the order matters.

    # -- 5. TRY IT -----------------------------------------------------
    # a) Which letters appear in both "python" and "typhoon"?
    # b) Which vowels does "rhythm and blues" NOT contain? (set("aeiou") - ...)
    # c) Print type({}) and type(set()).


if __name__ == "__main__":
    main()

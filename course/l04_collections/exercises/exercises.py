"""
=====================================================================
 LEVEL 04 - EXERCISES (your turn!)
=====================================================================
 HOW    : Replace each `raise NotImplementedError(...)` line with your
          answer. Many fit in one line with a comprehension or a
          collections helper, but a clear loop is just as good.
 RULE   : Never change the list or dict you receive. Build a new one.
          (Careful: numbers.sort() changes the caller's list.)
 CHECK  : uv run pytest -m exercise tests/l04_collections
          or open tests/l04_collections/test_exercises.py and click the
          green arrow next to the class name.
 STUCK? : Re-read the lesson in the hint. Still stuck? Peek at
          ../solutions/solutions.py, but try first!
=====================================================================
"""


class CollectionsExercises:
    # Hint: lesson04_sets (remove duplicates) + lesson01_lists (sorted() vs sort())
    def second_largest(self, numbers: list[int]) -> int | None:
        raise NotImplementedError("Ex 1: second-largest distinct value, or None")

    # Hint: lesson04_sets ("seen in order") or lesson03_dicts (keys keep insertion order)
    def remove_duplicates(self, items: list[str]) -> list[str]:
        raise NotImplementedError("Ex 2: drop duplicates, keep first-seen order")

    # Hint: lesson03_dicts (counting with get) or lesson07_collections_module (Counter)
    def word_frequencies(self, text: str) -> dict[str, int]:
        raise NotImplementedError("Ex 3: {word: count}")

    # Hint: lesson05_comprehensions (dict comprehensions) + lesson03_dicts (items())
    def invert(self, mapping: dict[str, int]) -> dict[int, str]:
        raise NotImplementedError("Ex 4: swap keys and values")

    # Hint: lesson04_sets (intersection)
    def common_elements(self, a: list[int], b: list[int]) -> set[int]:
        raise NotImplementedError("Ex 5: values in both lists")

    # Hint: lesson05_comprehensions (filtering with if)
    def squares_of_evens(self, numbers: list[int]) -> list[int]:
        raise NotImplementedError("Ex 6: squares of the even numbers")

    # Hint: lesson05_comprehensions (several for clauses)
    def flatten(self, nested: list[list[int]]) -> list[int]:
        raise NotImplementedError("Ex 7: one flat list")

    # Hint: lesson07_collections_module (defaultdict) or lesson03_dicts (setdefault)
    def group_by_length(self, words: list[str]) -> dict[int, list[str]]:
        raise NotImplementedError("Ex 8: {length: [words]}")

    # Hint: lesson01_lists (slicing, + on lists) + l01_basics/lesson06_operators (% wraps around)
    def rotate(self, items: list[int], steps: int) -> list[int]:
        raise NotImplementedError("Ex 9: rotate right by steps, as a new list")

    # Hint: lesson07_collections_module (Counter.most_common)
    def top_words(self, text: str, n: int) -> list[tuple[str, int]]:
        raise NotImplementedError("Ex 10: the n most common words with counts")

"""The list of Level 04 exercises.

Both ``exercises/exercises.py`` (your answers) and ``solutions/solutions.py``
(reference answers) implement this Protocol, so the SAME tests check both.

House rule for this level: NEVER change a list or dict you were given.
Build and return a new one. The tests check this.
"""

from typing import Protocol


class CollectionsTasks(Protocol):
    def second_largest(self, numbers: list[int]) -> int | None:
        """Ex 1. Second-largest DISTINCT value, or None if there isn't one.

        second_largest([3, 1, 3, 2]) == 2    second_largest([5, 5]) is None
        """
        ...

    def remove_duplicates(self, items: list[str]) -> list[str]:
        """Ex 2. Same items, duplicates removed, FIRST appearance order kept.

        remove_duplicates(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]
        """
        ...

    def word_frequencies(self, text: str) -> dict[str, int]:
        """Ex 3. How often each word appears, lower-cased, split on whitespace.

        word_frequencies("The cat the") == {"the": 2, "cat": 1}
        """
        ...

    def invert(self, mapping: dict[str, int]) -> dict[int, str]:
        """Ex 4. Swap keys and values. Values are unique.  {"a": 1} -> {1: "a"}"""
        ...

    def common_elements(self, a: list[int], b: list[int]) -> set[int]:
        """Ex 5. Values that appear in both lists.  ([1, 2, 3], [2, 3, 4]) -> {2, 3}"""
        ...

    def squares_of_evens(self, numbers: list[int]) -> list[int]:
        """Ex 6. The square of every even number, in order.  [1, 2, 3, 4] -> [4, 16]"""
        ...

    def flatten(self, nested: list[list[int]]) -> list[int]:
        """Ex 7. One flat list, in order.  [[1, 2], [], [3]] -> [1, 2, 3]"""
        ...

    def group_by_length(self, words: list[str]) -> dict[int, list[str]]:
        """Ex 8. Words grouped by their length, each group in the original order.

        group_by_length(["hi", "cat", "yo"]) == {2: ["hi", "yo"], 3: ["cat"]}
        """
        ...

    def rotate(self, items: list[int], steps: int) -> list[int]:
        """Ex 9. A NEW list rotated right by ``steps`` (negative: left).

        rotate([1, 2, 3, 4], 1) == [4, 1, 2, 3]    rotate([1, 2, 3, 4], -1) == [2, 3, 4, 1]
        Steps larger than the list wrap around; an empty list stays empty.
        """
        ...

    def top_words(self, text: str, n: int) -> list[tuple[str, int]]:
        """Ex 10. The ``n`` most common lower-case words with their counts.

        Most common first; equal counts keep the order in which the words first appear.
        top_words("b a b c a b", 2) == [("b", 3), ("a", 2)]
        """
        ...

"""Shared checks for Level 04.

Subclasses decide WHICH implementation is tested: the learner's exercises
or the reference solutions.
"""

from course.l04_collections.tasks import CollectionsTasks


class CollectionsContract:
    tasks: CollectionsTasks  # set by the subclass

    def test_ex1_second_largest_ignores_duplicates(self) -> None:
        assert self.tasks.second_largest([3, 1, 3, 2]) == 2, "Hint: set() removes the second 3"
        assert self.tasks.second_largest([10, 20]) == 10
        assert self.tasks.second_largest([-1, -5, -3]) == -3

    def test_ex1_second_largest_returns_none_when_missing(self) -> None:
        assert self.tasks.second_largest([]) is None, "An empty list has no second largest"
        assert self.tasks.second_largest([7]) is None
        assert self.tasks.second_largest([5, 5]) is None, "Only ONE distinct value"

    def test_ex1_second_largest_leaves_the_input_alone(self) -> None:
        numbers = [3, 1, 2]
        self.tasks.second_largest(numbers)
        assert numbers == [3, 1, 2], "Hint: sorted() makes a new list, .sort() changes this one"

    def test_ex2_remove_duplicates_keeps_first_order(self) -> None:
        items = ["b", "a", "b", "c", "a"]
        assert self.tasks.remove_duplicates(items) == ["b", "a", "c"], (
            "Hint: list(set(...)) loses the order"
        )
        assert items == ["b", "a", "b", "c", "a"], "Don't change the list you were given"
        assert self.tasks.remove_duplicates([]) == []

    def test_ex3_word_frequencies(self) -> None:
        assert self.tasks.word_frequencies("The cat the") == {"the": 2, "cat": 1}, (
            "Hint: lower() before counting"
        )
        assert self.tasks.word_frequencies("  spaced   out  ") == {"spaced": 1, "out": 1}
        assert self.tasks.word_frequencies("") == {}

    def test_ex4_invert(self) -> None:
        mapping = {"a": 1, "b": 2}
        assert self.tasks.invert(mapping) == {1: "a", 2: "b"}
        assert mapping == {"a": 1, "b": 2}, "Don't change the dict you were given"
        assert self.tasks.invert({}) == {}

    def test_ex5_common_elements(self) -> None:
        assert self.tasks.common_elements([1, 2, 3], [2, 3, 4]) == {2, 3}, "Hint: set & set"
        assert self.tasks.common_elements([1, 1, 2], [1, 1]) == {1}
        assert self.tasks.common_elements([1], [2]) == set()

    def test_ex6_squares_of_evens(self) -> None:
        assert self.tasks.squares_of_evens([1, 2, 3, 4]) == [4, 16]
        assert self.tasks.squares_of_evens([-2, 0, 5]) == [4, 0], "0 and -2 are even"
        assert self.tasks.squares_of_evens([]) == []

    def test_ex7_flatten(self) -> None:
        assert self.tasks.flatten([[1, 2], [], [3]]) == [1, 2, 3]
        assert self.tasks.flatten([]) == []
        assert self.tasks.flatten([[5, 4], [3, 2, 1]]) == [5, 4, 3, 2, 1], "Keep the order"

    def test_ex8_group_by_length(self) -> None:
        assert self.tasks.group_by_length(["hi", "cat", "yo"]) == {2: ["hi", "yo"], 3: ["cat"]}
        assert self.tasks.group_by_length([]) == {}
        assert self.tasks.group_by_length(["", "a"]) == {0: [""], 1: ["a"]}

    def test_ex9_rotate(self) -> None:
        assert self.tasks.rotate([1, 2, 3, 4], 1) == [4, 1, 2, 3]
        assert self.tasks.rotate([1, 2, 3, 4], -1) == [2, 3, 4, 1], "Negative steps go left"
        assert self.tasks.rotate([1, 2, 3, 4], 0) == [1, 2, 3, 4]
        assert self.tasks.rotate([1, 2, 3, 4], 6) == [3, 4, 1, 2], "Hint: steps % len(items)"
        assert self.tasks.rotate([], 3) == [], "Hint: an empty list can't be rotated (or % by 0)"

    def test_ex9_rotate_returns_a_new_list(self) -> None:
        items = [1, 2, 3]
        result = self.tasks.rotate(items, 1)
        assert items == [1, 2, 3], "Don't change the list you were given"
        assert result is not items, "Return a NEW list, even for 0 steps"

    def test_ex10_top_words(self) -> None:
        assert self.tasks.top_words("b a b c a b", 2) == [("b", 3), ("a", 2)]
        assert self.tasks.top_words("x y z", 2) == [("x", 1), ("y", 1)], (
            "Hint: equal counts keep first-seen order (Counter.most_common does)"
        )
        assert self.tasks.top_words("A a", 5) == [("a", 2)], "Lower-case first"
        assert self.tasks.top_words("", 3) == []

"""Shared checks for Level 08.

Subclasses decide WHICH implementation is tested: the learner's exercises
or the reference solutions. (mypy checks the types; these tests check the
behaviour.)
"""

from dataclasses import dataclass

import pytest

from course.l08_typing.tasks import Json, StackLike, TypingTasks


@dataclass(frozen=True)
class _Version:
    """Comparable only through __lt__ (no max() support needed)."""

    number: int
    label: str

    def __lt__(self, other: "_Version") -> bool:
        return self.number < other.number


def _first_letter(word: str) -> str:
    return word[0]


def _divide_ten(by: int) -> float:
    return 10 / by


DATA: Json = {"users": [{"name": "Ada", "tags": ["admin", "dev"]}, {"name": "Bo"}], "count": 2}


class TypingContract:
    tasks: TypingTasks  # set by the subclass

    def test_ex1_first_or_default(self) -> None:
        assert self.tasks.first_or_default([3, 4], 0) == 3
        assert self.tasks.first_or_default([], "none") == "none"
        assert self.tasks.first_or_default("xyz", "-") == "x", "Any Sequence works"

    def test_ex2_stack_push_pop_peek(self) -> None:
        stack: StackLike[str] = self.tasks.make_stack()
        assert len(stack) == 0
        assert stack.peek() is None, "Hint: peek() on an empty stack returns None"
        stack.push("a")
        stack.push("b")
        assert (len(stack), stack.peek()) == (2, "b")
        assert stack.pop() == "b"
        assert stack.pop() == "a"
        assert len(stack) == 0

    def test_ex2_pop_from_empty_stack(self) -> None:
        stack: StackLike[int] = self.tasks.make_stack()
        with pytest.raises(IndexError, match="pop from empty stack"):
            stack.pop()

    def test_ex2_stacks_are_independent(self) -> None:
        first: StackLike[int] = self.tasks.make_stack()
        second: StackLike[int] = self.tasks.make_stack()
        first.push(1)
        assert len(second) == 0, "Hint: create the list in __init__"

    def test_ex3_largest(self) -> None:
        assert self.tasks.largest([3, 9, 2]) == 9
        assert self.tasks.largest(["pear", "apple"]) == "pear"
        assert self.tasks.largest([]) is None

    def test_ex3_largest_uses_only_less_than_and_keeps_the_first(self) -> None:
        a, b = _Version(2, "first"), _Version(2, "second")
        result = self.tasks.largest([_Version(1, "old"), a, b])
        assert result is a, "Hint: replace best only when best < item (strictly)"

    def test_ex4_group_by(self) -> None:
        groups = self.tasks.group_by(["ant", "bee", "ape", "cow"], _first_letter)
        assert groups == {"a": ["ant", "ape"], "b": ["bee"], "c": ["cow"]}
        assert list(groups) == ["a", "b", "c"], "Keys in first-seen order"
        assert self.tasks.group_by([], _first_letter) == {}
        assert self.tasks.group_by([1, 2, 3, 4], lambda n: n % 2 == 0) == {
            False: [1, 3],
            True: [2, 4],
        }

    def test_ex5_parse_user(self) -> None:
        assert self.tasks.parse_user({"name": "Ada", "age": 36}) == {"name": "Ada", "age": 36}
        full = {"name": "Bo", "age": 9, "email": "bo@example.com", "extra": "ignored"}
        assert self.tasks.parse_user(full) == {"name": "Bo", "age": 9, "email": "bo@example.com"}

    @pytest.mark.parametrize(
        ("data", "message"),
        [
            ({"age": 3}, "name must be str"),
            ({"name": 7, "age": 3}, "name must be str"),
            ({"name": "Ada"}, "age must be int"),
            ({"name": "Ada", "age": "36"}, "age must be int"),
            ({"name": "Ada", "age": True}, "age must be int"),
            ({"name": "Ada", "age": 3, "email": None}, "email must be str"),
        ],
    )
    def test_ex5_parse_user_rejects_bad_data(self, data: dict[str, object], message: str) -> None:
        self.tasks.parse_user({"name": "ok", "age": 1})
        with pytest.raises(TypeError, match=message):
            self.tasks.parse_user(data)

    def test_ex6_move(self) -> None:
        assert self.tasks.move((0, 0), "up") == (0, 1)
        assert self.tasks.move((0, 0), "down") == (0, -1)
        assert self.tasks.move((5, 5), "left") == (4, 5)
        assert self.tasks.move((5, 5), "right") == (6, 5)

    def test_ex7_parse_number(self) -> None:
        whole = self.tasks.parse_number("42")
        fraction = self.tasks.parse_number("2.5", as_float=True)
        assert whole == 42 and type(whole) is int
        assert fraction == 2.5 and type(fraction) is float
        assert type(self.tasks.parse_number("3", as_float=True)) is float
        with pytest.raises(ValueError):
            self.tasks.parse_number("2.5")

    def test_ex8_is_str_list(self) -> None:
        assert self.tasks.is_str_list(["a", "b"]) is True
        assert self.tasks.is_str_list([]) is True, "Hint: all() of nothing is True"
        assert self.tasks.is_str_list(["a", 1]) is False
        assert self.tasks.is_str_list([None]) is False

    def test_ex9_with_fallback(self) -> None:
        safe_divide = self.tasks.with_fallback(_divide_ten, -1.0)
        assert safe_divide(4) == 2.5
        assert safe_divide(0) == -1.0, "Hint: catch Exception, return fallback"
        assert getattr(safe_divide, "__name__", None) == "_divide_ten", "Hint: functools.wraps"

    def test_ex10_get_path(self) -> None:
        assert self.tasks.get_path(DATA, ["count"]) == 2
        assert self.tasks.get_path(DATA, ["users", 0, "tags", 1]) == "dev"
        assert self.tasks.get_path(DATA, ["users", 1]) == {"name": "Bo"}
        assert self.tasks.get_path(DATA, []) == DATA, "An empty path is the data itself"

    @pytest.mark.parametrize(
        "path",
        [
            ["missing"],
            ["users", 5],
            ["users", -1],
            ["users", "0"],
            ["count", "x"],
            ["users", 0, "tags", 0, "deeper"],
        ],
    )
    def test_ex10_get_path_returns_none_when_a_step_does_not_fit(
        self, path: list[str | int]
    ) -> None:
        self.tasks.get_path(DATA, [])
        assert self.tasks.get_path(DATA, path) is None

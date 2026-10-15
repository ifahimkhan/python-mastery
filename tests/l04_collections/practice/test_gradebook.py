import pytest

from course.l04_collections.practice.gradebook.gradebook import (
    Gradebook,
    add_score,
    average,
    averages,
    distribution,
    letter,
    ranking,
)


def test_add_score_returns_a_new_book_and_keeps_the_old_one() -> None:
    book: Gradebook = {"Ada": [90]}
    updated = add_score(book, "Ada", 80)
    assert updated == {"Ada": [90, 80]}
    assert book == {"Ada": [90]}, "the original book must not change"


def test_add_score_does_not_share_inner_lists() -> None:
    book: Gradebook = {"Ada": [90]}
    updated = add_score(book, "Bob", 70)
    updated["Ada"].append(1)
    assert book["Ada"] == [90], "a shallow copy would share Ada's list"


def test_add_score_creates_new_students() -> None:
    assert add_score({}, "Bob", 70) == {"Bob": [70]}


def test_average_of_no_scores_is_zero() -> None:
    assert average([]) == 0.0
    assert average([80, 90]) == pytest.approx(85.0)


def test_averages_round_to_one_decimal() -> None:
    assert averages({"Ada": [95, 88, 92]}) == {"Ada": 91.7}


@pytest.mark.parametrize(
    ("score", "grade"), [(100, "A"), (90, "A"), (89.9, "B"), (70, "C"), (60, "D"), (59.9, "F")]
)
def test_letter_uses_inclusive_lower_limits(score: float, grade: str) -> None:
    assert letter(score) == grade


def test_ranking_best_first_with_ties_by_name() -> None:
    book: Gradebook = {"Cy": [80], "Al": [90], "Bo": [80]}
    assert ranking(book) == [("Al", 90.0), ("Bo", 80.0), ("Cy", 80.0)]


def test_distribution_lists_every_grade() -> None:
    book: Gradebook = {"Al": [95], "Bo": [50], "Cy": [91]}
    assert distribution(book) == {"A": 2, "B": 0, "C": 0, "D": 0, "F": 1}
    assert distribution({}) == {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

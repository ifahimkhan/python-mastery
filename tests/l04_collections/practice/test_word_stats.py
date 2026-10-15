import pytest

from course.l04_collections.practice.word_stats.word_stats import (
    average_length,
    bar_chart,
    count_sentences,
    longest_words,
    top_words,
    unique_words,
    words,
)


def test_words_lowercases_and_strips_punctuation() -> None:
    assert words("Hello, World! Hello.") == ["hello", "world", "hello"]


def test_words_drops_pure_punctuation() -> None:
    assert words("wait ... what?!") == ["wait", "what"]
    assert words("") == []


def test_unique_words() -> None:
    assert unique_words(["a", "b", "a"]) == {"a", "b"}


def test_longest_words_breaks_ties_alphabetically() -> None:
    assert longest_words(["bb", "aa", "c", "ddd", "aa"], 3) == ["ddd", "aa", "bb"]
    assert longest_words([], 3) == []


def test_average_length_handles_empty_lists() -> None:
    assert average_length(["ab", "abcd"]) == pytest.approx(3.0)
    assert average_length([]) == 0.0


def test_top_words_keeps_first_seen_order_on_ties() -> None:
    assert top_words(["b", "a", "b", "a", "c"], 2) == [("b", 2), ("a", 2)]


def test_bar_chart_aligns_the_bars() -> None:
    assert bar_chart([("is", 3), ("python", 1)]) == ["is     ### 3", "python # 1"]
    assert bar_chart([]) == []


def test_count_sentences() -> None:
    assert count_sentences("One. Two! Three?") == 3
    assert count_sentences("no end mark") == 0

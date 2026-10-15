import pytest

from course.l03_functions.practice.text_tools.text_tools import (
    initials,
    is_palindrome,
    letters_only,
    slugify,
    title_case,
    truncate,
    word_count,
)


@pytest.mark.parametrize(
    ("text", "count"), [("", 0), ("one", 1), ("  two   words  ", 2), ("tab\tand\nnewline", 3)]
)
def test_word_count_splits_on_any_whitespace(text: str, count: int) -> None:
    assert word_count(text) == count


def test_title_case_lowers_the_rest_of_each_word() -> None:
    assert title_case("hELLO wORLD") == "Hello World"
    assert title_case("") == ""


def test_truncate_leaves_short_text_alone() -> None:
    assert truncate("short", width=10) == "short"
    assert truncate("exactly10!", width=10) == "exactly10!"


def test_truncate_cuts_at_a_word_boundary() -> None:
    assert truncate("hello world", width=8) == "hello..."
    assert truncate("The quick brown fox", width=12, suffix=" >>") == "The quick >>"


def test_truncate_cuts_one_long_word_anywhere() -> None:
    assert truncate("abcdefghijklmnopqrstuvwxyz", width=10) == "abcdefg..."


@pytest.mark.parametrize("width", range(4, 30))
def test_truncate_never_exceeds_the_width(width: int) -> None:
    assert len(truncate("The quick brown fox jumps over the lazy dog", width)) <= width


def test_suffix_is_keyword_only() -> None:
    with pytest.raises(TypeError):
        truncate("some text here", 5, "~")  # type: ignore[call-arg]


def test_palindromes_ignore_case_spaces_and_punctuation() -> None:
    assert is_palindrome("Never odd or even") is True
    assert is_palindrome("A man, a plan, a canal: Panama!") is True
    assert is_palindrome("Python") is False
    assert is_palindrome("") is True


def test_letters_only() -> None:
    assert letters_only("R2-D2, C-3PO!") == "rdcpo"


def test_initials() -> None:
    assert initials("ada lovelace") == "A.L."
    assert initials("") == ""


def test_slugify_optionally_limits_words() -> None:
    assert slugify("Hello  Big World") == "hello-big-world"
    assert slugify("Hello Big World", max_words=2) == "hello-big"

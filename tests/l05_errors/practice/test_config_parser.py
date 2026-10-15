import pytest

from course.l05_errors.practice.config_parser.config_parser import (
    ConfigError,
    get_bool,
    get_int,
    parse_config,
    parse_line,
)


def test_parse_line_skips_blank_lines_and_comments() -> None:
    assert parse_line(1, "") is None
    assert parse_line(1, "   ") is None
    assert parse_line(1, "  # a comment") is None


def test_parse_line_splits_at_the_first_separator() -> None:
    assert parse_line(1, " url = a=b ") == ("url", "a=b")
    assert parse_line(1, "empty =") == ("empty", "")


def test_parse_line_errors_carry_the_line_number() -> None:
    with pytest.raises(ConfigError, match="line 4: expected") as caught:
        parse_line(4, "no separator")
    assert caught.value.line_number == 4
    with pytest.raises(ConfigError, match="missing key"):
        parse_line(2, "= value")


def test_parse_config_reads_settings() -> None:
    assert parse_config("a = 1\n# note\n\nb = two\n") == {"a": "1", "b": "two"}
    assert parse_config("") == {}


def test_parse_config_reports_every_bad_line_at_once() -> None:
    with pytest.raises(ExceptionGroup) as caught:
        parse_config("bad\nok = 1\n= x\nok = 2\n")
    errors = caught.value.exceptions
    assert all(isinstance(error, ConfigError) for error in errors)
    line_numbers = [error.line_number for error in errors if isinstance(error, ConfigError)]
    assert line_numbers == [1, 3, 4]
    assert "duplicate key 'ok'" in str(errors[2])


def test_get_int() -> None:
    assert get_int({"port": "8080"}, "port", 80) == 8080
    assert get_int({}, "port", 80) == 80


def test_get_int_chains_the_original_error() -> None:
    with pytest.raises(ConfigError, match="port must be a whole number") as caught:
        get_int({"port": "eighty"}, "port", 80)
    assert isinstance(caught.value.__cause__, ValueError)
    assert caught.value.line_number is None


@pytest.mark.parametrize(("text", "expected"), [("yes", True), ("ON", True), ("0", False)])
def test_get_bool_understands_common_words(text: str, expected: bool) -> None:
    assert get_bool({"debug": text}, "debug", not expected) is expected


def test_get_bool_default_and_bad_value() -> None:
    assert get_bool({}, "debug", True) is True
    with pytest.raises(ConfigError, match="yes or no"):
        get_bool({"debug": "maybe"}, "debug", False)

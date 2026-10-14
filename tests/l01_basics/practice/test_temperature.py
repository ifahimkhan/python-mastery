import pytest

from course.l01_basics.practice.temperature.temperature import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    describe_celsius,
    fahrenheit_to_celsius,
    main,
    parse_celsius,
)


def test_known_points_convert_to_fahrenheit() -> None:
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0), "Water freezes at 32 F"
    assert celsius_to_fahrenheit(100) == pytest.approx(212.0), "Water boils at 212 F"
    assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0), "-40 is the same in both"


def test_fahrenheit_round_trips_back_to_celsius() -> None:
    assert fahrenheit_to_celsius(212) == pytest.approx(100.0)
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(37.5)) == pytest.approx(37.5)


def test_kelvin_is_shifted_celsius() -> None:
    assert celsius_to_kelvin(0) == pytest.approx(273.15)
    assert celsius_to_kelvin(-273.15) == pytest.approx(0.0), "Absolute zero is 0 K"


def test_parse_celsius_accepts_numbers_with_spaces() -> None:
    assert parse_celsius(" 21.5 ") == 21.5
    assert parse_celsius("-10") == -10.0


@pytest.mark.parametrize("text", ["warm", "", "nan", "inf", "-inf", "1,5"])
def test_parse_celsius_rejects_unusable_text(text: str) -> None:
    assert parse_celsius(text) is None, f"{text!r} is not a usable temperature"


def test_describe_rounds_float_noise_away() -> None:
    assert describe_celsius(100.0) == "100.0 C = 212.0 F = 373.15 K"
    assert describe_celsius(36.6) == "36.6 C = 97.88 F = 309.75 K"


@pytest.mark.parametrize(
    ("typed", "expected"),
    [
        ("100", "100.0 C = 212.0 F = 373.15 K"),
        ("hot", "'hot' is not a usable number."),
        ("-300", "-300.0 C is below absolute zero (-273.15 C)."),
    ],
)
def test_main_prints_one_answer(
    typed: str, expected: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("builtins.input", lambda prompt: typed)
    main()
    assert capsys.readouterr().out.strip() == expected

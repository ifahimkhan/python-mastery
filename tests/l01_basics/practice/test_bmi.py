import math

import pytest

from course.l01_basics.practice.bmi.bmi import (
    bmi_category,
    calculate_bmi,
    describe_bmi,
    main,
    parse_positive_number,
)


def test_computes_bmi_from_weight_and_height() -> None:
    assert calculate_bmi(70, 1.75) == pytest.approx(22.857, abs=0.001)


@pytest.mark.parametrize(
    ("bmi", "category"),
    [
        (18.4, "Underweight"),
        (18.5, "Normal"),
        (24.9, "Normal"),
        (25.0, "Overweight"),
        (29.9, "Overweight"),
        (30.0, "Obese"),
    ],
)
def test_categories_use_upper_exclusive_limits(bmi: float, category: str) -> None:
    assert bmi_category(bmi) == category


@pytest.mark.parametrize(
    ("weight", "height"), [(70, 0), (70, -1.75), (-1, 1.75), (0, 1.75), (math.nan, 1.75)]
)
def test_rejects_impossible_values(weight: float, height: float) -> None:
    with pytest.raises(ValueError, match="must be a positive number"):
        calculate_bmi(weight, height)


def test_parse_positive_number_accepts_numbers_with_spaces() -> None:
    assert parse_positive_number(" 70 ") == 70.0
    assert parse_positive_number("1.75") == 1.75


@pytest.mark.parametrize("text", ["heavy", "", "0", "-5", "nan", "inf"])
def test_parse_positive_number_rejects_bad_text(text: str) -> None:
    assert parse_positive_number(text) is None


def test_describe_classifies_the_shown_value() -> None:
    assert describe_bmi(70, 1.75) == "Your BMI is 22.9 (Normal)"
    # 24.96 rounds to 25.0, which is Overweight: label and number must agree.
    assert describe_bmi(24.96, 1.0) == "Your BMI is 25.0 (Overweight)"


@pytest.mark.parametrize(
    ("typed", "expected"),
    [
        (["70", "1.75"], "Your BMI is 22.9 (Normal)"),
        (["heavy", "1.75"], "Please type positive numbers, e.g. 70 and 1.75."),
        (["70", "0"], "Please type positive numbers, e.g. 70 and 1.75."),
    ],
)
def test_main_prints_one_answer(
    typed: list[str],
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    answers = iter(typed)
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    main()
    assert capsys.readouterr().out.strip() == expected

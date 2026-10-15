import pytest

from course.l05_errors.practice.calculator.calculator import (
    CalculatorError,
    ParseError,
    UnknownOperatorError,
    evaluate,
    format_result,
)


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("3 + 4", 7),
        ("10 - 12", -2),
        ("6 * 7", 42),
        ("10 / 4", 2.5),
        ("2 ^ 10", 1024),
        ("1.5 + 1", 2.5),
    ],
)
def test_evaluates_every_operator(expression: str, expected: float) -> None:
    assert evaluate(expression) == pytest.approx(expected)


def test_division_by_zero_is_a_calculator_error_with_a_cause() -> None:
    with pytest.raises(CalculatorError, match="division by zero") as caught:
        evaluate("7 / 0")
    assert isinstance(caught.value.__cause__, ZeroDivisionError)


def test_bad_numbers_are_parse_errors() -> None:
    with pytest.raises(ParseError, match="not a number: 'seven'") as caught:
        evaluate("seven * 2")
    assert isinstance(caught.value.__cause__, ValueError)


@pytest.mark.parametrize("expression", ["", "1 +", "1 + 2 + 3", "12"])
def test_wrong_shape_is_a_parse_error(expression: str) -> None:
    with pytest.raises(ParseError, match="expected 'number operator number'"):
        evaluate(expression)


def test_unknown_operator_keeps_the_operator() -> None:
    with pytest.raises(UnknownOperatorError) as caught:
        evaluate("5 % 3")
    assert caught.value.operator == "%"


def test_every_error_is_a_calculator_error() -> None:
    assert issubclass(ParseError, CalculatorError)
    assert issubclass(UnknownOperatorError, CalculatorError)


@pytest.mark.parametrize(("value", "text"), [(12.0, "12"), (2.5, "2.5"), (-42.0, "-42")])
def test_format_result_drops_needless_point_zero(value: float, text: str) -> None:
    assert format_result(value) == text


@pytest.mark.parametrize("expression", ["-8 ^ 0.5", "10 ^ 999"])
def test_impossible_powers_are_calculator_errors(expression: str) -> None:
    with pytest.raises(CalculatorError, match="cannot compute"):
        evaluate(expression)

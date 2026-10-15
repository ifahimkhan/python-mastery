"""
=====================================================================
 PRACTICE 05.B - Safe calculator
=====================================================================
 GOAL   : Evaluate "number operator number" expressions and turn every
          kind of failure into a clear, specific error message.
 RUN    : uv run python -m course.l05_errors.practice.calculator.calculator
 OUTPUT :
          3 + 4      = 7
          10 / 4     = 2.5
          2 ^ 10     = 1024
          7 / 0      -> CalculatorError: division by zero
          seven * 2  -> ParseError: not a number: 'seven'
          5 % 3      -> UnknownOperatorError: unknown operator '%' (use + - * / ^)
          1 +        -> ParseError: expected 'number operator number', got '1 +'
          -6 * 7     = -42
 DESIGN : Every problem becomes a subclass of CalculatorError, so main()
          needs ONE except to report them all, while tests can check the
          exact kind. Low-level errors are chained with `from`.
 EXTEND : Allow longer expressions like "1 + 2 * 3" (respect precedence!).
=====================================================================
"""

import math

EXPECTED_PARTS = 3

EXPRESSIONS = ("3 + 4", "10 / 4", "2 ^ 10", "7 / 0", "seven * 2", "5 % 3", "1 +", "-6 * 7")


class CalculatorError(Exception):
    """Base class: anything that went wrong while calculating."""


class ParseError(CalculatorError):
    """The text is not of the form "number operator number"."""


class UnknownOperatorError(CalculatorError):
    def __init__(self, operator: str) -> None:
        self.operator = operator
        super().__init__(f"unknown operator {operator!r} (use + - * / ^)")


def parse_number(text: str) -> float:
    try:
        return float(text)
    except ValueError as error:
        raise ParseError(f"not a number: {text!r}") from error


def apply(left: float, operator: str, right: float) -> float:
    match operator:
        case "+":
            return left + right
        case "-":
            return left - right
        case "*":
            return left * right
        case "/":
            try:
                return left / right
            except ZeroDivisionError as error:
                raise CalculatorError("division by zero") from error
        case "^":
            # math.pow raises instead of returning a complex number (-8 ^ 0.5)
            # or an endless float (10 ^ 999).
            try:
                return math.pow(left, right)
            except (ValueError, OverflowError) as error:
                raise CalculatorError(f"cannot compute {left} ^ {right}") from error
        case _:
            raise UnknownOperatorError(operator)


def evaluate(expression: str) -> float:
    parts = expression.split()
    if len(parts) != EXPECTED_PARTS:
        raise ParseError(f"expected 'number operator number', got {expression!r}")
    left_text, operator, right_text = parts
    return apply(parse_number(left_text), operator, parse_number(right_text))


def format_result(value: float) -> str:
    """12.0 -> "12", 2.5 -> "2.5": no needless .0."""
    return str(int(value)) if value.is_integer() else str(value)


def main() -> None:
    for expression in EXPRESSIONS:
        try:
            result = format_result(evaluate(expression))
        except CalculatorError as error:
            print(f"{expression:<10} -> {type(error).__name__}: {error}")
        else:
            print(f"{expression:<10} = {result}")


if __name__ == "__main__":
    main()

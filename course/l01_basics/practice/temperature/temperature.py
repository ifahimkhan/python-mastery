"""
=====================================================================
 PRACTICE 01.A - Temperature converter (CLI)
=====================================================================
 GOAL   : Combine variables, numbers, operators, f-strings and input
          into a small, real program.
 RUN    : uv run python -m course.l01_basics.practice.temperature.temperature
 OUTPUT : (example session: you type 100)
          Enter a temperature in Celsius: 100
          100.0 C = 212.0 F = 373.15 K
 DESIGN : The math lives in small functions with no input or output, so
          tests can check them (see tests/l01_basics/practice/test_temperature.py).
          main() only reads input and prints results. Keep these two jobs
          separate in every program you write.
 NOTE   : Previews: `if`/`elif`/`else` (level 02), `None` and
          `try`/`except` (level 05), `import` (level 09).
          Read them like plain English for now.
 EXTEND : Add a Fahrenheit -> Celsius mode chosen by the user.
=====================================================================
"""

import math

FAHRENHEIT_RATIO = 9 / 5
FAHRENHEIT_OFFSET = 32.0
KELVIN_OFFSET = 273.15
DECIMALS = 2

# Absolute zero: nothing can be colder.
ABSOLUTE_ZERO_CELSIUS = -273.15


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * FAHRENHEIT_RATIO + FAHRENHEIT_OFFSET


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - FAHRENHEIT_OFFSET) / FAHRENHEIT_RATIO


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + KELVIN_OFFSET


def parse_celsius(text: str) -> float | None:
    """Turns user text into a Celsius value, or None if it isn't a usable number.

    isfinite() matters: float() happily accepts "nan" and "inf".
    """
    try:
        value = float(text.strip())
    except ValueError:
        return None
    if not math.isfinite(value):
        return None
    return value


def describe_celsius(celsius: float) -> str:
    # round() keeps float noise such as 0.30000000000000004 away from the user.
    fahrenheit = round(celsius_to_fahrenheit(celsius), DECIMALS)
    kelvin = round(celsius_to_kelvin(celsius), DECIMALS)
    return f"{celsius} C = {fahrenheit} F = {kelvin} K"


def main() -> None:
    text = input("Enter a temperature in Celsius: ")
    celsius = parse_celsius(text)

    # Validate at the boundary: reject text and physically impossible values.
    if celsius is None:
        print(f"{text.strip()!r} is not a usable number.")
    elif celsius < ABSOLUTE_ZERO_CELSIUS:
        print(f"{celsius} C is below absolute zero ({ABSOLUTE_ZERO_CELSIUS} C).")
    else:
        print(describe_celsius(celsius))


if __name__ == "__main__":
    main()

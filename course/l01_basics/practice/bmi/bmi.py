"""
=====================================================================
 PRACTICE 01.B - BMI calculator (CLI)
=====================================================================
 GOAL   : Read two numbers, validate them, compute and classify.
 RUN    : uv run python -m course.l01_basics.practice.bmi.bmi
 OUTPUT : (example session: you type 70 and 1.75)
          Weight in kg: 70
          Height in meters: 1.75
          Your BMI is 22.9 (Normal)
 NEW    : `raise ValueError(...)` stops the function with your message
          when an argument makes no sense: a one-line guard.
 NOTE   : Previews: `if`/`elif`/`return` (level 02), `None`, `raise`
          and `try`/`except` (level 05), `import` (level 09).
          Read them like plain English for now.
 EXTEND : Accept height in centimeters too (if the value is above 3, divide by 100).
=====================================================================
"""

import math

UNDERWEIGHT_LIMIT = 18.5
NORMAL_LIMIT = 25.0
OVERWEIGHT_LIMIT = 30.0
DECIMALS = 1


def parse_positive_number(text: str) -> float | None:
    """Turns user text into a positive, finite number, or None if it isn't one.

    isfinite() matters: float() happily accepts "nan" and "inf".
    """
    try:
        value = float(text.strip())
    except ValueError:
        return None
    if not math.isfinite(value) or value <= 0:
        return None
    return value


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """BMI = weight (kg) / height squared (m). Both must be positive and finite."""
    if not (math.isfinite(weight_kg) and weight_kg > 0):
        raise ValueError(f"Weight must be a positive number, was {weight_kg}")
    if not (math.isfinite(height_m) and height_m > 0):
        raise ValueError(f"Height must be a positive number, was {height_m}")
    return weight_kg / height_m**2


def bmi_category(bmi: float) -> str:
    # Each limit is the first value of the NEXT category (upper limit excluded).
    if bmi < UNDERWEIGHT_LIMIT:
        return "Underweight"
    if bmi < NORMAL_LIMIT:
        return "Normal"
    if bmi < OVERWEIGHT_LIMIT:
        return "Overweight"
    return "Obese"


def describe_bmi(weight_kg: float, height_m: float) -> str:
    # Classify the SAME rounded value we show, so "25.0 (Normal)" can't happen.
    bmi = round(calculate_bmi(weight_kg, height_m), DECIMALS)
    return f"Your BMI is {bmi} ({bmi_category(bmi)})"


def main() -> None:
    weight = parse_positive_number(input("Weight in kg: "))
    height = parse_positive_number(input("Height in meters: "))

    if weight is None or height is None:
        print("Please type positive numbers, e.g. 70 and 1.75.")
    else:
        print(describe_bmi(weight, height))


if __name__ == "__main__":
    main()

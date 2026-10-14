"""
=====================================================================
 LESSON 01.3 - Numbers: int, float and conversions
=====================================================================
 GOAL   : Do math with whole numbers and decimals, know the four kinds
          of division, and convert between text and numbers.
 RUN    : uv run python -m course.l01_basics.lesson03_numbers.number_types
 OUTPUT :
          7 + 2 = 9
          7 - 2 = 5
          7 * 2 = 14
          7 / 2 = 3.5
          7 // 2 = 3
          7 % 2 = 1
          7 ** 2 = 49
          divmod(7, 2) = (3, 1)
          8 / 2 = 4.0
          2 ** 100 = 1267650600228229401496703205376
          seconds in 30000 days: 2592000000
          0.1 + 0.2 = 0.30000000000000004
          round(0.1 + 0.2, 2) = 0.3
          round(3.14159, 2) = 3.14
          abs(-5) = 5
          int("42") + 1 = 43
          float("2.5") * 2 = 5.0
          int(3.99) = 3
          str(42) + "!" = 42!
          1 + 2.0 = 3.0
 NEXT   : lesson04_strings/strings.py
=====================================================================
"""

SECONDS_PER_DAY = 24 * 60 * 60


def main() -> None:
    # -- 1. CONCEPT: arithmetic ----------------------------------------
    # int = whole number (7), float = number with a decimal point (3.5).
    a, b = 7, 2
    print("7 + 2 =", a + b)
    print("7 - 2 =", a - b)
    print("7 * 2 =", a * b)
    print("7 / 2 =", a / b)  # true division: ALWAYS gives a float
    print("7 // 2 =", a // b)  # floor division: rounds DOWN to a whole number
    print("7 % 2 =", a % b)  # remainder (modulo)
    print("7 ** 2 =", a**b)  # power
    print("divmod(7, 2) =", divmod(a, b))  # (a // b, a % b) in one go

    # `/` gives a float even when the result is whole:
    print("8 / 2 =", 8 / 2)

    # -- 2. WHY: Python ints never overflow ----------------------------
    # Many languages cap whole numbers at about 2 billion or 9 quintillion.
    # Python ints grow as big as your memory allows.
    print("2 ** 100 =", 2**100)
    print("seconds in 30000 days:", 30_000 * SECONDS_PER_DAY)

    # -- 3. PITFALL: floats are approximate ----------------------------
    # Floats are stored in binary, and 0.1 has no exact binary form
    # (just like 1/3 has no exact decimal form: 0.3333...).
    print("0.1 + 0.2 =", 0.1 + 0.2)
    # So never compare floats with ==. Round for display instead
    # (or use math.isclose, level 09).
    print("round(0.1 + 0.2, 2) =", round(0.1 + 0.2, 2))
    print("round(3.14159, 2) =", round(3.14159, 2))
    print("abs(-5) =", abs(-5))  # absolute value: distance from zero

    # -- 4. CONCEPT: converting between types --------------------------
    # int(), float() and str() build a new value of that type.
    print('int("42") + 1 =', int("42") + 1)
    print('float("2.5") * 2 =', float("2.5") * 2)
    print("int(3.99) =", int(3.99))  # cuts off the decimals, does NOT round
    print('str(42) + "!" =', str(42) + "!")
    # Mixing int and float in math gives a float:
    print("1 + 2.0 =", 1 + 2.0)

    # -- 5. PITFALL: bad conversions crash -----------------------------
    #   int("abc")     # ValueError: invalid literal for int() with base 10: 'abc'
    #   int("3.5")     # ValueError: invalid literal for int() with base 10: '3.5'
    #   "Age: " + 30   # TypeError: can only concatenate str (not "int") to str
    #   10 / 0         # ZeroDivisionError: division by zero
    # Lesson 01.7 shows how to check text before converting it.

    # -- 6. TRY IT -----------------------------------------------------
    # a) How many whole weeks are in 100 days, and how many days are left? Use divmod.
    # b) Print 2 ** 0.5. What is it?
    # c) Print round(2.5) and round(3.5). Surprised? Python rounds halves to the even number.


if __name__ == "__main__":
    main()

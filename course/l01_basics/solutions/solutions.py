"""Reference answers for Level 01. Try the exercises first!

Each answer explains WHY it is written this way.
"""

SECONDS_PER_DAY = 24 * 60 * 60
CM_PER_INCH = 2.54
NUMBER_OF_VALUES = 3
DECIMAL_BASE = 10


class BasicsSolutions:
    # An f-string beats "Hello, " + name + "!": easier to read, no missed spaces.
    def greet(self, name: str) -> str:
        return f"Hello, {name}!"

    # Python ints never overflow, so no special care is needed for big values
    # (in Java or Kotlin, 30_000 days in seconds overflows an Int).
    def seconds_in_days(self, days: int) -> int:
        return days * SECONDS_PER_DAY

    # `/` is true division and always gives a float. `//` would drop the
    # decimals: (1 + 2 + 2) // 3 == 1.
    def average(self, a: int, b: int, c: int) -> float:
        return (a + b + c) / NUMBER_OF_VALUES

    # n % 2 is 0 for every even number, including negatives and zero.
    # The comparison already IS a bool: no need for "True if ... else False".
    def is_even(self, n: int) -> bool:
        return n % 2 == 0

    # [0] picks the first character; upper() returns a new, upper-case string.
    def initials(self, first_name: str, last_name: str) -> str:
        return f"{first_name[0].upper()}.{last_name[0].upper()}."

    # Python's % takes the sign of the RIGHT side: -147 % 10 == 3, not 7.
    # Removing the sign first gives the digit you actually see.
    def last_digit(self, n: int) -> int:
        return abs(n) % DECIMAL_BASE

    # A named constant explains the magic number 2.54.
    def inches_to_cm(self, inches: float) -> float:
        return inches * CM_PER_INCH

    # {age + 1} computes inside the f-string. "{age} + 1" would print "41 + 1".
    def describe(self, name: str, age: int) -> str:
        return f"{name} is {age} years old and will be {age + 1} next year."

    # , adds thousands separators and .2f always shows two decimals.
    # The $ outside the braces is plain text.
    def format_price(self, amount: float) -> str:
        return f"${amount:,.2f}"

    # A slice with step -1 walks the string from the end to the start.
    def reverse_text(self, text: str) -> str:
        return text[::-1]

"""Reference answers for Level 02. Try the exercises first!

Each answer explains WHY it is written this way.
"""

GRADE_A = 90
GRADE_B = 80
GRADE_C = 70
GRADE_D = 60
MIN_SCORE = 0
MAX_SCORE = 100
VOWELS = "aeiou"
LEAP_EVERY = 4
CENTURY = 100
LEAP_CENTURY = 400
DECIMAL_BASE = 10
SMALLEST_PRIME = 2


class ControlFlowSolutions:
    # Checking the two special cases first leaves `else` for the last one.
    def sign(self, n: int) -> str:
        if n > 0:
            return "positive"
        elif n < 0:
            return "negative"
        else:
            return "zero"

    # Reject bad input first (a "guard"), then walk the ladder from the
    # top: each elif only runs when every check above it was False, so
    # `score >= GRADE_B` already implies `score < GRADE_A`.
    def grade(self, score: int) -> str:
        if not MIN_SCORE <= score <= MAX_SCORE:
            return "invalid"
        if score >= GRADE_A:
            return "A"
        elif score >= GRADE_B:
            return "B"
        elif score >= GRADE_C:
            return "C"
        elif score >= GRADE_D:
            return "D"
        else:
            return "F"

    # lower() first, so one case covers "SAT", "Sat" and "sat".
    # `|` lists several values for one case; `_` catches everything else.
    def day_type(self, day: str) -> str:
        match day.lower():
            case "sat" | "sun":
                return "weekend"
            case "mon" | "tue" | "wed" | "thu" | "fri":
                return "weekday"
            case _:
                return "unknown"

    # A negative step counts down; stop=0 is excluded, so 0 is not printed.
    # The accumulator starts empty and grows by one piece per turn.
    def countdown(self, start: int) -> str:
        result = ""
        for n in range(start, 0, -1):
            result += f"{n} "
        return result + "Go!"

    # Start the product at 1 (not 0!), so factorial(0) == 1 falls out for free:
    # range(1, 1) is empty and the loop body never runs.
    def factorial(self, n: int) -> int:
        product = 1
        for k in range(2, n + 1):
            product *= k
        return product

    # Loop over the characters themselves; `in` checks membership in VOWELS.
    def count_vowels(self, text: str) -> int:
        count = 0
        for char in text.lower():
            if char in VOWELS:
                count += 1
        return count

    # The rule as one condition. Brackets make the grouping obvious:
    # "divisible by 4 AND (not a century OR divisible by 400)".
    # The comparison already is a bool, so return it directly.
    def is_leap_year(self, year: int) -> bool:
        return year % LEAP_EVERY == 0 and (year % CENTURY != 0 or year % LEAP_CENTURY == 0)

    # % 10 takes the last digit, // 10 drops it. abs() first, because
    # Python's % and // round towards minus infinity for negatives.
    def digit_sum(self, n: int) -> int:
        remaining = abs(n)
        total = 0
        while remaining > 0:
            total += remaining % DECIMAL_BASE
            remaining //= DECIMAL_BASE
        return total

    # Any divisor of n has a partner, and one of the two is at most sqrt(n).
    # So stop at d * d > n: much faster than trying every number below n.
    def is_prime(self, n: int) -> bool:
        if n < SMALLEST_PRIME:
            return False
        divisor = SMALLEST_PRIME
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

    # We don't know how many steps there will be, so `while` fits better than `for`.
    def collatz_steps(self, n: int) -> int:
        steps = 0
        while n != 1:
            n = n // 2 if n % 2 == 0 else 3 * n + 1
            steps += 1
        return steps

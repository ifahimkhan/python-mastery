"""
=====================================================================
 LEVEL 02 - EXERCISES (your turn!)
=====================================================================
 HOW    : Replace each `raise NotImplementedError(...)` line with your
          answer. Most answers need a few lines: an if ladder or a loop
          that builds up a result, followed by `return result`.
 CHECK  : uv run pytest -m exercise tests/l02_control_flow
          or open tests/l02_control_flow/test_exercises.py and click the
          green arrow next to the class name.
 STUCK? : Re-read the lesson in the hint. Still stuck? Peek at
          ../solutions/solutions.py, but try first!
 NOTE   : `return` hands the answer back and ends the method at once
          (level 03). It is fine to `return` from inside an if or a loop.
=====================================================================
"""


class ControlFlowExercises:
    # Hint: lesson01_if (if / elif / else)
    def sign(self, n: int) -> str:
        raise NotImplementedError('Ex 1: "positive", "negative" or "zero"')

    # Hint: lesson01_if (elif order matters) + l01_basics/lesson06_operators (chained comparisons)
    def grade(self, score: int) -> str:
        raise NotImplementedError('Ex 2: "A".."F", or "invalid" outside 0..100')

    # Hint: lesson02_match (several values with |, the _ default) + l01_basics/lesson04_strings
    def day_type(self, day: str) -> str:
        raise NotImplementedError('Ex 3: "weekend", "weekday" or "unknown"')

    # Hint: lesson03_ranges (negative step) + lesson04_for_loops (accumulator pattern)
    def countdown(self, start: int) -> str:
        raise NotImplementedError('Ex 4: "3 2 1 Go!"')

    # Hint: lesson04_for_loops (accumulator pattern; start the product at 1)
    def factorial(self, n: int) -> int:
        raise NotImplementedError("Ex 5: 1 * 2 * ... * n")

    # Hint: lesson04_for_loops (looping over a string, counting with +=)
    def count_vowels(self, text: str) -> int:
        raise NotImplementedError("Ex 6: count a, e, i, o, u")

    # Hint: lesson01_if (combining conditions) + l01_basics/lesson06_operators (and, or, not)
    def is_leap_year(self, year: int) -> bool:
        raise NotImplementedError("Ex 7: divisible by 4, except centuries, except every 400 years")

    # Hint: lesson05_while (taking a number apart with % and //) + abs()
    def digit_sum(self, n: int) -> int:
        raise NotImplementedError("Ex 8: add up the digits")

    # Hint: lesson06_break_continue (the prime test, and why divisor * divisor <= n is enough)
    def is_prime(self, n: int) -> bool:
        raise NotImplementedError("Ex 9: is n prime?")

    # Hint: lesson05_while (the Collatz loop)
    def collatz_steps(self, n: int) -> int:
        raise NotImplementedError("Ex 10: count the steps to reach 1")

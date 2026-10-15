"""The list of Level 02 exercises.

Both ``exercises/exercises.py`` (your answers) and ``solutions/solutions.py``
(reference answers) implement this Protocol, so the SAME tests check both.
Read the description of each method, then fill in its body in exercises/exercises.py.
"""

from typing import Protocol


class ControlFlowTasks(Protocol):
    def sign(self, n: int) -> str:
        """Ex 1. "positive", "negative" or "zero"."""
        ...

    def grade(self, score: int) -> str:
        """Ex 2. Letter grade for a score from 0 to 100.

        90-100 "A", 80-89 "B", 70-79 "C", 60-69 "D", 0-59 "F",
        anything outside 0..100 "invalid".
        """
        ...

    def day_type(self, day: str) -> str:
        """Ex 3. "weekend" for "sat"/"sun", "weekday" for "mon".."fri", else "unknown".

        Upper or lower case both work: day_type("SAT") == "weekend".
        """
        ...

    def countdown(self, start: int) -> str:
        """Ex 4. countdown(3) == "3 2 1 Go!"   countdown(0) == "Go!" """
        ...

    def factorial(self, n: int) -> int:
        """Ex 5. n! = 1 * 2 * ... * n, for n >= 0.  factorial(0) == 1, factorial(5) == 120"""
        ...

    def count_vowels(self, text: str) -> int:
        """Ex 6. Number of a, e, i, o, u in ``text``, upper or lower case."""
        ...

    def is_leap_year(self, year: int) -> bool:
        """Ex 7. Leap year: divisible by 4, except centuries, except every 400 years.

        2024 True, 2023 False, 1900 False (century), 2000 True (divisible by 400)
        """
        ...

    def digit_sum(self, n: int) -> int:
        """Ex 8. Sum of the digits of ``n``.  digit_sum(2026) == 10, digit_sum(-45) == 9"""
        ...

    def is_prime(self, n: int) -> bool:
        """Ex 9. True if ``n`` is a prime number. Numbers below 2 are not prime."""
        ...

    def collatz_steps(self, n: int) -> int:
        """Ex 10. Steps for ``n`` (>= 1) to reach 1: halve if even, else 3n + 1.

        collatz_steps(1) == 0, collatz_steps(6) == 8
        """
        ...

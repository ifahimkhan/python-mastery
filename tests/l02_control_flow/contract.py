"""Shared checks for Level 02.

Subclasses decide WHICH implementation is tested: the learner's exercises
or the reference solutions.
"""

from course.l02_control_flow.tasks import ControlFlowTasks


class ControlFlowContract:
    tasks: ControlFlowTasks  # set by the subclass

    def test_ex1_sign_covers_all_three_cases(self) -> None:
        assert self.tasks.sign(5) == "positive"
        assert self.tasks.sign(-5) == "negative"
        assert self.tasks.sign(0) == "zero", "Hint: zero is neither positive nor negative"

    def test_ex2_grade_uses_inclusive_lower_limits(self) -> None:
        assert self.tasks.grade(100) == "A"
        assert self.tasks.grade(90) == "A", "Hint: 90 itself is an A (>=, not >)"
        assert self.tasks.grade(89) == "B"
        assert self.tasks.grade(80) == "B"
        assert self.tasks.grade(79) == "C"
        assert self.tasks.grade(60) == "D"
        assert self.tasks.grade(59) == "F"
        assert self.tasks.grade(0) == "F", "Zero is a valid (if sad) score"

    def test_ex2_grade_rejects_scores_outside_0_to_100(self) -> None:
        assert self.tasks.grade(101) == "invalid", "Hint: check the range before the ladder"
        assert self.tasks.grade(-1) == "invalid"

    def test_ex3_day_type_ignores_case(self) -> None:
        assert self.tasks.day_type("sat") == "weekend"
        assert self.tasks.day_type("sun") == "weekend"
        assert self.tasks.day_type("SAT") == "weekend", "Hint: lower() before matching"
        assert self.tasks.day_type("Wed") == "weekday"
        assert self.tasks.day_type("fri") == "weekday"
        assert self.tasks.day_type("someday") == "unknown", "Hint: case _ catches the rest"
        assert self.tasks.day_type("") == "unknown"

    def test_ex4_countdown_ends_with_go(self) -> None:
        assert self.tasks.countdown(3) == "3 2 1 Go!", "Hint: range(start, 0, -1)"
        assert self.tasks.countdown(1) == "1 Go!"
        assert self.tasks.countdown(0) == "Go!", "Nothing to count: just Go!"

    def test_ex5_factorial_starts_from_one(self) -> None:
        assert self.tasks.factorial(0) == 1, "Hint: 0! is 1 - start the product at 1, not 0"
        assert self.tasks.factorial(1) == 1
        assert self.tasks.factorial(5) == 120
        assert self.tasks.factorial(20) == 2_432_902_008_176_640_000, "Python ints don't overflow"

    def test_ex6_count_vowels_ignores_case(self) -> None:
        assert self.tasks.count_vowels("programming") == 3
        assert self.tasks.count_vowels("AEIOU") == 5, "Hint: lower() the text first"
        assert self.tasks.count_vowels("rhythm") == 0
        assert self.tasks.count_vowels("") == 0

    def test_ex7_is_leap_year_follows_all_three_rules(self) -> None:
        assert self.tasks.is_leap_year(2024) is True, "Divisible by 4: leap"
        assert self.tasks.is_leap_year(2023) is False
        assert self.tasks.is_leap_year(1900) is False, "Hint: centuries are NOT leap years..."
        assert self.tasks.is_leap_year(2100) is False
        assert self.tasks.is_leap_year(2000) is True, "Hint: ...unless divisible by 400"
        assert self.tasks.is_leap_year(1600) is True

    def test_ex8_digit_sum_handles_zero_and_negatives(self) -> None:
        assert self.tasks.digit_sum(2026) == 10
        assert self.tasks.digit_sum(7) == 7
        assert self.tasks.digit_sum(0) == 0
        assert self.tasks.digit_sum(-45) == 9, "Hint: abs() before taking digits"

    def test_ex9_is_prime(self) -> None:
        assert self.tasks.is_prime(2) is True, "2 is the only even prime"
        assert self.tasks.is_prime(17) is True
        assert self.tasks.is_prime(21) is False
        assert self.tasks.is_prime(1) is False, "Hint: numbers below 2 are not prime"
        assert self.tasks.is_prime(0) is False
        assert self.tasks.is_prime(-7) is False
        assert self.tasks.is_prime(7919) is True

    def test_ex9_is_prime_is_fast_for_big_primes(self) -> None:
        # 1_000_000_007 is prime. Trying every divisor up to n takes too long;
        # stopping when divisor * divisor > n needs only about 31_623 tries.
        assert self.tasks.is_prime(1_000_000_007) is True, (
            "Hint: you only need divisors up to the square root (divisor * divisor <= n)"
        )

    def test_ex10_collatz_steps(self) -> None:
        assert self.tasks.collatz_steps(1) == 0, "Already at 1: zero steps"
        assert self.tasks.collatz_steps(6) == 8
        assert self.tasks.collatz_steps(27) == 111

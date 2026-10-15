"""
=====================================================================
 PRACTICE 02.A - FizzBuzz three ways
=====================================================================
 GOAL   : Solve the classic interview warm-up with an if ladder, with
          match, and by building the word, then check all three agree.
 RUN    : uv run python -m course.l02_control_flow.practice.fizzbuzz.fizzbuzz
 OUTPUT :
          1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
          all three ways agree for 1..100: True
 DESIGN : Three small functions with no printing, so tests can compare
          them. main() only loops and prints.
 NOTE   : `case (0, 0):` matches a pair of values (a tuple, level 04).
 EXTEND : Add "Bazz" for multiples of 7. Which version is easiest to change?
=====================================================================
"""

FIZZ_DIVISOR = 3
BUZZ_DIVISOR = 5
SHOW_UP_TO = 15
CHECK_UP_TO = 100


def fizzbuzz_if(n: int) -> str:
    """Way 1: an if ladder. The 'both' case must come first."""
    if n % FIZZ_DIVISOR == 0 and n % BUZZ_DIVISOR == 0:
        return "FizzBuzz"
    if n % FIZZ_DIVISOR == 0:
        return "Fizz"
    if n % BUZZ_DIVISOR == 0:
        return "Buzz"
    return str(n)


def fizzbuzz_match(n: int) -> str:
    """Way 2: match on BOTH remainders at once."""
    match (n % FIZZ_DIVISOR, n % BUZZ_DIVISOR):
        case (0, 0):
            return "FizzBuzz"
        case (0, _):
            return "Fizz"
        case (_, 0):
            return "Buzz"
        case _:
            return str(n)


def fizzbuzz_build(n: int) -> str:
    """Way 3: build the word piece by piece. No 'both' case needed at all."""
    word = ""
    if n % FIZZ_DIVISOR == 0:
        word += "Fizz"
    if n % BUZZ_DIVISOR == 0:
        word += "Buzz"
    return word or str(n)  # an empty word is falsy (lesson 01.6)


def all_ways_agree(limit: int) -> bool:
    for n in range(1, limit + 1):
        expected = fizzbuzz_if(n)
        if fizzbuzz_match(n) != expected or fizzbuzz_build(n) != expected:
            return False
    return True


def main() -> None:
    line = ""
    for n in range(1, SHOW_UP_TO + 1):
        line += fizzbuzz_build(n) + " "
    print(line.strip())
    print(f"all three ways agree for 1..{CHECK_UP_TO}: {all_ways_agree(CHECK_UP_TO)}")


if __name__ == "__main__":
    main()

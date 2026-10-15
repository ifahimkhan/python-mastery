"""
=====================================================================
 LESSON 03.6 - Recursion
=====================================================================
 GOAL   : Write functions that call themselves, with a base case that
          stops them, and know when a loop is the better choice.
 RUN    : uv run python -m course.l03_functions.lesson06_recursion.recursion
 OUTPUT :
          countdown: 3 2 1 Go!
          factorial(5) = 120
          sum_digits(2026) = 10
          binary(13) = 1101
          gcd(48, 18) = 6
          is_palindrome('racecar') = True
          is_palindrome('python') = False
          fib(10) = 55, calls needed: 177
          fib_loop(90) = 2880067194370816120
 NEXT   : lesson07_type_hints/type_hints.py
=====================================================================
"""

BINARY_BASE = 2
DECIMAL_BASE = 10

fib_calls = 0


# -- 1. CONCEPT: base case + recursive case ------------------------------
# Every recursive function needs:
#   a BASE CASE that answers directly (no more calls), and
#   a RECURSIVE CASE that calls itself on a SMALLER problem.
def countdown(n: int) -> str:
    if n == 0:  # base case
        return "Go!"
    return f"{n} " + countdown(n - 1)  # smaller problem: n - 1


# n! = n * (n - 1)!   and   0! = 1
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


# -- 2. CONCEPT: shrink the input each time ---------------------------------
# "The digit sum of 2026 is 6 plus the digit sum of 202."
def sum_digits(n: int) -> int:
    if n < DECIMAL_BASE:
        return n
    return n % DECIMAL_BASE + sum_digits(n // DECIMAL_BASE)


# Binary of 13 = binary of 6 (= 13 // 2), followed by 13 % 2.
def binary(n: int) -> str:
    if n < BINARY_BASE:
        return str(n)
    return binary(n // BINARY_BASE) + str(n % BINARY_BASE)


# Euclid (about 300 BC): gcd(a, b) == gcd(b, a % b), and gcd(a, 0) == a.
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


# -- 3. WHY: some problems ARE recursive ---------------------------------
# "A word is a palindrome if its first and last letters match and the
# middle is a palindrome." The code reads exactly like that definition.
def is_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and is_palindrome(word[1:-1])


# -- 4. PITFALL: the same work done over and over ------------------------
# fib(n) = fib(n - 1) + fib(n - 2) calls fib twice per step. The number of
# calls explodes: fib(10) needs 177 calls, fib(40) more than 300 million.
def fib(n: int) -> int:
    global fib_calls  # only to COUNT the calls for this demo (lesson 03.5)
    fib_calls += 1
    if n < BINARY_BASE:
        return n
    return fib(n - 1) + fib(n - 2)


# The loop version does each step once. (Caching results, level 07, also fixes it.)
def fib_loop(n: int) -> int:
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def main() -> None:
    print("countdown:", countdown(3))
    print("factorial(5) =", factorial(5))
    print("sum_digits(2026) =", sum_digits(2026))
    print("binary(13) =", binary(13))
    print("gcd(48, 18) =", gcd(48, 18))
    print("is_palindrome('racecar') =", is_palindrome("racecar"))
    print("is_palindrome('python') =", is_palindrome("python"))
    print(f"fib(10) = {fib(10)}, calls needed: {fib_calls}")
    print("fib_loop(90) =", fib_loop(90))

    # -- 5. PITFALL: no base case, or a base case never reached ----------
    #   factorial(-1)   # -1, -2, -3, ... never hits 0:
    #   # RecursionError: maximum recursion depth exceeded
    # Python stops at about 1000 nested calls. Deep problems (counting down
    # from 100_000) need a loop instead.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Write power(base, exp) recursively: base ** 0 == 1.
    # b) Write reverse(text) recursively: last char + reverse of the rest.
    # c) Print binary(255) and binary(256). Check with f"{255:b}".


if __name__ == "__main__":
    main()

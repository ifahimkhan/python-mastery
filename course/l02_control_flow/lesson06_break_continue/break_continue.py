"""
=====================================================================
 LESSON 02.6 - break, continue and loop else
=====================================================================
 GOAL   : Leave a loop early with break, skip a turn with continue,
          and use a loop's else block for "searched but not found".
 RUN    : uv run python -m course.l02_control_flow.lesson06_break_continue.break_continue
 OUTPUT :
          first multiple of 7 above 50: 56
          odd numbers: 1 3 5 7 9
          letters only: Python
          no 'z' in 'banana'
          first 'n' in 'banana' at index 2
          17 is prime
          21 = 3 x 7
          first pair adding to 10: 1 + 9
          smallest n with n * n > 50: 8
 NEXT   : practice/fizzbuzz/fizzbuzz.py
=====================================================================
"""

TARGET_SUM = 10
SQUARE_LIMIT = 50


def main() -> None:
    # -- 1. CONCEPT: break leaves the loop immediately ------------------
    for n in range(51, 100):
        if n % 7 == 0:
            print("first multiple of 7 above 50:", n)
            break

    # -- 2. CONCEPT: continue skips to the next turn --------------------
    print("odd numbers:", end="")
    for n in range(1, 11):
        if n % 2 == 0:
            continue  # the rest of the block is skipped for even numbers
        print("", n, end="")
    print()

    letters = ""
    for char in "P-y_t h1o2n!":
        if not char.isalpha():
            continue
        letters += char
    print("letters only:", letters)

    # -- 3. CONCEPT: for ... else ---------------------------------------
    # The else block runs only if the loop finished WITHOUT break.
    # Read it as "no break": perfect for searches.
    word = "banana"
    for char in word:
        if char == "z":
            print(f"found 'z' in {word!r}")
            break
    else:
        print(f"no 'z' in {word!r}")

    for index, char in enumerate(word):
        if char == "n":
            print(f"first 'n' in {word!r} at index {index}")
            break
    else:
        print(f"no 'n' in {word!r}")

    # A prime test: look for a divisor; if none is found, it's prime.
    for number in (17, 21):  # a tuple of two values (level 04)
        for divisor in range(2, number):
            if number % divisor == 0:
                print(f"{number} = {divisor} x {number // divisor}")
                break
        else:
            print(f"{number} is prime")
    # Faster: divisors come in pairs (3 x 7 = 7 x 3), and the smaller one is
    # never above the square root. So a while loop that stops as soon as
    # divisor * divisor > number checks far fewer numbers (31_623 instead of
    # a billion for 1_000_000_007).

    # -- 4. PITFALL: break only leaves the INNERMOST loop ---------------
    # To stop two nested loops, use a flag (or put them in a function and
    # `return`, level 03).
    found = False
    for a in range(1, TARGET_SUM):
        for b in range(a, TARGET_SUM):
            if a + b == TARGET_SUM:
                print(f"first pair adding to {TARGET_SUM}: {a} + {b}")
                found = True
                break  # leaves the `b` loop only...
        if found:
            break  # ...so leave the `a` loop too

    # -- 5. CONCEPT: while True + break ---------------------------------
    # A loop that decides to stop from the inside. Common for menus and
    # "ask until the answer is valid" input loops (see the guessing game).
    n = 0
    while True:
        n += 1
        if n * n > SQUARE_LIMIT:
            break
    print(f"smallest n with n * n > {SQUARE_LIMIT}: {n}")

    # -- 6. TRY IT -----------------------------------------------------
    # a) Find the first number above 100 that is divisible by both 6 and 8.
    # b) Print the numbers 1 to 20, skipping multiples of 3, with continue.
    # c) Use for-else to print whether "python" contains a capital letter.


if __name__ == "__main__":
    main()

"""
=====================================================================
 LESSON 02.5 - while loops
=====================================================================
 GOAL   : Repeat code while a condition holds, when you don't know in
          advance how many turns you need.
 RUN    : uv run python -m course.l02_control_flow.lesson05_while.while_loops
 OUTPUT :
          countdown: 3 2 1 liftoff!
          1000 doubled 4 times reaches 16000 (>= 10000)
          digits of 2026: 6 2 0 2
          digit sum of 2026 = 10
          collatz from 6: 6 3 10 5 16 8 4 2 1
          steps: 8
 NEXT   : lesson06_break_continue/break_continue.py
=====================================================================
"""

SAVINGS_GOAL = 10_000


def main() -> None:
    # -- 1. CONCEPT: while <condition>: --------------------------------
    # Check the condition, run the block, check again, ... until it is False.
    n = 3
    print("countdown:", end=" ")
    while n > 0:
        print(n, end=" ")
        n -= 1  # without this line the loop would never end
    print("liftoff!")

    # -- 2. WHY: while is for "until something happens" ------------------
    # Use `for` when you know the items (a range, a string). Use `while`
    # when you only know the stop condition.
    amount = 1000
    doublings = 0
    while amount < SAVINGS_GOAL:
        amount *= 2
        doublings += 1
    print(f"1000 doubled {doublings} times reaches {amount} (>= {SAVINGS_GOAL})")

    # -- 3. CONCEPT: taking a number apart with % and // ----------------
    # n % 10 is the last digit; n // 10 drops it. Repeat until nothing is left.
    number = 2026
    digit_total = 0
    print(f"digits of {number}:", end=" ")
    while number > 0:
        digit = number % 10
        print(digit, end=" ")
        digit_total += digit
        number //= 10
    print()
    print("digit sum of 2026 =", digit_total)

    # -- 4. CONCEPT: a loop whose length nobody knows -------------------
    # Collatz: halve even numbers, turn odd ones into 3n + 1. It seems to
    # always reach 1, but nobody has proved it yet!
    value = 6
    steps = 0
    print("collatz from 6:", value, end="")
    while value != 1:
        value = value // 2 if value % 2 == 0 else 3 * value + 1
        steps += 1
        print("", value, end="")
    print()
    print("steps:", steps)

    # -- 5. PITFALL: the endless loop ----------------------------------
    #   count = 0
    #   while count < 5:
    #       print(count)      # count never changes: prints 0 forever
    # Stop a runaway program with the red square in PyCharm, or Ctrl+C in
    # a terminal. In this course every test has a 5-second time limit, so
    # an endless loop in an exercise fails instead of hanging.
    # Also check the loop runs at all: `while number > 0` does nothing for 0.

    # -- 6. TRY IT -----------------------------------------------------
    # a) How many times can you halve 1_000_000 (with //) before it reaches 1?
    # b) Count the digits of 9876543210 with a while loop.
    # c) Print the Collatz steps for 27. How many are there?


if __name__ == "__main__":
    main()

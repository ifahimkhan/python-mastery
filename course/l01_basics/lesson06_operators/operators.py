"""
=====================================================================
 LESSON 01.6 - Operators
=====================================================================
 GOAL   : Compare values, combine conditions with and/or/not, update
          variables with +=, and avoid the classic % and == traps.
 RUN    : uv run python -m course.l01_basics.lesson06_operators.operators
 OUTPUT :
          5 == 5.0: True  3 != 4: True  3 > 2: True
          'apple' < 'banana': True
          0 < 7 < 10: True
          sunny and warm: False  sunny or warm: True
          not sunny: False
          or picks the first truthy value: guest
          bool(0) = False bool(42) = True
          bool('') = False bool('hi') = True
          count = 15
          count = 30
          count = 10
          2 + 3 * 4 = 14  (2 + 3) * 4 = 20
          2 ** 3 ** 2 = 512
          -7 // 2 = -4
          -7 % 2 = 1
          -147 % 10 = 3
          abs(-147) % 10 = 7
          -4 % 2 == 0: True
          a == b: True  a is b: False
 NEXT   : lesson07_input/user_input.py
=====================================================================
"""


def main() -> None:
    # -- 1. CONCEPT: comparisons give True or False ---------------------
    # True and False are the two values of type bool.
    three, five = 3, 5
    print("5 == 5.0:", five == 5.0, " 3 != 4:", three != 4, " 3 > 2:", three > 2)
    # Strings compare letter by letter, like a dictionary (A-Z before a-z).
    print("'apple' < 'banana':", "apple" < "banana")
    # Comparisons can be chained, just like in math:
    temperature = 7
    print("0 < 7 < 10:", 0 < temperature < 10)

    # -- 2. CONCEPT: and, or, not ---------------------------------------
    is_sunny = True
    is_warm = False
    print("sunny and warm:", is_sunny and is_warm, " sunny or warm:", is_sunny or is_warm)
    print("not sunny:", not is_sunny)
    # `and` / `or` stop as soon as the answer is known (short-circuit), and
    # they return one of the VALUES, not always True/False:
    username = ""
    print("or picks the first truthy value:", username or "guest")

    # -- 3. CONCEPT: truthiness -----------------------------------------
    # Every value counts as true or false. "Empty" things are false:
    # 0, 0.0, "", None and empty collections. Everything else is true.
    print("bool(0) =", bool(0), "bool(42) =", bool(42))
    print("bool('') =", bool(""), "bool('hi') =", bool("hi"))

    # -- 4. CONCEPT: augmented assignment -------------------------------
    # x += 5 is short for x = x + 5. Python has no ++ or --.
    count = 10
    count += 5
    print("count =", count)
    count *= 2
    print("count =", count)
    count //= 3
    print("count =", count)

    # -- 5. CONCEPT: precedence -----------------------------------------
    # ** first, then * / // %, then + -, then comparisons, then not, and, or.
    print("2 + 3 * 4 =", 2 + 3 * 4, " (2 + 3) * 4 =", (2 + 3) * 4)
    print("2 ** 3 ** 2 =", 2**3**2)  # ** groups from the RIGHT: 2 ** 9
    # When in doubt, add brackets. They cost nothing and help the reader.

    # -- 6. PITFALL: // and % with negative numbers ---------------------
    # // rounds DOWN (towards minus infinity), not towards zero.
    # % takes the sign of the RIGHT side, so it is never negative here.
    print("-7 // 2 =", -7 // 2)
    print("-7 % 2 =", -7 % 2)
    print("-147 % 10 =", -147 % 10)  # NOT 7! (Java and Kotlin would say -7)
    print("abs(-147) % 10 =", abs(-147) % 10)  # take the sign off first
    # Good news: n % 2 == 0 works for negative even numbers too.
    print("-4 % 2 == 0:", -4 % 2 == 0)

    # -- 7. PITFALL: == versus is ---------------------------------------
    # == asks "same value?". `is` asks "the very same object in memory?".
    a = "py" * 3
    b = "".join(["py", "py", "py"])  # built a different way
    print("a == b:", a == b, " a is b:", a is b)
    # Use == to compare values. Use `is` only for `is None` (level 05).

    # -- 8. TRY IT -----------------------------------------------------
    # a) Is 2026 a leap year? (divisible by 4 and (not by 100 or by 400))
    # b) Print 17 // 5, 17 % 5, -17 // 5 and -17 % 5. Explain each one.
    # c) Print "" or "default" and "x" or "default". What does `or` return?


if __name__ == "__main__":
    main()

"""
=====================================================================
 LESSON 02.4 - for loops
=====================================================================
 GOAL   : Repeat code for every number in a range or every character
          in a string, keep a running total, and use enumerate().
 RUN    : uv run python -m course.l02_control_flow.lesson04_for_loops.for_loops
 OUTPUT :
          lap 1
          lap 2
          lap 3
          P-y-t-h-o-n-
          total of 1..10 = 55
          vowels in 'programming' = 3
          0: c
          1: a
          2: t
          1 x 3 = 3
          2 x 3 = 6
          3 x 3 = 9
          *
          **
          ***
 NEXT   : lesson05_while/while_loops.py
=====================================================================
"""

VOWELS = "aeiou"


def main() -> None:
    # -- 1. CONCEPT: for over a range ----------------------------------
    # The loop variable takes each value in turn; the indented block runs once per value.
    for lap in range(1, 4):
        print("lap", lap)

    # -- 2. CONCEPT: for over a string ---------------------------------
    # A string is a sequence of characters, so you can loop over it directly.
    for char in "Python":
        print(char, end="-")
    print()  # finish the line

    # -- 3. CONCEPT: the accumulator pattern ----------------------------
    # Start with an "empty" value, then update it inside the loop.
    total = 0
    for n in range(1, 11):
        total += n
    print("total of 1..10 =", total)

    word = "programming"
    vowel_count = 0
    for char in word:
        if char in VOWELS:
            vowel_count += 1
    print(f"vowels in {word!r} = {vowel_count}")

    # -- 4. CONCEPT: enumerate() gives position AND value --------------
    for index, char in enumerate("cat"):
        print(f"{index}: {char}")

    # -- 5. CONCEPT: an f-string inside a loop, and nested loops -------
    factor = 3
    for i in range(1, 4):
        print(f"{i} x {factor} = {i * factor}")

    # The inner loop runs completely for EACH turn of the outer loop.
    for row in range(1, 4):
        for _ in range(row):  # `_` means "I don't need this value"
            print("*", end="")
        print()

    # -- 6. WHY: loop over the thing itself, not over its indexes ------
    # In other languages you often write `for i in range(len(word))` and
    # then use word[i]. In Python, loop over the characters directly,
    # and reach for enumerate() when you also need the position.

    # -- 7. PITFALL: indentation decides what is inside the loop -------
    #   total = 0
    #   for n in range(1, 4):
    #       total += n
    #       print(total)        # inside: prints 1, 3, 6
    #   print(total)            # outside: prints 6 once
    # And changing the loop variable does not skip anything:
    #   for n in range(5):
    #       n += 10             # the next turn still starts with the next number

    # -- 8. TRY IT -----------------------------------------------------
    # a) Print the squares of 1 to 10.
    # b) Count the capital letters in "Hello World From Python" (hint: char.isupper()).
    # c) Print a 5-row triangle like the one above, but upside down.


if __name__ == "__main__":
    main()

"""
=====================================================================
 LESSON 02.1 - if, elif and else
=====================================================================
 GOAL   : Make decisions with if/elif/else, write a one-line
          conditional expression, and use truthiness in conditions.
 RUN    : uv run python -m course.l02_control_flow.lesson01_if.if_statements
 OUTPUT :
          18 C: take a jacket
          28 C: it's warm
          score 85 -> grade B
          7 is odd
          -3 is negative and odd
          Hello, guest!
          ticket price: 6
 NEXT   : lesson02_match/match_statements.py
=====================================================================
"""

WARM_LIMIT_C = 25
CHILD_AGE_LIMIT = 12
CHILD_PRICE = 6
ADULT_PRICE = 10


def main() -> None:
    # -- 1. CONCEPT: if / else -----------------------------------------
    # The colon starts a block. The block is the INDENTED lines below it
    # (4 spaces). The block runs only when the condition is True.
    temperature = 18
    if temperature >= WARM_LIMIT_C:
        print(f"{temperature} C: it's warm")
    else:
        print(f"{temperature} C: take a jacket")

    temperature = 28
    if temperature >= WARM_LIMIT_C:
        print(f"{temperature} C: it's warm")

    # -- 2. CONCEPT: elif for more than two choices ---------------------
    # Python checks from the top and runs ONLY the first block that matches.
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"  # 85 >= 90 was False, 85 >= 80 is True: stop here
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"score {score} -> grade {grade}")

    # -- 3. CONCEPT: conditional expression (one line) -----------------
    # value_if_true if condition else value_if_false
    number = 7
    parity = "even" if number % 2 == 0 else "odd"
    print(f"{number} is {parity}")

    # Conditions can be combined with and / or / not (lesson 01.6):
    number = -3
    if number < 0 and number % 2 != 0:
        print(f"{number} is negative and odd")

    # -- 4. WHY: truthiness keeps conditions short ----------------------
    # An empty string is falsy, so `if not name:` means "if name is empty".
    name = ""
    if not name:
        name = "guest"
    print(f"Hello, {name}!")

    # -- 5. PITFALL: order of elif matters ------------------------------
    # Put the most specific check first. This ladder never gives the child price:
    #   if age >= 0:          # True for everyone, so this branch always wins
    #       price = ADULT_PRICE
    #   elif age < 12:        # never reached
    #       price = CHILD_PRICE
    age = 9
    price = CHILD_PRICE if age < CHILD_AGE_LIMIT else ADULT_PRICE
    print(f"ticket price: {price}")
    # Other classic mistakes:
    #   if score = 90:      # SyntaxError: invalid syntax. Maybe you meant '==' or ':=' ...
    #   if score > 90       # SyntaxError: expected ':'
    #   if x == 1 or 2:     # always True! It means (x == 1) or (2). Write x == 1 or x == 2.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Print "teen" for ages 13 to 19 using one chained comparison.
    # b) Turn the grade ladder into a conditional expression. Is it still readable?
    # c) Set score = 80 and predict the grade before running.


if __name__ == "__main__":
    main()

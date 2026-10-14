"""
=====================================================================
 LESSON 01.7 - Reading user input
=====================================================================
 GOAL   : Read text from the keyboard with input() and turn it into
          a number without crashing on bad input.
 RUN    : Click the green arrow in PyCharm and type into the Run window, or
          uv run python -m course.l01_basics.lesson07_input.user_input
 OUTPUT : (example session: you type "Sam" and "abc")
          What is your name? Sam
          Nice to meet you, Sam!
          How old are you? abc
          'abc' is not a whole number, assuming 0.
          In 10 years you will be 10.
 NOTE   : `if`/`else` is a preview of level 02. Read it like English.
 NEXT   : practice/temperature/temperature.py
=====================================================================
"""

YEARS_AHEAD = 10


def main() -> None:
    # -- 1. CONCEPT: input() -------------------------------------------
    # input() shows the prompt, waits for Enter, and returns what was typed.
    # strip() removes accidental spaces around it.
    name = input("What is your name? ").strip()
    print(f"Nice to meet you, {name}!")

    # -- 2. WHY: input() ALWAYS returns a string ------------------------
    # Even if the user types 42, you get the text "42", not the number 42.
    #   age_text + 10     # TypeError: can only concatenate str (not "int") to str
    # Convert it with int() first.
    age_text = input("How old are you? ").strip()

    # -- 3. PITFALL: int() crashes on bad text ---------------------------
    #   int("abc")        # ValueError: invalid literal for int() with base 10: 'abc'
    # Check the text BEFORE converting. isdecimal() is True only when every
    # character is a digit 0-9 (and the text is not empty).
    # (Catching the error with try/except is the other way: level 05.)
    if age_text.isdecimal():
        age = int(age_text)
    else:
        print(f"{age_text!r} is not a whole number, assuming 0.")
        age = 0
    print(f"In {YEARS_AHEAD} years you will be {age + YEARS_AHEAD}.")

    # -- 4. TRY IT -----------------------------------------------------
    # a) Ask for two numbers and print their sum. Type "3" and "4": is it 7 or 34?
    # b) Ask for a price with decimals and print it with 2 decimals.
    #    (isdecimal() says False for "2.5", so use float() and type carefully.)
    # c) Type " 42 " with spaces. Does it still work? Why?


if __name__ == "__main__":
    main()

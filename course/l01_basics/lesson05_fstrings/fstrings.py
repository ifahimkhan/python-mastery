"""
=====================================================================
 LESSON 01.5 - f-strings and formatting
=====================================================================
 GOAL   : Build text from values with f-strings, and control how
          numbers look: decimals, thousands separators, width, padding.
 RUN    : uv run python -m course.l01_basics.lesson05_fstrings.fstrings
 OUTPUT :
          Hi, I'm Linus and I have 3 cats.
          Next year I'll have 4 cats. My name has 5 letters.
          pi to 2 decimals: 3.14
          price: $1,234.50
          big: 1_000_000
          share: 75.0%
          order: 00042
          [left      ]
          [     right]
          [  middle  ]
          [-----42-----]
          cats=3
          cats + 1=4
          {cats} is shown as 3
          name='Linus'
 NEXT   : lesson06_operators/operators.py
=====================================================================
"""

PI = 3.14159265


def main() -> None:
    # -- 1. CONCEPT: f-strings -----------------------------------------
    # Put f before the quote, then any expression inside {...}.
    name = "Linus"
    cats = 3
    print(f"Hi, I'm {name} and I have {cats} cats.")
    print(f"Next year I'll have {cats + 1} cats. My name has {len(name)} letters.")

    # -- 2. CONCEPT: format specs after a colon ------------------------
    # {value:spec} - the spec says HOW to show the value.
    price = 1234.5
    print(f"pi to 2 decimals: {PI:.2f}")  # .2f = fixed point, 2 decimals
    print(f"price: ${price:,.2f}")  # , = thousands separator
    print(f"big: {1_000_000:_}")  # _ works as a separator too
    print(f"share: {0.75:.1%}")  # % multiplies by 100 and adds the sign
    print(f"order: {42:05}")  # pad with zeros to 5 characters

    # Width and alignment: < left, > right, ^ centre (default fill: space)
    print(f"[{'left':<10}]")
    print(f"[{'right':>10}]")
    print(f"[{'middle':^10}]")
    print(f"[{42:-^12}]")  # a fill character goes before the alignment sign

    # -- 3. CONCEPT: the = debug shortcut ------------------------------
    # {expr=} prints the expression AND its value. Great for quick checks.
    print(f"{cats=}")
    print(f"{cats + 1=}")

    # -- 4. WHY: f-strings beat + ---------------------------------------
    # "Hi, " + name + ", you have " + str(cats) + " cats" needs str() and
    # careful spaces. An f-string converts values for you and reads like
    # the final text.

    # -- 5. PITFALL: forgetting the f, and literal braces --------------
    # Without the f, the braces are printed as they are:
    #   print("Hi {name}")   # prints: Hi {name}
    # Double the braces to print them:
    print(f"{{cats}} is shown as {cats}")
    # !r shows the value the way you would type it in code (with quotes).
    # Handy to spot hidden spaces or to see that "42" is text, not a number.
    print(f"name={name!r}")

    # -- 6. TRY IT -----------------------------------------------------
    # a) Print 2 / 3 with 4 decimals.
    # b) Print a receipt line: item name left-aligned in 12 characters,
    #    price right-aligned in 8 with 2 decimals.
    # c) Print f"{name=}" and f"{name.upper()=}". What do you see?


if __name__ == "__main__":
    main()

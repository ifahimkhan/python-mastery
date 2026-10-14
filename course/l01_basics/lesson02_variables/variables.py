"""
=====================================================================
 LESSON 01.2 - Variables and names
=====================================================================
 GOAL   : Store values in variables, change them, swap them, and
          follow Python's naming rules and conventions.
 RUN    : uv run python -m course.l01_basics.lesson02_variables.variables
 OUTPUT :
          city = Lisbon
          score = 10
          score = 15
          x = 1 y = 2 z = 3
          after swap: left = R right = L
          a = 0 b = 0
          speed of light: 299792458
          <class 'int'> <class 'str'>
          <class 'float'>
 NEXT   : lesson03_numbers/number_types.py
=====================================================================
"""

# A name in UPPER_SNAKE_CASE is a *constant* by convention: Python does not
# stop you from changing it, but every Python programmer reads it as "never
# change this". Constants usually live at the top of the file.
SPEED_OF_LIGHT_M_PER_S = 299_792_458  # underscores make big numbers readable


def main() -> None:
    # -- 1. CONCEPT: a variable is a name for a value ----------------
    # `=` means "make this name refer to this value". It is not "equals".
    city = "Lisbon"
    print("city =", city)

    # -- 2. CONCEPT: names can be pointed at new values ---------------
    score = 10
    print("score =", score)
    score = score + 5  # read the right side first: 10 + 5, then store it
    print("score =", score)

    # -- 3. CONCEPT: several names at once ----------------------------
    x, y, z = 1, 2, 3
    print("x =", x, "y =", y, "z =", z)

    # Swapping needs no temporary variable in Python:
    left, right = "L", "R"
    left, right = right, left
    print("after swap: left =", left, "right =", right)

    # Give one value to several names:
    a = b = 0
    print("a =", a, "b =", b)

    print("speed of light:", SPEED_OF_LIGHT_M_PER_S)

    # -- 4. WHY: values have types, names do not ----------------------
    # The VALUE knows its type. type() tells you what it is.
    # The same name may later point at a value of another type. That is
    # legal, but confusing: keep one meaning per name.
    # (`: object` tells the type checker "any value is fine here". Type hints are level 03.)
    thing: object = 42
    first_type = type(thing)
    thing = "forty-two"
    print(first_type, type(thing))
    pi = 3.14
    print(type(pi))

    # -- 5. PITFALL: naming rules -------------------------------------
    # Names use letters, digits and _, and may not start with a digit:
    #   2nd_place = "Ana"   # SyntaxError: invalid decimal literal
    #   my-score = 3        # SyntaxError: cannot assign to expression here. ...
    # Names are case sensitive: `Score` and `score` are two different names.
    # Using a name before giving it a value:
    #   print(totl)         # NameError: name 'totl' is not defined
    # Do not reuse built-in names such as list, str, input or print:
    #   print = "oops"      # now print("hi") fails: TypeError: 'str' object is not callable
    # Convention: snake_case for variables, UPPER_SNAKE_CASE for constants.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Make variables `first_name` and `birth_year` and print them.
    # b) Make three variables and rotate them: a, b, c -> b, c, a in ONE line.
    # c) Print type(True) and type(None). What do you get?


if __name__ == "__main__":
    main()

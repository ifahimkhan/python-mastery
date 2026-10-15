"""
=====================================================================
 LESSON 03.2 - Default values and keyword arguments
=====================================================================
 GOAL   : Give parameters default values, call functions with
          name=value arguments, and avoid the mutable default trap.
 RUN    : uv run python -m course.l03_functions.lesson02_defaults.defaults_and_keywords
 OUTPUT :
          Hello, Ada!
          Hi, Ada!
          Good morning, Grace!
          Box: 10 x 5 x 1
          Box: 10 x 5 x 3
          Box: 2 x 4 x 6
          Box: 10 x 2 x 1
          shared list: ['milk']
          shared list: ['milk', 'eggs']
          fresh list: ['milk']
          fresh list: ['eggs']
 NEXT   : lesson03_args_kwargs/args_kwargs.py
=====================================================================
"""


# -- 1. CONCEPT: default values -----------------------------------------
# A parameter with `= value` is optional. Parameters with defaults come
# AFTER the ones without.
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


# -- 2. CONCEPT: keyword arguments --------------------------------------
# Pass arguments by name, in any order. Great when there are several
# numbers and it's easy to mix them up.
def describe_box(length: int, width: int, height: int = 1) -> str:
    return f"Box: {length} x {width} x {height}"


# -- 3. PITFALL: a mutable default is created ONCE ----------------------
# The default list is made when `def` runs, not on every call, so every
# call without an argument shares (and changes) the SAME list.
# Lists are level 04; append() adds an item to the end.
def add_item_buggy(item: str, basket: list[str] = []) -> list[str]:  # noqa: B006 - bug on purpose
    basket.append(item)
    return basket


# The fix: default to None and create a new list inside the function.
def add_item(item: str, basket: list[str] | None = None) -> list[str]:
    if basket is None:
        basket = []
    basket.append(item)
    return basket


def main() -> None:
    print(greet("Ada"))
    print(greet("Ada", "Hi"))
    print(greet(greeting="Good morning", name="Grace"))  # by name, any order

    print(describe_box(10, 5))
    print(describe_box(10, 5, height=3))
    print(describe_box(height=6, width=4, length=2))
    # Positional first, keywords after:
    print(describe_box(10, width=2))

    print("shared list:", add_item_buggy("milk"))
    print("shared list:", add_item_buggy("eggs"))  # milk is still there!
    print("fresh list:", add_item("milk"))
    print("fresh list:", add_item("eggs"))

    # -- 4. WHY: defaults keep calls short -----------------------------
    # The common case needs no extra arguments; the rare case can still
    # change the behaviour. Keyword arguments make the rare case readable:
    # describe_box(10, 5, height=3) says more than describe_box(10, 5, 3).

    # -- 5. PITFALL: argument order rules ------------------------------
    #   describe_box(length=10, 5)      # SyntaxError: positional argument follows keyword argument
    #   describe_box(10, length=10)     # TypeError: describe_box() got multiple values for
    #                                   #            argument 'length'
    #   def f(a=1, b): ...              # SyntaxError: parameter without a default follows
    #                                   #              parameter with a default

    # -- 6. TRY IT -----------------------------------------------------
    # a) Give describe_box a default width of 1 too. Call it with one argument.
    # b) Write power(base, exponent=2). Call it as power(3) and power(2, exponent=10).
    # c) Call add_item("tea", ["milk"]). Why is this one safe?


if __name__ == "__main__":
    main()

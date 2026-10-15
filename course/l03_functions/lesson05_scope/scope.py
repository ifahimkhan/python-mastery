"""
=====================================================================
 LESSON 03.5 - Scope: where a name lives
=====================================================================
 GOAL   : Know which variable a name refers to inside a function
          (local, enclosing, global, built-in) and why changing global
          variables from functions is a bad idea.
 RUN    : uv run python -m course.l03_functions.lesson05_scope.scope
 OUTPUT :
          inside: local message
          outside: global message
          rate from inside: 0.2
          price with tax: 120.0
          inner sees: outer value
          counter after 3 calls: 3
          clicks after 2 calls: 2
          total returned: 30
 NEXT   : lesson06_recursion/recursion.py
=====================================================================
"""

# Module level = "global" scope: visible everywhere in this file.
message = "global message"
TAX_RATE = 0.2
counter = 0


# -- 1. CONCEPT: assigning inside a function makes a LOCAL name ---------
# This `message` is a brand-new local variable. The global one is untouched.
def show_local() -> None:
    message = "local message"
    print("inside:", message)


# -- 2. CONCEPT: READING a global is fine ----------------------------------
def add_tax(price: float) -> float:
    print("rate from inside:", TAX_RATE)
    return price * (1 + TAX_RATE)


# -- 3. CONCEPT: nested functions see the enclosing function's names -----
# Python looks up a name in this order (LEGB):
#   Local -> Enclosing function -> Global (module) -> Built-in (print, len, ...)
def outer() -> None:
    value = "outer value"

    def inner() -> None:
        print("inner sees:", value)

    inner()


# -- 4. CONCEPT: global and nonlocal let you REBIND outer names -----------
# Without `global`, `counter += 1` would mean "local counter = local counter + 1"
# and crash. Use this sparingly (see WHY below).
def count_call() -> None:
    global counter
    counter += 1


def make_clicker() -> int:
    clicks = 0

    def click() -> None:
        nonlocal clicks  # the `clicks` of make_clicker, not a new local one
        clicks += 1

    click()
    click()
    return clicks


# -- 5. WHY: prefer parameters and return values --------------------------
# A function that changes globals is hard to test and to reason about:
# its result depends on what ran before it. Pass values in, return
# values out, and the function explains itself.
def add_to_total(total: int, amount: int) -> int:
    return total + amount


def main() -> None:
    show_local()
    print("outside:", message)

    print("price with tax:", add_tax(100))
    outer()

    for _ in range(3):
        count_call()
    print("counter after 3 calls:", counter)
    print("clicks after 2 calls:", make_clicker())

    total = 0
    total = add_to_total(total, 10)
    total = add_to_total(total, 20)
    print("total returned:", total)

    # -- 6. PITFALL: UnboundLocalError ----------------------------------
    #   score = 0
    #   def bump() -> None:
    #       score += 1   # UnboundLocalError: cannot access local variable 'score'
    #                    # where it is not associated with a value
    # Assigning ANYWHERE in a function makes the name local in the WHOLE function.
    # Also: if/for blocks do NOT create a new scope in Python. A variable
    # created inside a loop still exists after it.

    # -- 7. TRY IT -----------------------------------------------------
    # a) Remove `global counter` and run. Read the error message.
    # b) Rewrite count_call() so it takes the count and returns the new count.
    # c) Inside main(), print(len) and print(TAX_RATE). Which scope does each come from?


if __name__ == "__main__":
    main()

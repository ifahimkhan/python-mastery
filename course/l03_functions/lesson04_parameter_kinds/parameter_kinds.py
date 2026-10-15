"""
=====================================================================
 LESSON 03.4 - Keyword-only and positional-only parameters
=====================================================================
 GOAL   : Force some arguments to be passed by name (after *) and
          others by position (before /), and read a full signature.
 RUN    : uv run python -m course.l03_functions.lesson04_parameter_kinds.parameter_kinds
 OUTPUT :
          report.txt (overwrite=False, backup=True)
          report.txt (overwrite=True, backup=False)
          clamp(150) = 100
          clamp(-5, low=0, high=10) = 0
          clamp(7, 0, 10) = 7
          a=1 b=2 c=3 d=4 rest=(5, 6) options={'e': 7}
 NEXT   : lesson05_scope/scope.py
=====================================================================
"""

DEFAULT_LOW = 0
DEFAULT_HIGH = 100


# -- 1. CONCEPT: keyword-only parameters (after a bare *) ---------------
# Everything after `*` MUST be passed by name. Perfect for True/False
# flags: save("x", True, False) is unreadable; save("x", overwrite=True) isn't.
def save(filename: str, *, overwrite: bool = False, backup: bool = True) -> str:
    return f"{filename} (overwrite={overwrite}, backup={backup})"


# -- 2. CONCEPT: positional-only parameters (before a /) ----------------
# Everything before `/` must be passed by position. The names stay
# private, so you may rename them later without breaking any caller.
# Many built-ins work this way: len(obj=[1]) fails.
def clamp(value: int, /, low: int = DEFAULT_LOW, high: int = DEFAULT_HIGH) -> int:
    if value < low:
        return low
    if value > high:
        return high
    return value


# -- 3. CONCEPT: the full order -----------------------------------------
# positional-only / normal * keyword-only, with *args and **kwargs:
def everything(a: int, /, b: int, *rest: int, d: int, **options: int) -> str:
    c = rest[0]  # the first extra positional argument
    return f"a={a} b={b} c={c} d={d} rest={rest[1:]} options={options}"


def main() -> None:
    print(save("report.txt"))
    print(save("report.txt", overwrite=True, backup=False))

    print("clamp(150) =", clamp(150))
    print("clamp(-5, low=0, high=10) =", clamp(-5, low=0, high=10))
    print("clamp(7, 0, 10) =", clamp(7, 0, 10))

    print(everything(1, 2, 3, 5, 6, d=4, e=7))

    # -- 4. WHY: the signature is a contract -------------------------
    # Keyword-only flags make every call self-explaining. Positional-only
    # names let the author change them freely. Together they make the
    # function harder to call wrongly.

    # -- 5. PITFALL: calling them the wrong way ----------------------
    #   save("report.txt", True)
    #   # TypeError: save() takes 1 positional argument but 2 were given
    #   clamp(value=5)
    #   # TypeError: clamp() got some positional-only arguments passed as keyword
    #   #            arguments: 'value'

    # -- 6. TRY IT -----------------------------------------------------
    # a) Add a keyword-only `encoding: str = "utf-8"` to save() and print it.
    # b) Call everything(1, b=2, d=4). What goes wrong, and why?
    # c) Try print(len(obj="abc")). Read the error message.


if __name__ == "__main__":
    main()

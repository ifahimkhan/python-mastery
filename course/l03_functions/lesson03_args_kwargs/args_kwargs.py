"""
=====================================================================
 LESSON 03.3 - *args and **kwargs
=====================================================================
 GOAL   : Accept any number of positional arguments with *args and
          any number of keyword arguments with **kwargs, and unpack
          values into a call with * and **.
 RUN    : uv run python -m course.l03_functions.lesson03_args_kwargs.args_kwargs
 OUTPUT :
          total() = 0
          total(5) = 5
          total(1, 2, 3, 4) = 10
          args is a tuple: (1, 2, 3)
          name = Rex
          kind = dog
          age = 3
          kwargs is a dict: {'kind': 'cat'}
          [INFO] server started (port=8080)
          [WARN] disk almost full
          unpacked: 6
          unpacked: Box 2 x 3 x 4
 NOTE   : *args collects a tuple and **kwargs collects a dict. Both are
          level 04; here you only loop over them and use len().
 NEXT   : lesson04_parameter_kinds/parameter_kinds.py
=====================================================================
"""


# -- 1. CONCEPT: *args collects extra positional arguments --------------
# The * is what matters; `args` is just the usual name. Inside, `numbers`
# is a tuple holding every positional argument (maybe none).
def total(*numbers: int) -> int:
    result = 0
    for n in numbers:
        result += n
    return result


def show_args(*args: int) -> None:
    print("args is a tuple:", args)


# -- 2. CONCEPT: **kwargs collects extra keyword arguments ---------------
# `details` is a dict: names -> values. .items() gives the pairs (level 04).
def describe_pet(name: str, **details: str | int) -> None:
    print("name =", name)
    for key, value in details.items():
        print(key, "=", value)


def show_kwargs(**kwargs: str) -> None:
    print("kwargs is a dict:", kwargs)


# -- 3. CONCEPT: mixing them --------------------------------------------
# Order in the def: normal parameters, *args, then **kwargs.
def log(level: str, *words: str, **context: int) -> None:
    line = f"[{level}]"
    for word in words:
        line += " " + word
    if context:
        line += " ("
        for key, value in context.items():
            line += f"{key}={value}"
        line += ")"
    print(line)


def box(length: int, width: int, height: int) -> str:
    return f"Box {length} x {width} x {height}"


def main() -> None:
    print("total() =", total())
    print("total(5) =", total(5))
    print("total(1, 2, 3, 4) =", total(1, 2, 3, 4))
    show_args(1, 2, 3)

    describe_pet("Rex", kind="dog", age=3)
    show_kwargs(kind="cat")

    log("INFO", "server", "started", port=8080)
    log("WARN", "disk", "almost", "full")

    # -- 4. CONCEPT: unpacking INTO a call ---------------------------
    # * spreads a sequence into positional arguments, ** spreads a dict
    # into keyword arguments. It's the mirror image of *args / **kwargs.
    values = (1, 2, 3)
    print("unpacked:", total(*values))
    sizes = {"length": 2, "width": 3, "height": 4}
    print("unpacked:", box(**sizes))

    # -- 5. WHY: flexible but less clear --------------------------------
    # print() itself uses *args: print("a", "b", "c"). Use *args when "any
    # number of the same thing" is natural (numbers to add, words to log).
    # Prefer named parameters otherwise: they document themselves and
    # catch typos.

    # -- 6. PITFALL: typos in **kwargs are silent ------------------------
    #   describe_pet("Rex", knd="dog")   # no error: "knd" is just another key
    # With a normal parameter, the same typo fails loudly:
    #   box(lenght=2, width=3, height=4)
    #   # TypeError: box() got an unexpected keyword argument 'lenght'

    # -- 7. TRY IT -----------------------------------------------------
    # a) Write longest(*words) that returns the longest word ("" if none).
    # b) Call log("DEBUG", "x", user_id=7, attempt=2). What does the line look like?
    #    Can you add ", " between the pairs?
    # c) Call total(*range(1, 11)). What does * do with a range?


if __name__ == "__main__":
    main()

"""
=====================================================================
 LESSON 05.5 - EAFP vs LBYL
=====================================================================
 GOAL   : Choose between "Look Before You Leap" (check first) and
          "Easier to Ask Forgiveness than Permission" (try, then
          handle the error), and know why Python usually prefers EAFP.
 RUN    : uv run python -m course.l05_errors.lesson05_eafp_lbyl.eafp_lbyl
 OUTPUT :
          LBYL port: 8080
          EAFP port: 8080
          LBYL '-3' -> None
          EAFP '-3' -> -3
          EAFP ' 7 ' -> 7
          EAFP '1e3' -> None
          numbers found: [3, -4, 10]
          suppress: missing key ignored, value None
 NEXT   : lesson06_exception_groups/exception_groups.py
=====================================================================
"""

from contextlib import suppress

CONFIG = {"server": {"port": 8080}}


# -- 1. CONCEPT: LBYL - check every step first ----------------------------
def port_lbyl(config: dict[str, dict[str, int]]) -> int | None:
    if "server" in config and "port" in config["server"]:
        return config["server"]["port"]
    return None


# -- 2. CONCEPT: EAFP - just do it, handle the failure --------------------
def port_eafp(config: dict[str, dict[str, int]]) -> int | None:
    try:
        return config["server"]["port"]
    except KeyError:
        return None


# -- 3. WHY: checks are easy to get wrong -----------------------------------
# isdecimal() (lesson 01.7) rejects "-3", although int("-3") is fine.
# The check and the real conversion disagree. Asking int() itself avoids that.
def parse_lbyl(text: str) -> int | None:
    return int(text) if text.isdecimal() else None


def parse_eafp(text: str) -> int | None:
    try:
        return int(text)  # int() also accepts surrounding spaces and a sign
    except ValueError:
        return None


def main() -> None:
    print("LBYL port:", port_lbyl(CONFIG))
    print("EAFP port:", port_eafp(CONFIG))

    print("LBYL '-3' ->", parse_lbyl("-3"))
    print("EAFP '-3' ->", parse_eafp("-3"))
    print("EAFP ' 7 ' ->", parse_eafp(" 7 "))
    print("EAFP '1e3' ->", parse_eafp("1e3"))

    # EAFP in a loop: keep what works, skip what doesn't.
    shopping = "3 apples, -4 pears and 10 plums"
    found: list[int] = []
    for token in shopping.split():
        try:
            found.append(int(token))
        except ValueError:
            continue
    print("numbers found:", found)

    # -- 4. CONCEPT: contextlib.suppress for "ignore this one error" -------
    # `with` is level 09; read it as "inside this block, ignore KeyError".
    value = None
    with suppress(KeyError):
        value = CONFIG["database"]["port"]
    print("suppress: missing key ignored, value", value)

    # -- 5. PITFALL: when LBYL is still right ------------------------------
    # - When failing would be expensive or half-done: check the bank
    #   balance BEFORE moving money, not after.
    # - When "missing" is a normal case, not an error: dict.get() is clearer
    #   than try/except KeyError.
    # - Keep the try block tiny. A big try can catch a KeyError from a
    #   completely different line and hide a bug.
    # And a classic LBYL race: "if the file exists, open it" can still fail
    # if another program deletes the file in between (level 09).

    # -- 6. TRY IT -----------------------------------------------------
    # a) Write average_or_none(numbers) with EAFP (what error does an empty list give?).
    # b) Rewrite port_eafp with .get() twice. Which version do you prefer?
    # c) Find the floats in "1.5 kg costs 3 euros, 0.25 tax" with EAFP and float().


if __name__ == "__main__":
    main()

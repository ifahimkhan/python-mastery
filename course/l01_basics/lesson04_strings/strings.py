r"""
=====================================================================
 LESSON 01.4 - Strings
=====================================================================
 GOAL   : Write strings, pick out characters and slices, and use the
          most common string methods.
 RUN    : uv run python -m course.l01_basics.lesson04_strings.strings
 OUTPUT :
          Tab:[	] Backslash:[\]
          raw: C:\new\table
          Line one
          Line two
          ice cream
          ha ha ha
          len = 13
          first = P last = !
          [0:6] = Python
          [7:] = Rocks!
          [::-1] = !skcoR nohtyP
          upper = PYTHON ROCKS! lower = python rocks!
          title = Ada Lovelace
          strip = [spaces]
          replace = Python is fun!
          split = ['red', 'green', 'blue']
          join = red-green-blue
          count('o') = 2 find('R') = 7
          'Rocks' in text: True
          startswith('Py'): True
          original is still: Python Rocks!
 NEXT   : lesson05_fstrings/fstrings.py
=====================================================================
"""


def main() -> None:
    # -- 1. CONCEPT: writing strings -----------------------------------
    # Escape sequences start with a backslash: \t tab, \n new line,
    # \\ backslash, \" and \' quotes (only needed when they match the outer quotes).
    print("Tab:[\t] Backslash:[\\]")
    # A raw string (r"...") treats backslashes as plain text: handy for
    # Windows paths. Without the r, \n and \t would be a new line and a tab.
    print(r"raw: C:\new\table")
    # Triple quotes keep line breaks.
    print("""Line one
Line two""")

    # + glues strings together, * repeats them.
    print("ice" + " " + "cream")
    print("ha " * 3)

    # -- 2. CONCEPT: indexing and slicing ------------------------------
    # Positions (indexes) start at 0. Negative indexes count from the end.
    #    P  y  t  h  o  n     R  o  c  k  s  !
    #    0  1  2  3  4  5  6  7  8  9 10 11 12
    #                                     -2 -1
    text = "Python Rocks!"
    print("len =", len(text))
    print("first =", text[0], "last =", text[-1])
    # text[start:stop] - start is included, stop is NOT.
    print("[0:6] =", text[0:6])
    print("[7:] =", text[7:])  # leave out stop: up to the end
    print("[::-1] =", text[::-1])  # a step of -1 walks backwards: reversed

    # -- 3. CONCEPT: common methods ------------------------------------
    print("upper =", text.upper(), "lower =", text.lower())
    print("title =", "ada lovelace".title())
    print("strip = [" + "   spaces   ".strip() + "]")
    print("replace =", text.replace("Rocks", "is fun"))
    colors = "red,green,blue"
    print("split =", colors.split(","))  # gives a list (level 04)
    print("join =", "-".join(["red", "green", "blue"]))
    print("count('o') =", text.count("o"), "find('R') =", text.find("R"))
    print("'Rocks' in text:", "Rocks" in text)
    print("startswith('Py'):", text.startswith("Py"))

    # -- 4. WHY: strings are immutable ---------------------------------
    # A string can never change. Every method above returns a NEW string.
    text.upper()  # the result is thrown away!
    print("original is still:", text)
    # To keep a result, store it: shout = text.upper()

    # -- 5. PITFALL: index out of range --------------------------------
    #   "abc"[3]        # IndexError: string index out of range
    #   ""[0]           # IndexError: string index out of range
    # Slices never crash, they just give less: "abc"[1:99] == "bc", ""[0:1] == "".
    # Strings can't be changed in place:
    #   text[0] = "J"   # TypeError: 'str' object does not support item assignment
    # Always think: "What if the string is empty?"

    # -- 6. TRY IT -----------------------------------------------------
    # a) Print the first 3 and the last 3 characters of your name.
    # b) Count how many times "o" appears in "foo boo zoo".
    # c) Is "racecar" the same as its reverse? Print the comparison.


if __name__ == "__main__":
    main()

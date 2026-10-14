"""
=====================================================================
 LESSON 01.1 - Hello, World!
=====================================================================
 GOAL   : Write and run your first program, print text in different
          ways, and know why every lesson ends with `if __name__ ...`.
 RUN    : uv run python -m course.l01_basics.lesson01_hello.hello
 OUTPUT :
          Hello, World!
          Single quotes let you use "double quotes" inside.
          one two three
          2026-10-15
          Loading... done!

          A blank line is just print() with nothing inside.
 NOTE   : `def main() -> None:` defines a function. Functions are
          level 03; for now read it as "the program starts here".
          `-> None` says "this function gives nothing back".
 NEXT   : lesson02_variables/variables.py
=====================================================================
"""


def main() -> None:
    # -- 1. CONCEPT: print() -------------------------------------------
    # print() writes text to the screen and then starts a new line.
    # Text in quotes is a *string*. Single or double quotes both work.
    print("Hello, World!")
    print('Single quotes let you use "double quotes" inside.')

    # -- 2. CONCEPT: several values, sep= and end= ---------------------
    # Give print() several values: it puts a space between them.
    print("one", "two", "three")
    # sep= changes the text between the values.
    print("2026", "10", "15", sep="-")
    # end= changes what comes after the last value (normally a new line).
    print("Loading...", end=" ")
    print("done!")

    # An empty print() prints just the new line: a blank line.
    print()
    print("A blank line is just print() with nothing inside.")

    # -- 3. WHY: comments ---------------------------------------------
    # Everything after # is a comment. Python ignores it.
    # Write comments that explain WHY, not WHAT: the code already says what.

    # -- 4. PITFALL: Python is picky -----------------------------------
    # Case matters, quotes must match, and brackets must be closed:
    #   Print("hi")    # NameError: name 'Print' is not defined. Did you mean: 'print'?
    #   print("hi')    # SyntaxError: unterminated string literal (detected at line 1)
    #   print("hi"     # SyntaxError: '(' was never closed
    # Indentation matters too. A line indented for no reason:
    #     print("hi")  # IndentationError: unexpected indent
    # Read the LAST line of an error message first: it says what went wrong.

    # -- 5. TRY IT -----------------------------------------------------
    # a) Print your name and your favourite food on one line, separated by " | ".
    # b) Print "3...2...1...Go!" using three print() calls and end=.
    # c) Remove a closing bracket, run the file, and read the error message.


# `__name__` is "__main__" only when you RUN this file. When another file
# imports it, main() does not run by itself. PyCharm shows a green arrow here.
if __name__ == "__main__":
    main()

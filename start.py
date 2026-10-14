"""Welcome screen. Run it with ``uv run python start.py`` or the "Start" run configuration.

Every lesson in this repository is a small, self-contained program with its
own ``main()``. Open any lesson file in PyCharm and click the green run arrow
next to ``if __name__ == "__main__":``, or run it from the terminal (see below).
"""

WELCOME = """\
==============================================================
  Python Mastery - learn Python from zero to asyncio
==============================================================

  1. Read ROADMAP.md and start at level 01.
  2. Open a lesson, read it top to bottom, then run it.
  3. Solve the level's exercises and check them:

       uv run pytest -m exercise tests/l01_basics

  Run a lesson from the terminal:

       uv run python -m course.l01_basics.lesson01_hello.hello

  (Module name = folder path with dots, without ".py")
=============================================================="""


def main() -> None:
    print(WELCOME)


if __name__ == "__main__":
    main()

# Python Mastery

[![Build](https://github.com/ifahimkhan/python-mastery/actions/workflows/build.yml/badge.svg)](https://github.com/ifahimkhan/python-mastery/actions/workflows/build.yml)
[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A free, hands-on course that takes you from **your first `print()`** to
**asyncio**. Every concept is a small program you can run, read and break.

- **Runnable**: every lesson has its own `main()`. Click ▶ and see the result.
- **Visible**: each lesson prints what happens and documents the exact output in its header.
- **Logical**: comments explain *why*, not just *what*, and show the common pitfall next to the fix.
- **Checked**: every level has exercises with tests that tell you when your answer is right.

## Quick start

**Requirements:** Python 3.12 or newer, [uv](https://docs.astral.sh/uv/), and
[PyCharm](https://www.jetbrains.com/pycharm/) (the free edition is fine).

```bash
git clone https://github.com/ifahimkhan/python-mastery.git
cd python-mastery
uv sync               # creates .venv and installs the tools
uv run pytest         # everything should be green
```

### Open it in PyCharm

1. **File ▸ Open**, and pick the `python-mastery` folder.
2. PyCharm finds `.venv` created by `uv sync`. If it asks, choose
   **Use existing environment** (`.venv`). Otherwise set it in
   **Settings ▸ Project ▸ Python Interpreter ▸ Add Interpreter ▸ Add Local Interpreter ▸
   uv ▸ Select existing**.
3. Check that **Settings ▸ Tools ▸ Python Integrated Tools ▸ Default test runner** is `pytest`.
4. Ready-made run configurations appear in the top-right dropdown:
   **Start**, **All tests**, **My exercises**.

## How to study

1. Follow [ROADMAP.md](ROADMAP.md) top to bottom and tick lessons off as you go.
2. Open a lesson and **predict the output before you run it**.
3. Run it with the ▶ next to `if __name__ == "__main__":`, or from the terminal:
   ```bash
   uv run python -m course.l01_basics.lesson01_hello.hello
   ```
4. Do the **TRY IT** tasks at the end of each lesson. Change the code and break it on purpose.
5. Solve the level's exercises, then check them:
   ```bash
   uv run pytest -m exercise tests/l01_basics
   ```
   In PyCharm, open `tests/l01_basics/test_exercises.py` and click ▶ next to the class.
   A red test shows a hint. Make all of them green before moving on.
6. Build the level's **practice projects**. They combine everything in the level.

## Levels

| Level | Topic | Status |
|------:|-------|:------:|
| 01 | Basics — print, variables, numbers, strings, f-strings, operators, input | 🚧 |
| 02 | Control flow — if, `match`, `range`, loops, `for`-`else` | 🚧 |
| 03 | Functions — defaults, `*args`/`**kwargs`, keyword-only, scope, recursion, type hints | 🚧 |
| 04 | Collections — lists, tuples, dicts, sets, comprehensions, copying, `collections` | 🚧 |
| 05 | None & errors — `None`, exceptions, custom exceptions, EAFP vs LBYL, `except*` | 🚧 |
| 06 | OOP — classes, properties, dunder methods, inheritance, ABCs, `Protocol`, dataclasses, enums | 🚧 |
| 07 | Functional — closures, decorators, iterators, generators, `itertools`, `functools` | 🚧 |
| 08 | Typing — generics, variance, `Protocol`, `TypedDict`, `Literal`, overloads, mypy | 🚧 |
| 09 | Files & stdlib — modules, `pathlib`, context managers, json/csv, logging, argparse | 🚧 |
| 10 | Concurrency — threads & the GIL, locks, `concurrent.futures`, multiprocessing | 🚧 |
| 11 | asyncio — `await`, `TaskGroup`, timeouts, cancellation, queues, rate limits | 🚧 |
| 12 | Advanced — descriptors, `__slots__`, metaclasses, operator overloading, DSLs | 🚧 |
| 13 | Capstones — library CLI, weather aggregator, task scheduler | 🚧 |

## Repository layout

```
course/lNN_topic/
├── README.md         theory summary + cheat sheet for the level
├── tasks.py          the list of exercises
├── lessonNN_name/    one runnable lesson per folder
├── exercises/        your answers go here
├── solutions/        reference answers (try first!)
└── practice/         mini-projects
tests/                tests for exercises, solutions and practice projects
```

| Command | What it does |
|---------|--------------|
| `uv run pytest` | Checks the reference solutions, practice projects, and that every lesson prints what its header says |
| `uv run pytest -m exercise` | Checks **your** answers in every `exercises/` folder |
| `uv run pytest -m exercise tests/l02_control_flow` | Checks your answers for one level only |
| `uv run python -m course.<level>.<lesson>.<module>` | Runs one lesson |
| `uv run python start.py` | Shows the welcome screen |
| `uv run ruff check . && uv run mypy` | Lint and type check |

## Contributing

Found a typo, an unclear explanation or a better example? Issues and pull
requests are welcome. Read [docs/CONVENTIONS.md](docs/CONVENTIONS.md) first,
so new lessons look like the existing ones.

## License

[MIT](LICENSE). Use it, share it, teach with it.

# Repository conventions

Every level looks the same, so learners always know where to find things.
Follow these rules when adding lessons.

## Level layout

```
course/lNN_topic/
├── __init__.py
├── README.md                       # theory summary + lesson list + cheat sheet
├── tasks.py                        # Protocol: one method per exercise, docstring = task
├── lessonNN_name/name.py           # one lesson per folder (each has its own main())
├── exercises/exercises.py          # class implementing the tasks, every body raises NotImplementedError
├── solutions/solutions.py          # class implementing the tasks, commented answers
└── practice/<project>/<name>.py    # runnable mini-projects with testable functions

tests/lNN_topic/
├── contract.py                     # shared tests; subclasses set `tasks`
├── test_solutions.py               # runs in a plain `uv run pytest` (keeps CI green)
├── test_exercises.py               # @pytest.mark.exercise, runs with `-m exercise`
└── practice/test_<name>.py         # tests for practice projects
```

Every folder under `course/` and `tests/` has an `__init__.py`.

Why one folder per lesson? It gives every lesson a clean run command:
`uv run python -m course.<level>.<lesson>.<module>`, and keeps lessons from
importing each other by accident.

## Lesson header

The module docstring is the header:

```python
"""
=====================================================================
 LESSON 02.3 - Title
=====================================================================
 GOAL   : One or two sentences: what the learner can do afterwards.
 RUN    : uv run python -m course.l02_control_flow.lesson03_ranges.ranges
 OUTPUT :
          exact output, line by line
 NEXT   : lesson04_loops/loops.py
=====================================================================
"""
```

- `tests/test_lesson_output.py` runs every lesson and practice project with
  `python -m` and compares stdout with the OUTPUT block. Keep the output
  **deterministic**.
- If output depends on input, time, randomness or threads, put text in
  parentheses on the OUTPUT line itself, e.g. `OUTPUT : (example session: you type 7)`.
  That opts the file out of the check. A file with no OUTPUT line fails the test.
- Header labels: GOAL, RUN, OUTPUT, NEXT, NEW, DESIGN, EXTEND, NOTE. The
  output block ends at the next one of these labels or at the `=====` ruler.
- Every lesson ends with:

  ```python
  if __name__ == "__main__":
      main()
  ```

  PyCharm shows a green run arrow next to it.
- Lessons that read files find them with `Path(__file__).parent`, never the
  working directory (PyCharm and the terminal use different ones).
- Seed randomness (`random.Random(42)`) when the output must stay checkable.
- Concurrent lessons (threads, asyncio) must print the same text on a slow CI runner:
  - Order output with signals (`Event`, `Queue`, `await`, `join`), not with
    racing sleeps. Sleep gaps that decide output order must be at least 150 ms.
  - Never print thread names, ids, raw durations or racy counts. Print
    comparisons with wide margins (at least 3x) instead, e.g. `took less than 600 ms: True`.
  - Tests inject a fake clock or a fake `sleep`, never real delays.
- Every test has a 5-second timeout (`pyproject.toml`), so a learner's endless
  loop fails instead of hanging.

## Lesson body sections

Use these numbered banners, in this order, and skip the ones that don't apply:

```python
# -- 1. CONCEPT: ... ------------------------------------------------
# -- 2. WHY ... ----------------------------------------------------
# -- 3. PITFALL: ... -----------------------------------------------
# -- 4. TRY IT -----------------------------------------------------
```

- Show, then explain: print the result so the learner **sees** it.
- Show a pitfall as commented-out code, with the exact exception text, e.g.
  `# TypeError: can only concatenate str (not "int") to str`.
- End with 2-3 "TRY IT" tasks.
- Only use features from the current or earlier levels. If you must use a
  later feature, add a short comment such as "(level 06)".

## Exercises

- 6-10 exercises per level, numbered `Ex 1`..`Ex N` in the `tasks.py` docstrings.
- `tasks.py` defines a `typing.Protocol`. `exercises.py` and `solutions.py`
  each define a class with the same methods, so the SAME tests check both.
- Exercise bodies: `raise NotImplementedError("Ex 3: short instruction")`.
- Put a `# Hint: lessonNN_x (...)` comment above each exercise. For a lesson in
  another level, prefix the level folder: `# Hint: l04_collections/lesson03_dicts (...)`.
- A hint must point to a lesson that actually teaches what the exercise needs.
- Tests are named `test_exN_what_it_checks`, include edge cases (empty, zero,
  negative), and every assert has a hint message:
  `assert result == 7, "Hint: % keeps the sign of the right side in Python"`.

Contract pattern:

```python
# tests/l01_basics/contract.py
class BasicsContract:
    tasks: BasicsTasks  # set by the subclass

    def test_ex1_greets_by_name(self) -> None:
        assert self.tasks.greet("Py") == "Hello, Py!", "Hint: use an f-string"


# tests/l01_basics/test_exercises.py
@pytest.mark.exercise
class TestBasicsExercises(BasicsContract):
    tasks = BasicsExercises()
```

A plain `uv run pytest` leaves exercise tests out (see `tests/conftest.py`).
They run with `-m exercise`, or when you name the file or click its run arrow in PyCharm.

## Style

- PEP 8 via `ruff` (lint + format), 4 spaces, max 100 chars.
- Type hints everywhere from level 03 on; `mypy --strict` must pass.
- Prefer immutable data (`tuple`, `frozenset`, `@dataclass(frozen=True)`).
  No mutable default arguments, no bare `except:`, and no magic numbers in
  solutions or practice code (use UPPER_SNAKE_CASE constants).
- Keep printed text ASCII. Windows consoles garble characters like `°` and `—`.
  Unicode in comments is fine.
- Never put real secrets (passwords, API keys, tokens) in examples.

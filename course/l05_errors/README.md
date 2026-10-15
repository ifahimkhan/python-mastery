# Level 05 — None & errors

> Deal with missing values and things that go wrong: `None`, `try`/`except`, raising, custom exceptions, EAFP vs LBYL and exception groups.

## Lessons

| # | Lesson | You will learn |
|---|--------|----------------|
| 05.1 | [none_values](lesson01_none/none_values.py) | `None`, `X \| None`, `is None`, why `0` is not `None`, the `or` default trap |
| 05.2 | [exceptions](lesson02_exceptions/exceptions.py) | `try`/`except`/`else`/`finally`, `as error`, the exception hierarchy, bare `except` |
| 05.3 | [raising](lesson03_raising/raising.py) | `raise`, guard clauses, `raise ... from ...`, re-raising, `assert` |
| 05.4 | [custom_exceptions](lesson04_custom_exceptions/custom_exceptions.py) | your own exception classes, a base class per module, extra attributes |
| 05.5 | [eafp_lbyl](lesson05_eafp_lbyl/eafp_lbyl.py) | "ask forgiveness" vs "look before you leap", `contextlib.suppress` |
| 05.6 | [exception_groups](lesson06_exception_groups/exception_groups.py) | `ExceptionGroup`, `except*`, `add_note()` |

## Practice projects

| Project | Combines |
|---------|----------|
| [config_parser](practice/config_parser/config_parser.py) | custom errors with line numbers, collecting errors into a group, typed getters |
| [calculator](practice/calculator/calculator.py) | an exception hierarchy, chaining with `from`, `match` on operators |

## Exercises

1. Open [exercises/exercises.py](exercises/exercises.py).
2. Replace each `raise NotImplementedError(...)` with your answer. Read [tasks.py](tasks.py) for the exact exception types and messages.
3. Check: `uv run pytest -m exercise tests/l05_errors`. All 19 tests should pass.

## Cheat sheet

```python
def find(user_id: int) -> str | None: ...


user = find(7)
if user is None:  # `is None`, never `== None`
    ...

try:
    value = int(text)
except ValueError as error:  # catch the specific error
    value = None
else:
    ...  # only if nothing was raised
finally:
    ...  # always

if age < 0:
    raise ValueError(f"age must be >= 0, got {age}")

try:
    port = settings["port"]
except KeyError as error:
    raise ConfigError("port is missing") from error  # keep the cause


class BankError(Exception): ...  # one base per module


class InsufficientFundsError(BankError): ...


raise ExceptionGroup("invalid form", [ValueError("a"), KeyError("b")])

try:
    ...
except* ValueError as group:  # every matching except* runs
    ...
```

## Key ideas

- **`None` means "no value".** Test it with `is None`; `0`, `""` and `[]` are real values.
- **Catch narrowly.** Handle the errors you expect, in a tiny `try` block, and let the rest crash loudly.
- **Fail fast with a clear message.** A `raise` beats returning `-1` that nobody checks.
- **Chain with `from`** when you translate one error into another.
- **Give errors names and data.** Custom exceptions let callers react precisely.
- **Python prefers EAFP:** try the operation and handle the failure.

**Next:** Level 06 — OOP

# Level 03 — Functions

> Name a piece of logic and reuse it: parameters, return values, defaults, `*args`/`**kwargs`, keyword-only parameters, scope, recursion and type hints.

## Lessons

| # | Lesson | You will learn |
|---|--------|----------------|
| 03.1 | [function_basics](lesson01_basics/function_basics.py) | `def`, parameters vs arguments, `return` vs `print`, early return, returning several values, docstrings |
| 03.2 | [defaults_and_keywords](lesson02_defaults/defaults_and_keywords.py) | default values, keyword arguments, the mutable default trap |
| 03.3 | [args_kwargs](lesson03_args_kwargs/args_kwargs.py) | `*args`, `**kwargs`, unpacking with `*` and `**` in a call |
| 03.4 | [parameter_kinds](lesson04_parameter_kinds/parameter_kinds.py) | keyword-only (`*`), positional-only (`/`), the full parameter order |
| 03.5 | [scope](lesson05_scope/scope.py) | local vs global, LEGB, `global`/`nonlocal`, `UnboundLocalError` |
| 03.6 | [recursion](lesson06_recursion/recursion.py) | base case and recursive case, Euclid, palindromes, exploding `fib`, `RecursionError` |
| 03.7 | [type_hints](lesson07_type_hints/type_hints.py) | annotations, `X \| None`, mypy, functions as values, `Callable` |

## Practice projects

| Project | Combines |
|---------|----------|
| [text_tools](practice/text_tools/text_tools.py) | small single-purpose functions, keyword-only options, reuse |
| [receipt](practice/receipt/receipt.py) | defaults, keyword-only options, `*args`, aligned formatting |
| [hanoi](practice/hanoi/hanoi.py) | recursion, passing a function as an argument |

## Exercises

1. Open [exercises/exercises.py](exercises/exercises.py).
2. Replace each `raise NotImplementedError(...)` with your answer. Keep the `def` lines as they are.
3. Check: `uv run pytest -m exercise tests/l03_functions`. All 11 tests should pass.

## Cheat sheet

```python
def area(width: float, height: float = 1.0) -> float:
    """Docstring: what the function returns."""
    return width * height


area(3)  # 3.0 (height defaults to 1.0)
area(height=2, width=3)  # keyword arguments, any order


def total(*numbers: int) -> int: ...  # numbers is a tuple


def tag(name: str, **attrs: str) -> str: ...  # attrs is a dict


total(*(1, 2, 3))  # unpack into positional arguments
tag("a", **{"href": "/"})  # unpack into keyword arguments


def save(path: str, *, overwrite: bool = False) -> None: ...  # keyword-only after *


def clamp(value: int, /, low: int = 0) -> int: ...  # positional-only before /


def add(item: str, basket: list[str] | None = None) -> list[str]:
    if basket is None:  # never use a mutable default like []
        basket = []
    basket.append(item)
    return basket


def fact(n: int) -> int:
    return 1 if n == 0 else n * fact(n - 1)  # base case + smaller problem


def apply(func: Callable[[str], str], text: str) -> str:
    return func(text)  # functions are values
```

## Key ideas

- **Return values, don't print them.** Callers can use a returned value; a printed one is gone.
- **Defaults are created once.** Use `None` as the default for lists and dicts.
- **Make flags keyword-only.** `save(path, overwrite=True)` explains itself.
- **Pass values in, return values out.** Avoid changing globals from functions.
- **Every recursion needs a base case** and a smaller problem each call.
- **Type hints are checked by tools, not at run time.** Run `uv run mypy`.

**Next:** Level 04 — Collections

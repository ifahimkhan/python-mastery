# Level 01 — Basics

> Your first Python programs: print, variables, numbers, strings, f-strings, operators and input.

## Lessons

| # | Lesson | You will learn |
|---|--------|----------------|
| 01.1 | [hello](lesson01_hello/hello.py) | `print()`, `sep=` and `end=`, comments, reading error messages, `if __name__ == "__main__"` |
| 01.2 | [variables](lesson02_variables/variables.py) | names and `=`, multiple assignment, swapping, constants, `type()`, naming rules |
| 01.3 | [number_types](lesson03_numbers/number_types.py) | `int` vs `float`, `/` `//` `%` `**`, big ints, float noise, `round()`, `int()`/`float()`/`str()` |
| 01.4 | [strings](lesson04_strings/strings.py) | escapes, raw and triple-quoted strings, indexing, slicing, common methods, immutability |
| 01.5 | [fstrings](lesson05_fstrings/fstrings.py) | f-strings, format specs (`.2f`, `,`, `%`, width, alignment), `{x=}`, `!r` |
| 01.6 | [operators](lesson06_operators/operators.py) | comparisons, chaining, `and`/`or`/`not`, truthiness, `+=`, precedence, `%` with negatives, `==` vs `is` |
| 01.7 | [user_input](lesson07_input/user_input.py) | `input()`, text vs numbers, checking text before converting it |

## Practice projects

| Project | Combines |
|---------|----------|
| [temperature](practice/temperature/temperature.py) | input, float math, constants, validation |
| [bmi](practice/bmi/bmi.py) | two inputs, guards with `raise`, classification, rounding |

## Exercises

1. Open [exercises/exercises.py](exercises/exercises.py).
2. Replace each `raise NotImplementedError(...)` with your answer.
3. Check: `uv run pytest -m exercise tests/l01_basics`. All 10 tests should pass.

## Cheat sheet

```python
MAX_TRIES = 3  # constant: UPPER_SNAKE_CASE by convention
name = "Ada"  # variable: snake_case
x, y = y, x  # swap

7 / 2  # 3.5   true division, always a float
7 // 2  # 3     floor division (rounds DOWN: -7 // 2 == -4)
7 % 2  # 1     remainder, sign of the RIGHT side (-147 % 10 == 3)
2**100  # ints never overflow
0.1 + 0.2  # 0.30000000000000004: never compare floats with ==

int("42"), float("2.5"), str(42)  # conversions
"abc"[0], "abc"[-1], "abc"[::-1]  # 'a', 'c', 'cba'

f"Hi {name}, next year {age + 1}"  # f-string
f"{price:,.2f}"  # 1,234.50
f"{0.75:.1%}"  # 75.0%
f"{x=}"  # x=42  (debug)

a == b  # same value
a is b  # same object (use only for `is None`)
input("Age? ")  # ALWAYS returns a str
```

## Key ideas

- **Names point at values.** Values have types; names don't.
- **`/` always gives a float.** Use `//` for whole-number division and mind negatives.
- **Floats are approximate.** Round for display; don't compare them with `==`.
- **Strings are immutable.** Their methods return new strings.
- **Prefer f-strings** over `+` for building text.
- **`input()` returns text.** Check or convert it where it enters the program.

**Next:** Level 02 — Control flow

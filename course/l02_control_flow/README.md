# Level 02 — Control flow

> Make decisions and repeat work: `if`, `match`, `range`, `for`, `while`, `break`, `continue` and loop `else`.

## Lessons

| # | Lesson | You will learn |
|---|--------|----------------|
| 02.1 | [if_statements](lesson01_if/if_statements.py) | `if`/`elif`/`else`, blocks and indentation, conditional expressions, truthiness in conditions |
| 02.2 | [match_statements](lesson02_match/match_statements.py) | `match`/`case`, several values with `\|`, the `_` default, guards, capture vs compare |
| 02.3 | [ranges](lesson03_ranges/ranges.py) | `range(start, stop, step)`, counting down, `len` and `in` on ranges, off-by-one |
| 02.4 | [for_loops](lesson04_for_loops/for_loops.py) | looping over ranges and strings, the accumulator pattern, `enumerate()`, nested loops |
| 02.5 | [while_loops](lesson05_while/while_loops.py) | `while`, loops of unknown length, taking numbers apart with `%` and `//`, endless loops |
| 02.6 | [break_continue](lesson06_break_continue/break_continue.py) | `break`, `continue`, `for`-`else`, leaving nested loops, `while True` |

## Practice projects

| Project | Combines |
|---------|----------|
| [fizzbuzz](practice/fizzbuzz/fizzbuzz.py) | the same problem solved with `if`, `match` and string building |
| [times_table](practice/times_table/times_table.py) | nested loops, f-string widths and alignment |
| [guessing](practice/guessing/guessing.py) | `while True`, `continue`, input validation, random numbers |

## Exercises

1. Open [exercises/exercises.py](exercises/exercises.py).
2. Replace each `raise NotImplementedError(...)` with your answer.
3. Check: `uv run pytest -m exercise tests/l02_control_flow`. All 12 tests should pass.

## Cheat sheet

```python
if score >= 90:
    grade = "A"
elif score >= 80:  # only checked if the line above was False
    grade = "B"
else:
    grade = "F"

label = "even" if n % 2 == 0 else "odd"  # conditional expression

match day.lower():
    case "sat" | "sun":
        kind = "weekend"
    case code if code.startswith("x"):  # guard
        kind = "special"
    case _:  # default
        kind = "weekday"

range(5)  # 0 1 2 3 4         stop is excluded
range(1, 101)  # 1 .. 100
range(5, 0, -1)  # 5 4 3 2 1     count down with a negative step

for char in "abc":
    ...
for i, char in enumerate("abc"):
    ...  # 0 a, 1 b, 2 c

while n > 0:
    n //= 10

for d in range(2, n):
    if n % d == 0:
        break  # leave the loop
else:
    print("prime")  # runs only if the loop did NOT break
```

## Key ideas

- **Indentation is the block.** Four spaces decide what is inside an `if` or a loop.
- **The first matching branch wins.** Put the most specific `elif`/`case` first.
- **`for` when you know the items, `while` when you only know when to stop.**
- **Loop over the thing itself.** Use `enumerate()` when you need positions too.
- **Every `while` loop needs something that changes its condition.**
- **Loop `else` means "no break".** It is perfect for searches.

**Next:** Level 03 — Functions

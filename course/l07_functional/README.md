# Level 07 — Functional

> Treat functions as values: lambdas, closures and decorators. Then produce values lazily with iterators and generators, and use the `itertools` and `functools` toolboxes.

## Lessons

| # | Lesson | You will learn |
|---|--------|----------------|
| 07.1 | [higher_order](lesson01_higher_order/higher_order.py) | `lambda`, `key=` functions, `map`/`filter` vs comprehensions, functions that return functions |
| 07.2 | [closures](lesson02_closures/closures.py) | captured variables, `nonlocal` state, the late-binding trap in loops |
| 07.3 | [decorators](lesson03_decorators/decorators.py) | wrapping functions, `functools.wraps`, decorators with arguments, stacking |
| 07.4 | [iterators](lesson04_iterators/iterators.py) | `iter`/`next`/`StopIteration`, iterable vs iterator, `__iter__`/`__next__`, exhaustion |
| 07.5 | [generators](lesson05_generators/generators.py) | `yield`, lazy pipelines, `yield from`, endless generators, generator expressions |
| 07.6 | [itertools_tour](lesson06_itertools/itertools_tour.py) | `islice`, `chain`, `pairwise`, `batched`, `accumulate`, `groupby`, combinatorics |
| 07.7 | [functools_tour](lesson07_functools/functools_tour.py) | `@cache`, `@lru_cache`, `partial`, `reduce`, `@cached_property` |

## Practice projects

| Project | Combines |
|---------|----------|
| [log_pipeline](practice/log_pipeline/log_pipeline.py) | generator stages, a frozen dataclass, `IntEnum` levels, `Counter`, `groupby` |
| [command_registry](practice/command_registry/command_registry.py) | decorators with arguments, stacked decorators, closures, `functools.wraps` and docstrings |

## Exercises

1. Open [exercises/exercises.py](exercises/exercises.py).
2. Replace each `raise NotImplementedError(...)` with your answer. Many answers return a function or an iterator; read [tasks.py](tasks.py) for the details.
3. Check: `uv run pytest -m exercise tests/l07_functional`. All 19 tests should pass.

## Cheat sheet

```python
sorted(people, key=lambda person: person.age)


def make_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count  # rebinding a captured name
        count += 1
        return count

    return counter


def log_calls(func):  # see lesson 07.3 for the typed version
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)

    return wrapper


def naturals() -> Iterator[int]:
    n = 1
    while True:
        yield n  # pause here until the next next()
        n += 1


list(itertools.islice(naturals(), 5))  # [1, 2, 3, 4, 5]
sum(n * n for n in range(10))  # generator expression
itertools.accumulate([3, 1, 4], max)  # 3, 3, 4


@functools.cache
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)


square = functools.partial(pow, exp=2)
```

## Key ideas

- **Functions are values.** Pass them in, return them, store them in dicts.
- **A closure remembers.** Use `nonlocal` to rebind captured names; in loops, capture values, not the loop variable.
- **Decorators add behaviour around a function** without touching its body. Always use `functools.wraps`.
- **Iterators are one-shot.** An iterable (a list, a range) gives you a fresh iterator each time.
- **Generators are lazy.** They compute one item when asked, so pipelines and endless streams cost almost no memory.
- **Reach for `itertools` and `functools`** before writing index loops or your own cache.

**Next:** Level 08 — Typing

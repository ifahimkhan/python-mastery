# Level 04 — Collections

> Hold many values at once: lists, tuples, dicts and sets, comprehensions to build them, copies that don't surprise you, and the `collections` module.

## Lessons

| # | Lesson | You will learn |
|---|--------|----------------|
| 04.1 | [lists](lesson01_lists/lists.py) | indexing and slicing, `append`/`insert`/`extend`/`remove`/`pop`, `sorted` vs `sort`, `key=` |
| 04.2 | [tuples](lesson02_tuples/tuples.py) | immutable records, unpacking, `*rest`, tuples as dict keys |
| 04.3 | [dicts](lesson03_dicts/dicts.py) | lookups, `get`, `in`, `items()`, `\|` merge, counting and grouping |
| 04.4 | [sets](lesson04_sets/sets.py) | uniqueness, fast `in`, union/intersection/difference, `frozenset` |
| 04.5 | [comprehensions](lesson05_comprehensions/comprehensions.py) | list/dict/set comprehensions, filters, nested `for`, `sum`/`any`/`all` |
| 04.6 | [copying](lesson06_copying/copying.py) | `=` never copies, shallow vs deep copies, the `[[...]] * n` trap, not changing arguments |
| 04.7 | [collections_module](lesson07_collections_module/collections_module.py) | `Counter`, `defaultdict`, `deque`, `NamedTuple` |

## Practice projects

| Project | Combines |
|---------|----------|
| [word_stats](practice/word_stats/word_stats.py) | comprehensions, sets, `Counter`, sorting with `key=`, a text bar chart |
| [gradebook](practice/gradebook/gradebook.py) | dict of lists, copies instead of changes, stable sorting, `Counter` |
| [inventory](practice/inventory/inventory.py) | `NamedTuple` records, `frozenset` tags, `_replace` for immutable updates |

## Exercises

1. Open [exercises/exercises.py](exercises/exercises.py).
2. Replace each `raise NotImplementedError(...)` with your answer. Never change the list or dict you receive.
3. Check: `uv run pytest -m exercise tests/l04_collections`. All 13 tests should pass.

## Cheat sheet

```python
nums = [3, 1, 2]
nums.append(4)
nums.pop()  # 4
sorted(nums)  # new list [1, 2, 3]; nums.sort() sorts in place, returns None
sorted(words, key=len, reverse=True)

point = (3, 4)
x, y = point
first, *rest = [1, 2, 3]

ages = {"Ada": 36}
ages.get("Bob", 0)  # 0, no KeyError
for name, age in ages.items():
    ...
ages | {"Bob": 41}  # merged copy

{1, 2} | {2, 3}  # {1, 2, 3}
{1, 2} & {2, 3}  # {2}
{1, 2} - {2, 3}  # {1}
set()  # empty set ({} is an empty dict!)

[n * n for n in nums if n % 2 == 0]
{w: len(w) for w in words}
sum(n * n for n in nums)

copy = nums.copy()  # shallow
grid = [[0] * 3 for _ in range(3)]  # NOT [[0] * 3] * 3

Counter("banana").most_common(1)  # [('a', 3)]
groups = defaultdict(list)
deque(maxlen=3)
```

## Key ideas

- **Pick the container by the question you ask.** In order → list. Fixed parts → tuple. Lookup by key → dict. "Is it there?" / unique → set.
- **`sorted()` returns a new list; `.sort()` returns `None`.** The same goes for `append`, `extend`, `remove`.
- **`=` never copies.** Copy on purpose, and use `deepcopy` for nested data.
- **Don't change what you were given.** Return a new list or dict instead.
- **Use the standard library.** `Counter`, `defaultdict` and `deque` replace a lot of hand-written loops.

**Next:** Level 05 — None & errors

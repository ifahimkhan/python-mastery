# Level 08 — Typing

> Let mypy find bugs before your users do: narrowing, generics, variance, Protocols, `TypedDict`, `Literal`, overloads and typed decorators.

Run `uv run mypy` often in this level. Most lessons show mypy's exact error messages in comments: un-comment them and see for yourself.

## Lessons

| # | Lesson | You will learn |
|---|--------|----------------|
| 08.1 | [type_basics](lesson01_type_basics/type_basics.py) | what mypy checks, narrowing with `is None`/`isinstance`, `object` vs `Any`, `type` aliases, `cast` |
| 08.2 | [generics](lesson02_generics/generics.py) | `def f[T]`, `class Box[T]`, several type parameters, constraints and bounds |
| 08.3 | [variance](lesson03_variance/variance.py) | why `list` is invariant, `Sequence`/`Mapping` are covariant, callable parameters are contravariant |
| 08.4 | [protocols](lesson04_protocols/protocols.py) | generic Protocols, a `SupportsLessThan` bound, `@runtime_checkable`, `__call__` Protocols |
| 08.5 | [typeddict_literal](lesson05_typeddict_literal/typeddict_literal.py) | `TypedDict` + `NotRequired`, `Literal`, `Final`, `NamedTuple`, which to choose |
| 08.6 | [overloads](lesson06_overloads/overloads.py) | `@overload`, `TypeGuard`, exhaustive `match` with `assert_never` |
| 08.7 | [callables](lesson07_callables/callables.py) | `Callable`, `ParamSpec` decorators, `Concatenate`, why `Callable[..., R]` hides bugs |

## Practice projects

| Project | Combines |
|---------|----------|
| [result_type](practice/result_type/result_type.py) | generic frozen dataclasses, a generic type alias, `match`, narrowing with `isinstance` |
| [event_bus](practice/event_bus/event_bus.py) | `type[E]` linked to `Callable[[E], None]`, one well-contained `Any`, `ExceptionGroup` |

## Exercises

1. Open [exercises/exercises.py](exercises/exercises.py).
2. Replace each `raise NotImplementedError(...)` with your answer. The signatures are already typed. Read [tasks.py](tasks.py) for the details.
3. Check both behaviour and types:
   - `uv run pytest -m exercise tests/l08_typing`. All 25 tests should pass.
   - `uv run mypy`. No errors, without `Any` or `# type: ignore`.

## Cheat sheet

```python
type UserId = int  # alias
type Json = dict[str, Json] | list[Json] | str | int | float | bool | None


def first[T](items: Sequence[T]) -> T: ...  # generic function


class Box[T]:  # generic class
    def __init__(self, content: T) -> None:
        self.content = content


def biggest[T: (int, float)](a: T, b: T) -> T: ...  # constrained
def by_name[T: HasName](things: Iterable[T]) -> list[T]: ...  # bounded


def total(numbers: Sequence[float]) -> float: ...  # accepts list[int] too


class Movie(TypedDict):
    title: str
    year: NotRequired[int]


def open_file(mode: Literal["r", "w"]) -> None: ...


@overload
def parse(text: str, as_float: Literal[True]) -> float: ...
@overload
def parse(text: str, as_float: Literal[False] = ...) -> int: ...
def parse(text: str, as_float: bool = False) -> int | float: ...


def is_str_list(values: list[object]) -> TypeGuard[list[str]]: ...


def logged[**P, R](func: Callable[P, R]) -> Callable[P, R]: ...  # keeps the signature


match status:
    case "ok":
        ...
    case _:
        assert_never(status)  # mypy error if a case is missing
```

## Key ideas

- **Hints are checked by tools, not at runtime.** Validate data from outside (files, users, APIs) yourself.
- **Narrow, don't cast.** `if x is None`, `isinstance` and `TypeGuard` teach mypy; `cast` and `Any` just silence it.
- **Generics keep the exact type** flowing from input to output.
- **Ask for the least in parameters** (`Iterable`, `Sequence`, `Mapping`); return concrete types.
- **Make illegal states unrepresentable:** `Literal`, enums, and `assert_never` turn forgotten cases into mypy errors.
- **Type decorators with `ParamSpec`** so the wrapped function keeps its signature.

**Next:** Level 09 — Files & stdlib

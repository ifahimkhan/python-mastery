# Level 06 — OOP

> Bundle data with the code that uses it: classes, properties, dunder methods, inheritance, ABCs, `Protocol`, dataclasses and enums.

## Lessons

| # | Lesson | You will learn |
|---|--------|----------------|
| 06.1 | [classes](lesson01_classes/classes.py) | `class`, `__init__`, `self`, methods, instance vs class attributes, the shared-list trap |
| 06.2 | [properties](lesson02_properties/properties.py) | `@property`, setters that validate, computed read-only values, `@classmethod`, `@staticmethod` |
| 06.3 | [dunder_methods](lesson03_dunder_methods/dunder_methods.py) | `__repr__`, `__str__`, `__eq__` + `__hash__`, `NotImplemented`, `__len__`, `__contains__` |
| 06.4 | [inheritance](lesson04_inheritance/inheritance.py) | subclasses, overriding, `super()`, `isinstance`, the MRO, composition over inheritance |
| 06.5 | [abc_protocol](lesson05_abc_protocol/abc_protocol.py) | `ABC` + `@abstractmethod`, `Protocol` and duck typing, when to use which |
| 06.6 | [data_classes](lesson06_dataclasses/data_classes.py) | `@dataclass`, `field(default_factory=...)`, `frozen=True`, `__post_init__`, `replace`, `order=True` |
| 06.7 | [enums](lesson07_enums/enums.py) | `Enum`, `StrEnum`, `auto()`, lookup by name and value, `match` on members |

## Practice projects

| Project | Combines |
|---------|----------|
| [bank_account](practice/bank_account/bank_account.py) | read-only properties, a `@classmethod` constructor, a subclass that overrides one rule, frozen records, custom errors |
| [card_deck](practice/card_deck/card_deck.py) | `IntEnum`s, an ordered frozen dataclass, a container with `__len__`/`__getitem__`/`__contains__`/`__iter__`, seeded shuffling |

## Exercises

1. Open [exercises/exercises.py](exercises/exercises.py).
2. Most answers are classes: fill in each class skeleton, then make the matching `make_...` method return an object of it. Read [tasks.py](tasks.py) for exactly what each object must do.
3. Check: `uv run pytest -m exercise tests/l06_oop`. All 23 tests should pass.

## Cheat sheet

```python
class Temperature:
    unit = "C"  # class attribute: shared

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius  # instance attribute (via the setter)

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

    @classmethod
    def from_fahrenheit(cls, f: float) -> "Temperature":
        return cls((f - 32) * 5 / 9)

    def __repr__(self) -> str:
        return f"Temperature({self._celsius})"


class Manager(Employee):  # inheritance
    def __init__(self, name: str, bonus: int) -> None:
        super().__init__(name)
        self.bonus = bonus


class Shape(ABC):  # must be subclassed
    @abstractmethod
    def area(self) -> float: ...


class HasArea(Protocol):  # anything with area() fits
    def area(self) -> float: ...


@dataclass(frozen=True)
class Point:
    x: int
    y: int = 0


moved = replace(Point(1, 2), x=5)  # a new object


class Color(Enum):
    RED = 1
    GREEN = 2


Color(1) is Color.RED  # True
```

## Key ideas

- **An object owns its state.** Set every attribute in `__init__`; never share a mutable class attribute.
- **Start with plain attributes.** Switch to a `@property` when you need a check or a computed value; callers don't change.
- **Always write `__repr__`.** If you write `__eq__`, write `__hash__` from the same fields (or make the object unhashable).
- **Inherit for "is a", compose for "has a".** Keep class trees shallow.
- **ABC to share code and force methods; `Protocol` to accept anything that fits.**
- **Reach for `@dataclass(frozen=True)` first** for classes that mainly hold data.
- **Enums beat magic strings:** typos fail loudly and mypy checks your `match`.

**Next:** Level 07 — Functional

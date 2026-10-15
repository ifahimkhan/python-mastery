"""
=====================================================================
 LEVEL 06 - EXERCISES (your turn!)
=====================================================================
 HOW    : Most answers here are CLASSES. Fill in each class skeleton
          below, then replace the matching `raise NotImplementedError`
          in OopExercises with a line that builds your object, e.g.
              return Counter(start)
          Read ../tasks.py for exactly what each object must do.
 CHECK  : uv run pytest -m exercise tests/l06_oop
          or open tests/l06_oop/test_exercises.py and click the
          green arrow next to the class name.
 STUCK? : Re-read the lesson in the hint. Still stuck? Peek at
          ../solutions/solutions.py, but try first!
=====================================================================
"""

from collections.abc import Sequence
from dataclasses import dataclass

from course.l06_oop.tasks import (
    BookLike,
    CounterLike,
    EmployeeLike,
    HasArea,
    Light,
    PlaylistLike,
    Shape,
    TemperatureLike,
    VectorLike,
)


# Hint: lesson01_classes (__init__, self, methods that change state)
class Counter:
    """Ex 1. Write __init__(self, start), increment(self, step=1) and reset(self)."""


# Hint: lesson02_properties (@property, @celsius.setter, a read-only property)
class Temperature:
    """Ex 2. Write __init__, the celsius property + setter, and fahrenheit."""


# Hint: lesson03_dunder_methods (__repr__, __eq__ + __hash__, NotImplemented)
class Vector:
    """Ex 3. Write __init__, x and y, __repr__, __eq__ and __hash__."""


# Hint: lesson03_dunder_methods (__len__, __contains__, __str__)
class Playlist:
    """Ex 4. Write __init__(self, name, songs), __len__, __contains__ and __str__."""


# Hint: lesson04_inheritance (Employee and Manager, super())
class Employee:
    """Ex 5. Write __init__(self, name, salary), monthly_pay and describe."""


class Manager(Employee):
    """Ex 5. Write __init__(self, name, salary, bonus) and override monthly_pay."""


# Hint: lesson05_abc_protocol (a concrete subclass of an ABC)
class Circle(Shape):
    """Ex 6. Write __init__(self, radius) and area(). describe() comes from Shape."""


# Hint: lesson06_dataclasses (frozen=True, __post_init__, replace)
@dataclass(frozen=True)
class Book:
    """Ex 8. Add the fields title, author and year, and a __post_init__."""

    def with_year(self, year: int) -> "Book":
        raise NotImplementedError("Ex 9: a NEW Book with this year, via replace()")


class OopExercises:
    def make_counter(self, start: int) -> CounterLike:
        raise NotImplementedError("Ex 1: write class Counter, then return Counter(start)")

    def make_temperature(self, celsius: float) -> TemperatureLike:
        raise NotImplementedError("Ex 2: write class Temperature with properties")

    def make_vector(self, x: int, y: int) -> VectorLike:
        raise NotImplementedError("Ex 3: write class Vector with __repr__, __eq__, __hash__")

    def make_playlist(self, name: str, songs: Sequence[str]) -> PlaylistLike:
        raise NotImplementedError("Ex 4: write class Playlist with __len__, __contains__")

    def make_employee(self, name: str, salary: int) -> EmployeeLike:
        raise NotImplementedError("Ex 5: write class Employee")

    def make_manager(self, name: str, salary: int, bonus: int) -> EmployeeLike:
        raise NotImplementedError("Ex 5: write class Manager(Employee)")

    def make_circle(self, radius: float) -> Shape:
        raise NotImplementedError("Ex 6: write class Circle(Shape)")

    # Hint: lesson05_abc_protocol (duck typing) + l04_collections/lesson03_dicts (max with key=)
    def largest(self, shapes: Sequence[HasArea]) -> HasArea | None:
        raise NotImplementedError("Ex 7: the item with the biggest area(), or None")

    def make_book(self, title: str, author: str, year: int) -> BookLike:
        raise NotImplementedError("Ex 8: write the frozen dataclass Book")

    # Hint: lesson07_enums (look a member up by value)
    def parse_light(self, text: str) -> Light:
        raise NotImplementedError("Ex 10: Light(...) from cleaned-up text")

    # Hint: lesson07_enums (match on enum members)
    def next_light(self, light: Light) -> Light:
        raise NotImplementedError("Ex 10: RED -> GREEN -> YELLOW -> RED")

"""Reference answers for Level 06. Try the exercises first!

Each answer explains WHY it is written this way.
"""

import math
from collections.abc import Sequence
from dataclasses import dataclass, replace

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

ABSOLUTE_ZERO_C = -273.15
MONTHS_PER_YEAR = 12


# Ex 1. `start` is stored too, so reset() knows where to go back to.
# Every attribute is set in __init__, so each Counter has its own.
class Counter:
    def __init__(self, start: int) -> None:
        self.start = start
        self.value = start

    def increment(self, step: int = 1) -> None:
        self.value += step

    def reset(self) -> None:
        self.value = self.start


# Ex 2. __init__ assigns through the property, so the check runs there too.
# The value is only stored AFTER the check, so a bad value changes nothing.
class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < ABSOLUTE_ZERO_C:
            raise ValueError(f"below absolute zero: {value}")
        self._celsius = value

    # No setter: assigning raises AttributeError.
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32


# Ex 3. __eq__ and __hash__ use the SAME fields, so equal vectors hash equal.
# Returning NotImplemented for other types lets Python answer False.
# (A frozen dataclass would write all of this for you, see lesson 06.6.)
class Vector:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    # Read-only properties: a Vector used as a set item must never change.
    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __repr__(self) -> str:
        return f"Vector({self._x}, {self._y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (self._x, self._y) == (other._x, other._y)

    def __hash__(self) -> int:
        return hash((self._x, self._y))


# Ex 4. A tuple copy: later changes to the caller's list don't leak in.
# No __bool__ needed: Python falls back to __len__, and 0 is falsy.
class Playlist:
    def __init__(self, name: str, songs: Sequence[str]) -> None:
        self.name = name
        self.songs = tuple(songs)

    def __len__(self) -> int:
        return len(self.songs)

    def __contains__(self, song: object) -> bool:
        return song in self.songs

    def __str__(self) -> str:
        noun = "song" if len(self) == 1 else "songs"
        return f"{self.name} ({len(self)} {noun})"


# Ex 5. describe() calls self.monthly_pay(), so a Manager's override is used
# automatically: Manager doesn't need its own describe().
class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    def monthly_pay(self) -> float:
        return self.salary / MONTHS_PER_YEAR

    def describe(self) -> str:
        return f"{self.name} earns {self.monthly_pay():.2f} a month"


class Manager(Employee):
    def __init__(self, name: str, salary: int, bonus: int) -> None:
        super().__init__(name, salary)
        self.bonus = bonus

    def monthly_pay(self) -> float:
        return super().monthly_pay() + self.bonus


# Ex 6. Only area() is needed: describe() is inherited from Shape.
class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError(f"radius must not be negative, got {radius}")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


# Ex 8 + 9. frozen=True: no assignment after creation, and a __hash__ for free.
# replace() builds a copy with one field changed (and runs __post_init__ again).
@dataclass(frozen=True)
class Book:
    title: str
    author: str
    year: int

    def __post_init__(self) -> None:
        if not self.title:
            raise ValueError("title must not be empty")

    def with_year(self, year: int) -> "Book":
        return replace(self, year=year)


def _area_of(shape: HasArea) -> float:
    return shape.area()


class OopSolutions:
    def make_counter(self, start: int) -> CounterLike:
        return Counter(start)

    def make_temperature(self, celsius: float) -> TemperatureLike:
        return Temperature(celsius)

    def make_vector(self, x: int, y: int) -> VectorLike:
        return Vector(x, y)

    def make_playlist(self, name: str, songs: Sequence[str]) -> PlaylistLike:
        return Playlist(name, songs)

    def make_employee(self, name: str, salary: int) -> EmployeeLike:
        return Employee(name, salary)

    def make_manager(self, name: str, salary: int, bonus: int) -> EmployeeLike:
        return Manager(name, salary, bonus)

    def make_circle(self, radius: float) -> Shape:
        return Circle(radius)

    # Ex 7. Duck typing: any object with area() works. max() keeps the
    # FIRST of equal items; `default` handles the empty case.
    def largest(self, shapes: Sequence[HasArea]) -> HasArea | None:
        return max(shapes, key=_area_of, default=None)

    def make_book(self, title: str, author: str, year: int) -> BookLike:
        return Book(title, author, year)

    # Ex 10. Light(value) looks a member up by value and raises ValueError
    # for unknown text. Clean the input first.
    def parse_light(self, text: str) -> Light:
        return Light(text.strip().lower())

    # match on enum members; mypy warns if a member is ever left out.
    def next_light(self, light: Light) -> Light:
        match light:
            case Light.RED:
                return Light.GREEN
            case Light.GREEN:
                return Light.YELLOW
            case Light.YELLOW:
                return Light.RED

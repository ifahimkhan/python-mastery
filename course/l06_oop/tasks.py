"""The list of Level 06 exercises.

Both ``exercises/exercises.py`` (your answers) and ``solutions/solutions.py``
(reference answers) implement the ``OopTasks`` Protocol, so the SAME tests
check both.

In this level most answers are CLASSES. Each ``make_...`` method just builds
and returns an object of a class you write. The small Protocols below say
what that object must be able to do. ``Shape`` and ``Light`` are shared:
your answers use them, the tests check against them.
"""

from abc import ABC, abstractmethod
from collections.abc import Sequence
from enum import Enum
from typing import Protocol


class Shape(ABC):
    """The abstract base class for Ex 6."""

    @abstractmethod
    def area(self) -> float: ...

    def describe(self) -> str:
        return f"{type(self).__name__} with area {self.area():.2f}"


class Light(Enum):
    """The traffic light for Ex 10."""

    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"


class CounterLike(Protocol):
    value: int

    def increment(self, step: int = 1) -> None: ...

    def reset(self) -> None: ...


class TemperatureLike(Protocol):
    @property
    def celsius(self) -> float: ...

    @celsius.setter
    def celsius(self, value: float) -> None: ...

    @property
    def fahrenheit(self) -> float: ...


class VectorLike(Protocol):
    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...


class PlaylistLike(Protocol):
    def __len__(self) -> int: ...

    def __contains__(self, song: object) -> bool: ...


class EmployeeLike(Protocol):
    def monthly_pay(self) -> float: ...

    def describe(self) -> str: ...


class HasArea(Protocol):
    def area(self) -> float: ...


class BookLike(Protocol):
    @property
    def title(self) -> str: ...

    @property
    def author(self) -> str: ...

    @property
    def year(self) -> int: ...

    def with_year(self, year: int) -> "BookLike": ...


class OopTasks(Protocol):
    def make_counter(self, start: int) -> CounterLike:
        """Ex 1. A Counter whose ``value`` begins at ``start``.

        increment(step=1) adds ``step`` to value; reset() puts it back to ``start``.
        Every counter keeps its own value.
        """
        ...

    def make_temperature(self, celsius: float) -> TemperatureLike:
        """Ex 2. A Temperature with a ``celsius`` property and a READ-ONLY
        ``fahrenheit`` property (celsius * 9 / 5 + 32).

        Setting celsius below -273.15 (in __init__ too) raises
        ValueError("below absolute zero: <value>") and keeps the old value.
        """
        ...

    def make_vector(self, x: int, y: int) -> VectorLike:
        """Ex 3. A Vector with ``x`` and ``y``.

        repr(make_vector(1, 2)) == "Vector(1, 2)"
        Vectors are equal when x and y are equal, and can go in a set.
        A Vector is never equal to a tuple.
        """
        ...

    def make_playlist(self, name: str, songs: Sequence[str]) -> PlaylistLike:
        """Ex 4. A Playlist that supports len(), ``in`` and str().

        str(make_playlist("Road trip", ["a", "b"])) == "Road trip (2 songs)"
        With one song: "Road trip (1 song)". An empty playlist is falsy.
        """
        ...

    def make_employee(self, name: str, salary: int) -> EmployeeLike:
        """Ex 5. An Employee. monthly_pay() is salary / 12.

        describe() == "<name> earns <monthly pay with 2 decimals> a month"
        """
        ...

    def make_manager(self, name: str, salary: int, bonus: int) -> EmployeeLike:
        """Ex 5. A Manager: a SUBCLASS of your Employee whose monthly_pay()
        adds ``bonus`` to the employee pay. Don't rewrite describe().

        make_manager("Ann", 120_000, 500).describe() == "Ann earns 10500.00 a month"
        """
        ...

    def make_circle(self, radius: float) -> Shape:
        """Ex 6. A class named Circle that inherits from ``Shape``.

        make_circle(1).describe() == "Circle with area 3.14"
        A negative radius raises ValueError.
        """
        ...

    def largest(self, shapes: Sequence[HasArea]) -> HasArea | None:
        """Ex 7. The item with the biggest area(), or None if there are none.
        On a tie, the first one wins. Works for ANY object with area()."""
        ...

    def make_book(self, title: str, author: str, year: int) -> BookLike:
        """Ex 8. A FROZEN dataclass named Book with fields title, author, year.

        repr: "Book(title='Dune', author='Frank Herbert', year=1965)"
        An empty title raises ValueError. Assigning a field raises
        dataclasses.FrozenInstanceError.

        Ex 9. book.with_year(2000) returns a NEW Book with that year;
        the original book does not change.
        """
        ...

    def parse_light(self, text: str) -> Light:
        """Ex 10. The Light whose value matches ``text``, ignoring case and
        surrounding spaces: parse_light(" Green ") is Light.GREEN.
        Unknown text raises ValueError."""
        ...

    def next_light(self, light: Light) -> Light:
        """Ex 10. RED -> GREEN -> YELLOW -> RED."""
        ...

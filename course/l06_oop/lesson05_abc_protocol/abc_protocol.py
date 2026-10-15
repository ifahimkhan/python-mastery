"""
=====================================================================
 LESSON 06.5 - Abstract base classes and Protocols
=====================================================================
 GOAL   : Force subclasses to implement methods with an ABC, and
          describe "anything that has these methods" with a Protocol,
          without any inheritance at all.
 RUN    : uv run python -m course.l06_oop.lesson05_abc_protocol.abc_protocol
 OUTPUT :
          Circle with area 3.14
          Square with area 9.00
          Shape() raised TypeError, message mentions 'area': True
          Triangle() raised TypeError, message mentions 'area': True
          chorus: Quack Beep Quack
          Duck's MRO, no Speaker in it: ['Duck', 'object']
 NOTE   : Generic and runtime-checkable Protocols are covered in level 08.
 NEXT   : lesson06_dataclasses/data_classes.py
=====================================================================
"""

import math
from abc import ABC, abstractmethod
from typing import Protocol


# -- 1. CONCEPT: an ABC is a parent that can't be used on its own ---------
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Every concrete shape MUST write this."""

    # A normal method can rely on the abstract one.
    def describe(self) -> str:
        return f"{type(self).__name__} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2


class Triangle(Shape):  # forgot area()
    pass


# -- 2. CONCEPT: a Protocol describes a SHAPE of object ("duck typing") ---
# Anything with a matching `speak` method fits. No inheritance needed.
class Speaker(Protocol):
    def speak(self) -> str: ...


class Duck:
    def speak(self) -> str:
        return "Quack"


class Robot:
    def speak(self) -> str:
        return "Beep"


def chorus(speakers: list[Speaker]) -> str:
    return " ".join(speaker.speak() for speaker in speakers)


def main() -> None:
    shapes: list[Shape] = [Circle(1), Square(3)]
    for shape in shapes:
        print(shape.describe())

    try:
        Shape()  # type: ignore[abstract]  # mypy catches this before you run
    except TypeError as error:
        # TypeError: Can't instantiate abstract class Shape without an
        # implementation for abstract method 'area'
        print("Shape() raised TypeError, message mentions 'area':", "'area'" in str(error))

    try:
        Triangle()  # type: ignore[abstract]
    except TypeError as error:
        print("Triangle() raised TypeError, message mentions 'area':", "'area'" in str(error))

    print("chorus:", chorus([Duck(), Robot(), Duck()]))
    print("Duck's MRO, no Speaker in it:", [cls.__name__ for cls in Duck.__mro__])

    # -- 3. WHY: which one? ------------------------------------------------
    # ABC:      you own the family of classes and want shared code
    #           (describe) plus a guarantee each child fills in the gaps.
    # Protocol: you only care what an object CAN DO. Great for classes you
    #           don't own and for keeping modules independent. mypy checks
    #           the match; at runtime, Python just calls the method.

    # -- 4. PITFALL: Protocol mismatches show up in mypy, not at runtime ---
    # class Cat:
    #     def meow(self) -> str: return "Meow"
    # chorus([Cat()])
    # mypy:    List item 0 has incompatible type "Cat"; expected "Speaker"
    # runtime: AttributeError: 'Cat' object has no attribute 'speak'
    # Run `uv run mypy` often: it catches this before your users do.

    # -- 5. TRY IT -----------------------------------------------------
    # a) Give Triangle(base, height) an area() and add it to `shapes`.
    # b) Add an abstract perimeter() to Shape. What breaks? Fix each class.
    # c) Write a Dog class with speak() and pass it to chorus(). Did Dog import anything?


if __name__ == "__main__":
    main()

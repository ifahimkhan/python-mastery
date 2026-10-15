"""
=====================================================================
 LESSON 06.2 - Properties, class methods and static methods
=====================================================================
 GOAL   : Guard attributes with @property and setters, compute values
          on the fly, and add alternative constructors with
          @classmethod and helpers with @staticmethod.
 RUN    : uv run python -m course.l06_oop.lesson02_properties.properties
 OUTPUT :
          celsius: 21.5  fahrenheit: 70.7
          after setting 30: 30 86.0
          ValueError: below absolute zero: -300
          value kept: 30
          AttributeError: property 'fahrenheit' of 'Temperature' object has no setter
          in __init__ too: below absolute zero: -500
          Duration(75): 1:15
          from_minutes(3): 3:00
          parse('2:05'): 2:05 = 125 s
          pad(7): 07
 NOTE   : A line like @property is a DECORATOR. How decorators work is
          level 07; for now read it as a label that changes the method.
 NEXT   : lesson03_dunder_methods/dunder_methods.py
=====================================================================
"""

ABSOLUTE_ZERO_C = -273.15
SECONDS_PER_MINUTE = 60


# -- 1. CONCEPT: a property looks like an attribute but runs code ---------
class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius  # goes through the setter below, so it is checked

    @property
    def celsius(self) -> float:
        # A leading underscore means "internal: use the property instead".
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < ABSOLUTE_ZERO_C:
            raise ValueError(f"below absolute zero: {value}")
        self._celsius = value

    # A read-only, COMPUTED property: no setter, nothing stored.
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32


# -- 2. CONCEPT: @classmethod builds objects, @staticmethod is a plain helper
class Duration:
    def __init__(self, seconds: int) -> None:
        self.seconds = seconds

    # cls is the class itself (Duration, or a subclass). Named
    # "from_..." by convention: an alternative way to create an object.
    @classmethod
    def from_minutes(cls, minutes: int) -> "Duration":
        return cls(minutes * SECONDS_PER_MINUTE)

    @classmethod
    def parse(cls, text: str) -> "Duration":
        minutes, seconds = text.split(":")
        return cls(int(minutes) * SECONDS_PER_MINUTE + int(seconds))

    # No self, no cls: a function that simply lives in the class's namespace.
    @staticmethod
    def pad(number: int) -> str:
        return f"{number:02d}"

    def __str__(self) -> str:  # explained in the next lesson
        minutes, seconds = divmod(self.seconds, SECONDS_PER_MINUTE)
        return f"{minutes}:{self.pad(seconds)}"


def main() -> None:
    room = Temperature(21.5)
    print("celsius:", room.celsius, " fahrenheit:", room.fahrenheit)

    room.celsius = 30  # looks like plain assignment, runs the setter
    print("after setting 30:", room.celsius, room.fahrenheit)

    try:
        room.celsius = -300
    except ValueError as error:
        print("ValueError:", error)
    print("value kept:", room.celsius)

    try:
        room.fahrenheit = 100  # type: ignore[misc]  # mypy also spots this
    except AttributeError as error:
        print("AttributeError:", error)

    try:
        Temperature(-500)  # __init__ uses the setter, so this is checked too
    except ValueError as error:
        print("in __init__ too:", error)

    print("Duration(75):", Duration(75))
    print("from_minutes(3):", Duration.from_minutes(3))
    print("parse('2:05'):", Duration.parse("2:05"), "=", Duration.parse("2:05").seconds, "s")
    print("pad(7):", Duration.pad(7))

    # -- 3. WHY properties -------------------------------------------------
    # Start with a plain attribute. If you later need a check or a computed
    # value, turn it into a property: callers keep writing room.celsius and
    # nothing breaks. No need for Java-style get_celsius()/set_celsius().

    # -- 4. PITFALL: the setter assigning to itself -----------------------
    # @celsius.setter
    # def celsius(self, value): self.celsius = value    (no underscore)
    # The setter calls itself forever:
    # RecursionError: maximum recursion depth exceeded

    # -- 5. TRY IT -----------------------------------------------------
    # a) Add a kelvin property with a setter that converts and stores celsius.
    # b) Add Temperature.from_fahrenheit(f) as a @classmethod.
    # c) Make Duration.parse("abc") raise a clear ValueError (level 05).


if __name__ == "__main__":
    main()

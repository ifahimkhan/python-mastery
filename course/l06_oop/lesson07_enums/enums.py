"""
=====================================================================
 LESSON 06.7 - Enums
=====================================================================
 GOAL   : Replace "magic strings" with a fixed set of named values,
          look members up by name or value, loop over them, and match
          on them.
 RUN    : uv run python -m course.l06_oop.lesson07_enums.enums
 OUTPUT :
          member: Color.RED
          name and value: RED 1
          by value Color(2): Color.GREEN
          by name Color['BLUE']: Color.BLUE
          all members: ['RED', 'GREEN', 'BLUE']
          identity check: True
          StrEnum value: in_progress
          StrEnum == str: True
          Status('open'): <Status.OPEN: 'open'>
          light sequence: red -> green -> yellow -> red
          ValueError: 7 is not a valid Color
 NEXT   : ../README.md, then the exercises
=====================================================================
"""

from enum import Enum, StrEnum, auto


# -- 1. CONCEPT: an Enum is a class with a fixed list of members ----------
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Status(StrEnum):  # members ARE strings: handy for JSON and printing
    OPEN = auto()  # auto() picks the value: the lowercase name for StrEnum
    IN_PROGRESS = auto()
    DONE = auto()


# -- 2. CONCEPT: enums can have methods -----------------------------------
class Light(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

    def next(self) -> "Light":
        match self:
            case Light.RED:
                return Light.GREEN
            case Light.GREEN:
                return Light.YELLOW
            case Light.YELLOW:
                return Light.RED


def main() -> None:
    print("member:", Color.RED)
    print("name and value:", Color.RED.name, Color.RED.value)
    print("by value Color(2):", Color(2))
    print("by name Color['BLUE']:", Color["BLUE"])
    print("all members:", [color.name for color in Color])
    print("identity check:", Color(1) is Color.RED)

    print("StrEnum value:", Status.IN_PROGRESS.value)
    from_json = "done"  # e.g. text read from a file
    print("StrEnum == str:", from_json == Status.DONE)
    print("Status('open'):", repr(Status("open")))

    light = Light.RED
    sequence = []
    for _ in range(4):
        sequence.append(light.value)
        light = light.next()
    print("light sequence:", " -> ".join(sequence))

    try:
        Color(7)
    except ValueError as error:
        print("ValueError:", error)

    # -- 3. WHY ------------------------------------------------------------
    # With strings, a typo like "grene" runs and silently does nothing.
    # Light.GREENN fails immediately, PyCharm autocompletes the members,
    # and mypy warns when a `match` forgets one of them.

    # -- 4. PITFALL: comparing a plain Enum to its value ------------------
    # Color.RED == 1   -> False (a plain Enum is NOT its value)
    # Use Color.RED.value == 1, Color(1) is Color.RED, or IntEnum/StrEnum.
    # Members are constants: Color.RED = 5 raises
    # AttributeError: cannot reassign member 'RED'

    # -- 5. TRY IT -----------------------------------------------------
    # a) Add Light.FLASHING and run mypy. What does it say about next()?
    # b) Write a function that turns "Green" (any case) into Light.GREEN.
    # c) Add a `duration` property to Light (RED 30, GREEN 25, YELLOW 5).


if __name__ == "__main__":
    main()

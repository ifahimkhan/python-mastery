"""
=====================================================================
 PRACTICE 07.B - A command registry
=====================================================================
 GOAL   : Build a tiny command interpreter where commands are plain
          functions registered with a decorator, and argument checks
          are added by a second, stackable decorator.
 RUN    : uv run python -m course.l07_functional.practice.command_registry.command_registry
 OUTPUT :
          > help
          commands:
            add     Add whole numbers.
            greet   Say hello to everyone named.
            help    List every command.
            repeat  Repeat words a number of times.
            shout   (no help)
          > greet Ada
          hello, Ada
          > add 2 3 4
          9
          > add 2 x
          usage: add expects whole numbers
          > repeat 3 ho
          ho ho ho
          > repeat
          usage: repeat needs at least 2 argument(s), got 0
          > repeat many ho
          usage: repeat expects a count first, e.g. repeat 3 ho
          > shout
          !
          > dance
          unknown command 'dance' (try: help)
 DESIGN : @registry.command("name") is a decorator WITH an argument: it
          stores the function in a dict and returns it unchanged.
          @needs_args(n) wraps the function with a check. functools.wraps
          keeps the docstring, so `help` can show it. The registry is an
          object, so tests can make a fresh one without shared state.
 EXTEND : Add aliases: @registry.command("sum", "add"). Then add a
          "history" command that lists earlier input lines.
=====================================================================
"""

import functools
from collections.abc import Callable

Command = Callable[..., str]  # takes any number of str arguments, returns text

SCRIPT = (
    "help",
    "greet Ada",
    "add 2 3 4",
    "add 2 x",
    "repeat 3 ho",
    "repeat",
    "repeat many ho",
    "shout",
    "dance",
)


class UsageError(Exception):
    """The command exists but was called the wrong way."""


class CommandRegistry:
    def __init__(self) -> None:
        self._commands: dict[str, Command] = {}

    def command(self, name: str) -> Callable[[Command], Command]:
        if name in self._commands:
            raise ValueError(f"command {name!r} is already registered")

        def register(func: Command) -> Command:
            self._commands[name] = func
            return func  # registered, NOT wrapped: the function stays usable directly

        return register

    @property
    def names(self) -> list[str]:
        return sorted(self._commands)

    def help_text(self) -> str:
        return "\n".join(f"  {name:<7} {_summary(self._commands[name])}" for name in self.names)

    def run(self, line: str) -> str:
        name, *args = line.split() or [""]
        func = self._commands.get(name)
        if func is None:
            return f"unknown command {name!r} (try: help)"
        try:
            return func(*args)
        except UsageError as error:
            return f"usage: {name} {error}"


def _summary(func: Command) -> str:
    """The first line of a function's docstring."""
    doc = func.__doc__
    return doc.strip().splitlines()[0] if doc else "(no help)"


def needs_args(count: int) -> Callable[[Command], Command]:
    """Decorator: refuse calls with fewer than ``count`` arguments."""

    def decorator(func: Command) -> Command:
        @functools.wraps(func)
        def wrapper(*args: str) -> str:
            if len(args) < count:
                raise UsageError(f"needs at least {count} argument(s), got {len(args)}")
            return func(*args)

        return wrapper

    return decorator


def build_registry() -> CommandRegistry:
    registry = CommandRegistry()

    @registry.command("help")
    def show_help() -> str:
        """List every command."""
        return "commands:\n" + registry.help_text()  # a closure over registry

    @registry.command("greet")
    @needs_args(1)
    def greet(*names: str) -> str:
        """Say hello to everyone named."""
        return "hello, " + " and ".join(names)

    @registry.command("add")
    @needs_args(2)
    def add(*numbers: str) -> str:
        """Add whole numbers."""
        try:
            return str(sum(int(number) for number in numbers))
        except ValueError as error:
            raise UsageError("expects whole numbers") from error

    @registry.command("repeat")
    @needs_args(2)
    def repeat(times: str, *words: str) -> str:
        """Repeat words a number of times."""
        if not times.isdigit():
            raise UsageError("expects a count first, e.g. repeat 3 ho")
        return " ".join(words * int(times))

    @registry.command("shout")
    def shout(*words: str) -> str:  # no docstring: help shows "(no help)"
        return " ".join(words).upper() + "!"

    return registry


def main() -> None:
    registry = build_registry()
    for line in SCRIPT:
        print(f"> {line}")
        print(registry.run(line))


if __name__ == "__main__":
    main()

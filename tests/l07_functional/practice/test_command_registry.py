import pytest

from course.l07_functional.practice.command_registry.command_registry import (
    CommandRegistry,
    UsageError,
    build_registry,
    needs_args,
)


@pytest.fixture
def registry() -> CommandRegistry:
    return build_registry()


@pytest.mark.parametrize(
    ("line", "output"),
    [
        ("greet Ada Bo", "hello, Ada and Bo"),
        ("add 2 3 4", "9"),
        ("add -2 2", "0"),
        ("repeat 2 la di", "la di la di"),
        ("shout hey you", "HEY YOU!"),
    ],
)
def test_runs_commands(registry: CommandRegistry, line: str, output: str) -> None:
    assert registry.run(line) == output


@pytest.mark.parametrize(
    ("line", "message"),
    [
        ("greet", "usage: greet needs at least 1 argument(s), got 0"),
        ("add 1", "usage: add needs at least 2 argument(s), got 1"),
        ("add 1 one", "usage: add expects whole numbers"),
        ("repeat x ho", "usage: repeat expects a count first, e.g. repeat 3 ho"),
    ],
)
def test_reports_usage_errors(registry: CommandRegistry, line: str, message: str) -> None:
    assert registry.run(line) == message


@pytest.mark.parametrize("line", ["dance", "", "   "])
def test_unknown_commands(registry: CommandRegistry, line: str) -> None:
    assert registry.run(line).startswith("unknown command")


def test_help_lists_sorted_commands_with_docstrings(registry: CommandRegistry) -> None:
    lines = registry.run("help").splitlines()
    assert lines[0] == "commands:"
    assert [line.split()[0] for line in lines[1:]] == ["add", "greet", "help", "repeat", "shout"]
    assert "Add whole numbers." in lines[1], "needs_args must keep the docstring (wraps)"
    assert lines[-1].endswith("(no help)")


def test_registering_a_name_twice_fails() -> None:
    registry = CommandRegistry()

    @registry.command("ping")
    def ping() -> str:
        return "pong"

    with pytest.raises(ValueError, match="already registered"):
        registry.command("ping")


def test_registered_function_stays_callable_directly() -> None:
    registry = CommandRegistry()

    @registry.command("ping")
    def ping() -> str:
        return "pong"

    assert ping() == "pong"
    assert registry.names == ["ping"]


def test_needs_args_keeps_name_and_checks_count() -> None:
    @needs_args(2)
    def pair(*args: str) -> str:
        """Join two things."""
        return "+".join(args)

    assert pair.__name__ == "pair"
    assert pair.__doc__ == "Join two things."
    assert pair("a", "b") == "a+b"
    with pytest.raises(UsageError):
        pair("a")


def test_registries_are_independent() -> None:
    first, second = CommandRegistry(), build_registry()
    assert first.names == []
    assert "add" in second.names

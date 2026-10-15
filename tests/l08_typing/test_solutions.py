"""Checks the reference answers. Runs in a plain ``uv run pytest`` (keeps CI green)."""

from course.l08_typing.solutions.solutions import TypingSolutions
from course.l08_typing.tasks import TypingTasks
from tests.l08_typing.contract import TypingContract


class TestTypingSolutions(TypingContract):
    tasks: TypingTasks = TypingSolutions()

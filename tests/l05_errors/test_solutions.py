"""Checks the reference answers. Runs in a plain ``uv run pytest`` (keeps CI green)."""

from course.l05_errors.solutions.solutions import ErrorsSolutions
from course.l05_errors.tasks import ErrorsTasks
from tests.l05_errors.contract import ErrorsContract


class TestErrorsSolutions(ErrorsContract):
    tasks: ErrorsTasks = ErrorsSolutions()

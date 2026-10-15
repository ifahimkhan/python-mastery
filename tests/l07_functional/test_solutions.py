"""Checks the reference answers. Runs in a plain ``uv run pytest`` (keeps CI green)."""

from course.l07_functional.solutions.solutions import FunctionalSolutions
from course.l07_functional.tasks import FunctionalTasks
from tests.l07_functional.contract import FunctionalContract


class TestFunctionalSolutions(FunctionalContract):
    tasks: FunctionalTasks = FunctionalSolutions()

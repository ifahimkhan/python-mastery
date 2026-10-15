"""Checks the reference answers. Runs in a plain ``uv run pytest`` (keeps CI green)."""

from course.l06_oop.solutions.solutions import OopSolutions
from course.l06_oop.tasks import OopTasks
from tests.l06_oop.contract import OopContract


class TestOopSolutions(OopContract):
    tasks: OopTasks = OopSolutions()

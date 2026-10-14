"""Checks the reference answers. Runs in a plain ``uv run pytest`` (keeps CI green)."""

from course.l01_basics.solutions.solutions import BasicsSolutions
from course.l01_basics.tasks import BasicsTasks
from tests.l01_basics.contract import BasicsContract


class TestBasicsSolutions(BasicsContract):
    tasks: BasicsTasks = BasicsSolutions()

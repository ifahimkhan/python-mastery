"""Checks the reference answers. Runs in a plain ``uv run pytest`` (keeps CI green)."""

from course.l03_functions.solutions.solutions import FunctionsSolutions
from course.l03_functions.tasks import FunctionsTasks
from tests.l03_functions.contract import FunctionsContract


class TestFunctionsSolutions(FunctionsContract):
    tasks: FunctionsTasks = FunctionsSolutions()

"""Checks the reference answers. Runs in a plain ``uv run pytest`` (keeps CI green)."""

from course.l02_control_flow.solutions.solutions import ControlFlowSolutions
from course.l02_control_flow.tasks import ControlFlowTasks
from tests.l02_control_flow.contract import ControlFlowContract


class TestControlFlowSolutions(ControlFlowContract):
    tasks: ControlFlowTasks = ControlFlowSolutions()

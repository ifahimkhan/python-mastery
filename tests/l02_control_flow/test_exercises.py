"""Checks YOUR answers in course/l02_control_flow/exercises/exercises.py.

Run: uv run pytest -m exercise tests/l02_control_flow   (or click the green arrow next to the class)
Every test fails with NotImplementedError until you write its answer.
"""

import pytest

from course.l02_control_flow.exercises.exercises import ControlFlowExercises
from course.l02_control_flow.tasks import ControlFlowTasks
from tests.l02_control_flow.contract import ControlFlowContract


@pytest.mark.exercise
class TestControlFlowExercises(ControlFlowContract):
    tasks: ControlFlowTasks = ControlFlowExercises()

"""Checks YOUR answers in course/l06_oop/exercises/exercises.py.

Run: uv run pytest -m exercise tests/l06_oop   (or click the green arrow next to the class)
Every test fails with NotImplementedError until you write its answer.
"""

import pytest

from course.l06_oop.exercises.exercises import OopExercises
from course.l06_oop.tasks import OopTasks
from tests.l06_oop.contract import OopContract


@pytest.mark.exercise
class TestOopExercises(OopContract):
    tasks: OopTasks = OopExercises()

"""Checks YOUR answers in course/l07_functional/exercises/exercises.py.

Run: uv run pytest -m exercise tests/l07_functional   (or click the green arrow next to the class)
Every test fails with NotImplementedError until you write its answer.
"""

import pytest

from course.l07_functional.exercises.exercises import FunctionalExercises
from course.l07_functional.tasks import FunctionalTasks
from tests.l07_functional.contract import FunctionalContract


@pytest.mark.exercise
class TestFunctionalExercises(FunctionalContract):
    tasks: FunctionalTasks = FunctionalExercises()

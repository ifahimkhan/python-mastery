"""Checks YOUR answers in course/l05_errors/exercises/exercises.py.

Run: uv run pytest -m exercise tests/l05_errors   (or click the green arrow next to the class)
Every test fails with NotImplementedError until you write its answer.
"""

import pytest

from course.l05_errors.exercises.exercises import ErrorsExercises
from course.l05_errors.tasks import ErrorsTasks
from tests.l05_errors.contract import ErrorsContract


@pytest.mark.exercise
class TestErrorsExercises(ErrorsContract):
    tasks: ErrorsTasks = ErrorsExercises()

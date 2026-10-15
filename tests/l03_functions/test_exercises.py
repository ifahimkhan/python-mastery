"""Checks YOUR answers in course/l03_functions/exercises/exercises.py.

Run: uv run pytest -m exercise tests/l03_functions   (or click the green arrow next to the class)
Every test fails with NotImplementedError until you write its answer.
"""

import pytest

from course.l03_functions.exercises.exercises import FunctionsExercises
from course.l03_functions.tasks import FunctionsTasks
from tests.l03_functions.contract import FunctionsContract


@pytest.mark.exercise
class TestFunctionsExercises(FunctionsContract):
    tasks: FunctionsTasks = FunctionsExercises()

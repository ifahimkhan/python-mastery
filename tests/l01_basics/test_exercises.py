"""Checks YOUR answers in course/l01_basics/exercises/exercises.py.

Run: uv run pytest -m exercise tests/l01_basics   (or click the green arrow next to the class)
Every test fails with NotImplementedError until you write its answer.
"""

import pytest

from course.l01_basics.exercises.exercises import BasicsExercises
from course.l01_basics.tasks import BasicsTasks
from tests.l01_basics.contract import BasicsContract


@pytest.mark.exercise
class TestBasicsExercises(BasicsContract):
    tasks: BasicsTasks = BasicsExercises()

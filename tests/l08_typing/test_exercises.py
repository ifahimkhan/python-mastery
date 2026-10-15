"""Checks YOUR answers in course/l08_typing/exercises/exercises.py.

Run: uv run pytest -m exercise tests/l08_typing   (or click the green arrow next to the class)
Every test fails with NotImplementedError until you write its answer.
Also run `uv run mypy`: in this level the types are part of the answer.
"""

import pytest

from course.l08_typing.exercises.exercises import TypingExercises
from course.l08_typing.tasks import TypingTasks
from tests.l08_typing.contract import TypingContract


@pytest.mark.exercise
class TestTypingExercises(TypingContract):
    tasks: TypingTasks = TypingExercises()

"""Checks YOUR answers in course/l04_collections/exercises/exercises.py.

Run: uv run pytest -m exercise tests/l04_collections   (or click the green arrow next to the class)
Every test fails with NotImplementedError until you write its answer.
"""

import pytest

from course.l04_collections.exercises.exercises import CollectionsExercises
from course.l04_collections.tasks import CollectionsTasks
from tests.l04_collections.contract import CollectionsContract


@pytest.mark.exercise
class TestCollectionsExercises(CollectionsContract):
    tasks: CollectionsTasks = CollectionsExercises()

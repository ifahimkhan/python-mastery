"""Checks the reference answers. Runs in a plain ``uv run pytest`` (keeps CI green)."""

from course.l04_collections.solutions.solutions import CollectionsSolutions
from course.l04_collections.tasks import CollectionsTasks
from tests.l04_collections.contract import CollectionsContract


class TestCollectionsSolutions(CollectionsContract):
    tasks: CollectionsTasks = CollectionsSolutions()

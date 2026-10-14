"""Leaves exercise tests out of a plain ``pytest`` run.

Exercise tests fail until a learner solves them, so a plain run (and CI) must
not include them. They run when you ask for them:

- ``uv run pytest -m exercise``             any marker expression selects them
- ``uv run pytest tests/l01_basics/test_exercises.py``  the file is named directly
- the green run arrow in PyCharm            same as naming the file or test
"""

from pathlib import Path

import pytest

EXERCISE_MARK = "exercise"


def _named_files(config: pytest.Config) -> set[Path]:
    """Files given on the command line, e.g. ``tests/x/test_exercises.py::TestX``."""
    root = Path(config.invocation_params.dir)
    files = set()
    for arg in config.args:
        path = (root / arg.split("::", 1)[0]).resolve()
        if path.is_file():
            files.add(path)
    return files


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    if config.option.markexpr:
        return  # the user chose with -m; respect it

    named = _named_files(config)
    kept: list[pytest.Item] = []
    dropped: list[pytest.Item] = []
    for item in items:
        is_exercise = item.get_closest_marker(EXERCISE_MARK) is not None
        if is_exercise and item.path.resolve() not in named:
            dropped.append(item)
        else:
            kept.append(item)

    if dropped:
        config.hook.pytest_deselected(items=dropped)
        items[:] = kept

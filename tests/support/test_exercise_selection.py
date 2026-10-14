"""Checks the rule in tests/conftest.py: exercises run only when asked for."""

from pathlib import Path

import pytest

CONFTEST = (Path(__file__).resolve().parent.parent / "conftest.py").read_text(encoding="utf-8")

EXERCISE_FILE = """
import pytest

@pytest.mark.exercise
def test_unsolved():
    raise NotImplementedError("Ex 1")
"""

SOLUTION_FILE = """
def test_solved():
    assert True
"""


@pytest.fixture
def project(pytester: pytest.Pytester) -> pytest.Pytester:
    pytester.makeconftest(CONFTEST)
    pytester.makeini("[pytest]\nmarkers =\n    exercise: learner answers\n")
    pytester.makepyfile(test_exercises=EXERCISE_FILE, test_solutions=SOLUTION_FILE)
    return pytester


def test_plain_run_leaves_exercises_out(project: pytest.Pytester) -> None:
    result = project.runpytest()
    result.assert_outcomes(passed=1, deselected=1)


def test_marker_expression_selects_exercises(project: pytest.Pytester) -> None:
    result = project.runpytest("-m", "exercise")
    result.assert_outcomes(failed=1, deselected=1)


def test_naming_the_exercise_file_runs_it(project: pytest.Pytester) -> None:
    result = project.runpytest("test_exercises.py")
    result.assert_outcomes(failed=1)


def test_naming_one_exercise_test_runs_it(project: pytest.Pytester) -> None:
    result = project.runpytest("test_exercises.py::test_unsolved")
    result.assert_outcomes(failed=1)

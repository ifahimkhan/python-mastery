"""Keeps the study material honest.

Runs every lesson and practice project as ``python -m <module>`` and checks
that what it prints matches the OUTPUT block in its header docstring.
"""

import os
import subprocess
import sys
from pathlib import Path

import pytest

from tests.support.lesson_header import expected_output_of

ROOT = Path(__file__).resolve().parent.parent
COURSE = ROOT / "course"
LESSON_TIMEOUT_SECONDS = 10


def _is_runnable(path: Path) -> bool:
    if path.name == "__init__.py":
        return False
    in_lesson = path.parent.name.startswith("lesson")
    in_practice = path.parent.parent.name == "practice"
    return in_lesson or in_practice


def _discover() -> list[Path]:
    return sorted(p for p in COURSE.rglob("*.py") if _is_runnable(p))


def _module_name(path: Path) -> str:
    return ".".join(path.relative_to(ROOT).with_suffix("").parts)


def _run(module: str) -> subprocess.CompletedProcess[str]:
    env = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}
    return subprocess.run(
        [sys.executable, "-m", module],
        cwd=ROOT,
        env=env,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=LESSON_TIMEOUT_SECONDS,
        check=False,
    )


@pytest.mark.timeout(LESSON_TIMEOUT_SECONDS + 5)
@pytest.mark.parametrize("path", _discover(), ids=_module_name)
def test_lesson_prints_what_its_header_promises(path: Path) -> None:
    expected = expected_output_of(path)
    if expected is None:
        pytest.skip("OUTPUT opted out: depends on input, time or scheduling")

    module = _module_name(path)
    result = _run(module)

    assert result.returncode == 0, f"{module} crashed:\n{result.stderr}"
    actual = [line.rstrip() for line in result.stdout.splitlines()]
    while actual and not actual[-1].strip():
        actual.pop()
    assert actual == expected, f"Output of {module} differs from its OUTPUT block"

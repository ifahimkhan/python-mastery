import pytest

import start


def test_welcome_screen_explains_how_to_run_a_lesson(capsys: pytest.CaptureFixture[str]) -> None:
    start.main()
    out = capsys.readouterr().out
    assert "ROADMAP.md" in out
    assert "uv run python -m course." in out
    assert "uv run pytest -m exercise" in out
    assert out.isascii(), "Printed text must be ASCII (see docs/CONVENTIONS.md)"

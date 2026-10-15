import pytest

from course.l02_control_flow.practice.guessing import guessing
from course.l02_control_flow.practice.guessing.guessing import judge, parse_guess, play


@pytest.mark.parametrize(("text", "expected"), [("50", 50), (" 7 ", 7), ("1", 1), ("100", 100)])
def test_parse_guess_accepts_whole_numbers_in_range(text: str, expected: int) -> None:
    assert parse_guess(text) == expected


@pytest.mark.parametrize("text", ["abc", "", "0", "101", "-5", "4.5"])
def test_parse_guess_rejects_everything_else(text: str) -> None:
    assert parse_guess(text) is None


def test_judge_points_towards_the_secret() -> None:
    assert judge(10, 37) == "Too low!"
    assert judge(50, 37) == "Too high!"
    assert judge(37, 37) == "Correct!"


def _type(monkeypatch: pytest.MonkeyPatch, *answers: str) -> None:
    typed = iter(answers)
    monkeypatch.setattr("builtins.input", lambda prompt: next(typed))


def test_play_counts_only_valid_guesses(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _type(monkeypatch, "50", "abc", "25", "37")
    assert play(37) == 3
    out = capsys.readouterr().out
    assert "Too high!" in out
    assert "Too low!" in out
    assert "'abc' is not a whole number from 1 to 100." in out


def test_play_ends_on_the_first_correct_guess(monkeypatch: pytest.MonkeyPatch) -> None:
    _type(monkeypatch, "42")
    assert play(42) == 1


def test_main_reports_the_number_of_guesses(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("random.randint", lambda low, high: 10)
    _type(monkeypatch, "5", "10")
    guessing.main()
    assert capsys.readouterr().out.strip().endswith("Correct! You needed 2 guesses.")

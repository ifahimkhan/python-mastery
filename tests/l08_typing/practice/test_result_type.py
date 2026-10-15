import pytest

from course.l08_typing.practice.result_type.result_type import (
    Account,
    Err,
    Ok,
    Result,
    and_then,
    check_age,
    collect,
    map_ok,
    parse_int,
    sign_up,
    unwrap_or,
)

GOOD_FORM = {"username": " Ada ", "age": "36", "password": "correct horse"}


def _half(number: int) -> Result[int, str]:
    return Ok(number // 2) if number % 2 == 0 else Err(f"{number} is odd")


def test_parse_int() -> None:
    assert parse_int("42") == Ok(42)
    assert parse_int("4.2") == Err("not a number: '4.2'")


def test_map_ok_transforms_only_ok() -> None:
    ok: Result[int, str] = Ok(3)
    err: Result[int, str] = Err("bad")
    assert map_ok(ok, str) == Ok("3")
    assert map_ok(err, str) == Err("bad")


def test_and_then_chains_until_the_first_error() -> None:
    assert and_then(Ok(8), _half) == Ok(4)
    assert and_then(and_then(Ok(8), _half), _half) == Ok(2)
    assert and_then(and_then(Ok(6), _half), _half) == Err("3 is odd")
    err: Result[int, str] = Err("earlier")
    assert and_then(err, _half) == Err("earlier")


def test_unwrap_or() -> None:
    assert unwrap_or(parse_int("7"), 0) == 7
    assert unwrap_or(parse_int("x"), 0) == 0


def test_collect() -> None:
    oks: list[Result[int, str]] = [Ok(1), Ok(2)]
    mixed: list[Result[int, str]] = [Ok(1), Err("a"), Err("b")]
    assert collect(oks) == Ok([1, 2])
    assert collect(mixed) == Err("a"), "the FIRST error wins"
    assert collect([]) == Ok([])


@pytest.mark.parametrize(("age", "ok"), [(12, False), (13, True), (120, True), (121, False)])
def test_check_age_bounds(age: int, ok: bool) -> None:
    assert isinstance(check_age(age), Ok) is ok


def test_sign_up_success_cleans_the_username() -> None:
    assert sign_up(GOOD_FORM) == Ok(Account("ada", 36))


@pytest.mark.parametrize(
    ("changes", "error"),
    [
        ({"username": "d@n"}, "username must be letters and digits: 'd@n'"),
        ({"age": "ten"}, "not a number: 'ten'"),
        ({"age": "7"}, "age must be 13..120, got 7"),
        ({"password": "short"}, "password needs at least 8 characters"),
        ({"username": "", "age": "x"}, "username must be letters and digits: ''"),
    ],
)
def test_sign_up_reports_the_first_problem(changes: dict[str, str], error: str) -> None:
    assert sign_up({**GOOD_FORM, **changes}) == Err(error)


def test_sign_up_with_missing_fields() -> None:
    assert isinstance(sign_up({}), Err)

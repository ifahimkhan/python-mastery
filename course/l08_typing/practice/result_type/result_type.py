"""
=====================================================================
 PRACTICE 08.A - A generic Result type
=====================================================================
 GOAL   : Model "a value OR an error" as data with two generic frozen
          dataclasses, chain steps that may fail, and let mypy and
          `match` make sure every error is handled.
 RUN    : uv run python -m course.l08_typing.practice.result_type.result_type
 OUTPUT :
          created Account(username='ada', age=36)
          rejected: not a number: 'ten'
          rejected: age must be 13..120, got 7
          rejected: username must be letters and digits: 'd@n'
          rejected: password needs at least 8 characters
          map_ok: Ok(value=42)
          unwrap_or: 0
          collect ok: Ok(value=[1, 2])
          collect err: Err(error='boom')
 DESIGN : Result[T, E] = Ok[T] | Err[E]. Functions that can fail RETURN
          an Err instead of raising, so the failure is visible in the
          signature. map_ok / and_then pass an Err through untouched, so
          a chain of steps stops at the first problem.
 EXTEND : Add collect_all(), which returns EVERY error instead of the
          first one: Result[list[T], list[E]].
=====================================================================
"""

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass

MIN_AGE = 13
MAX_AGE = 120
MIN_PASSWORD_LENGTH = 8


@dataclass(frozen=True)
class Ok[T]:
    value: T


@dataclass(frozen=True)
class Err[E]:
    error: E


type Result[T, E] = Ok[T] | Err[E]


def map_ok[T, U, E](result: Result[T, E], func: Callable[[T], U]) -> Result[U, E]:
    """Transform the value of an Ok; pass an Err through unchanged."""
    match result:
        case Ok(value):
            return Ok(func(value))
        case Err():
            return result


def and_then[T, U, E](result: Result[T, E], func: Callable[[T], Result[U, E]]) -> Result[U, E]:
    """Run a step that may itself fail, only if everything so far is Ok."""
    match result:
        case Ok(value):
            return func(value)
        case Err():
            return result


def unwrap_or[T, E](result: Result[T, E], default: T) -> T:
    match result:
        case Ok(value):
            return value
        case Err():
            return default


def collect[T, E](results: Iterable[Result[T, E]]) -> Result[list[T], E]:
    """Ok(list of values), or the FIRST Err."""
    values: list[T] = []
    for result in results:
        match result:
            case Ok(value):
                values.append(value)
            case Err():
                return result
    return Ok(values)


# -- an example domain: a sign-up form ---------------------------------------
@dataclass(frozen=True)
class Account:
    username: str
    age: int


def parse_int(text: str) -> Result[int, str]:
    try:
        return Ok(int(text))
    except ValueError:
        return Err(f"not a number: {text!r}")


def check_age(age: int) -> Result[int, str]:
    if MIN_AGE <= age <= MAX_AGE:
        return Ok(age)
    return Err(f"age must be {MIN_AGE}..{MAX_AGE}, got {age}")


def check_username(name: str) -> Result[str, str]:
    cleaned = name.strip().lower()
    if cleaned.isalnum():
        return Ok(cleaned)
    return Err(f"username must be letters and digits: {name!r}")


def check_password(password: str) -> Result[str, str]:
    if len(password) >= MIN_PASSWORD_LENGTH:
        return Ok(password)
    return Err(f"password needs at least {MIN_PASSWORD_LENGTH} characters")


def sign_up(form: Mapping[str, str]) -> Result[Account, str]:
    # Each isinstance(..., Err) check narrows: after it, mypy knows the
    # value is an Ok, so .value is safe.
    username = check_username(form.get("username", ""))
    if isinstance(username, Err):
        return username
    age = and_then(parse_int(form.get("age", "")), check_age)
    if isinstance(age, Err):
        return age
    password = check_password(form.get("password", ""))
    if isinstance(password, Err):
        return password
    return Ok(Account(username.value, age.value))


FORMS: tuple[dict[str, str], ...] = (
    {"username": " Ada ", "age": "36", "password": "correct horse"},
    {"username": "bo", "age": "ten", "password": "correct horse"},
    {"username": "cy", "age": "7", "password": "correct horse"},
    {"username": "d@n", "age": "40", "password": "short"},
    {"username": "eve", "age": "30", "password": "short"},
)


def main() -> None:
    for form in FORMS:
        match sign_up(form):
            case Ok(account):
                print(f"created {account}")
            case Err(error):
                print(f"rejected: {error}")

    doubled = map_ok(parse_int("21"), lambda n: n * 2)
    print("map_ok:", doubled)
    print("unwrap_or:", unwrap_or(parse_int("x"), 0))
    print("collect ok:", collect([Ok(1), Ok(2)]))
    mixed: list[Result[int, str]] = [Ok(1), Err("boom"), Err("later")]  # mypy needs the hint
    print("collect err:", collect(mixed))


if __name__ == "__main__":
    main()

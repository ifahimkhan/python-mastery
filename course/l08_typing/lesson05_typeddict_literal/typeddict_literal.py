"""
=====================================================================
 LESSON 08.5 - TypedDict, Literal, Final and NamedTuple
=====================================================================
 GOAL   : Type dict-shaped data (like JSON) with TypedDict, restrict a
          value to a few exact options with Literal, protect constants
          with Final, and know when to use each.
 RUN    : uv run python -m course.l08_typing.lesson05_typeddict_literal.typeddict_literal
 OUTPUT :
          Dune (2021), 8.0/10
          Alien (1979), unrated
          at runtime it is a plain dict: dict {'title': 'Dune', 'year': 2021, 'rating': 8.0}
          opening notes.txt in mode 'a'
          sizes allowed: ('S', 'M', 'L')
          price('M'): 4
          coordinate: Coordinate(lat=52.37, lon=4.89) | home.lat: 52.37 | unpacked: 52.37 4.89
          max retries: 3
 NEXT   : lesson06_overloads/overloads.py
=====================================================================
"""

from typing import Final, Literal, NamedTuple, NotRequired, TypedDict, get_args

# -- 1. CONCEPT: Final: a name that must never be re-assigned --------------
MAX_RETRIES: Final = 3  # MAX_RETRIES = 4 later -> mypy: Cannot assign to final name


# -- 2. CONCEPT: TypedDict: a dict with known keys and value types ---------
class Movie(TypedDict):
    title: str
    year: int
    rating: NotRequired[float]  # this key may be missing


# -- 3. CONCEPT: Literal: only these exact values ---------------------------
type Mode = Literal["r", "w", "a"]
type Size = Literal["S", "M", "L"]

PRICES: Final[dict[Size, int]] = {"S": 3, "M": 4, "L": 5}


def open_file(path: str, mode: Mode) -> str:
    return f"opening {path} in mode {mode!r}"


def price(size: Size) -> int:
    return PRICES[size]


# -- 4. CONCEPT: NamedTuple: a typed, immutable tuple with field names -----
class Coordinate(NamedTuple):
    lat: float
    lon: float


def describe(movie: Movie) -> str:
    rating = movie.get("rating")  # NotRequired: use .get(), it may be absent
    stars = f"{rating}/10" if rating is not None else "unrated"
    return f"{movie['title']} ({movie['year']}), {stars}"


def main() -> None:
    dune: Movie = {"title": "Dune", "year": 2021, "rating": 8.0}
    alien: Movie = {"title": "Alien", "year": 1979}
    print(describe(dune))
    print(describe(alien))
    print("at runtime it is a plain dict:", type(dune).__name__, dune)

    print(open_file("notes.txt", "a"))
    print("sizes allowed:", get_args(Size.__value__))
    print("price('M'):", price("M"))

    home = Coordinate(52.37, 4.89)
    lat, lon = home  # unpacks like a tuple
    print("coordinate:", home, "| home.lat:", home.lat, "| unpacked:", lat, lon)
    print("max retries:", MAX_RETRIES)

    # -- 5. WHY: which one? ---------------------------------------------------
    # TypedDict   : data that IS a dict: JSON from an API, **kwargs, config.
    # dataclass   : your own records with methods and validation (level 06).
    # NamedTuple  : small immutable records that should also act as tuples.
    # Literal     : a parameter with a few allowed strings or numbers.
    #               For a set of values used across a program, use an Enum.

    # -- 6. PITFALL: TypedDict and Literal are checked by mypy only -------
    # m: Movie = {"title": "x", "yaer": 1999}
    # mypy: Missing key "year" for TypedDict "Movie"
    # mypy: Extra key "yaer" for TypedDict "Movie"
    # open_file("x", "x")
    # mypy: Argument 2 to "open_file" has incompatible type "Literal['x']";
    #       expected "Literal['r', 'w', 'a']"
    # At runtime both run fine. Data from OUTSIDE (files, users, APIs) must
    # still be validated by hand (exercise 5 does exactly that).

    # -- 7. TRY IT -----------------------------------------------------
    # a) Add a NotRequired `tags: list[str]` key to Movie and use it.
    # b) Call price("XL"). Read mypy's message.
    # c) Turn Coordinate into a frozen dataclass. What stops working?


if __name__ == "__main__":
    main()

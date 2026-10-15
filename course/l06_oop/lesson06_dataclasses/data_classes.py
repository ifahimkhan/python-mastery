"""
=====================================================================
 LESSON 06.6 - Dataclasses
=====================================================================
 GOAL   : Let @dataclass write __init__, __repr__ and __eq__ for you,
          make objects immutable with frozen=True, validate in
          __post_init__, and "change" frozen objects with replace().
 RUN    : uv run python -m course.l06_oop.lesson06_dataclasses.data_classes
 OUTPUT :
          Player(name='Ada', score=0, tags=[])
          Player(name='Ada', score=10, tags=['pro'])
          equal by value: True
          own tags list: []
          asdict: {'name': 'Ada', 'score': 10, 'tags': ['pro']}
          Money(amount=1999, currency='EUR') -> Money(amount=2499, currency='EUR')
          original unchanged: 1999
          FrozenInstanceError: cannot assign to field 'amount'
          ValueError: currency must be a 3-letter code, got 'euro'
          hashable, usable in a set: 1
          sorted: [(0, 9, 0), (1, 2, 3), (1, 10, 0)]
          Version(1, 2) < Version(1, 10): True
 NEXT   : lesson07_enums/enums.py
=====================================================================
"""

from dataclasses import FrozenInstanceError, asdict, dataclass, field, replace


# -- 1. CONCEPT: declare the fields, get the boilerplate for free --------
@dataclass
class Player:
    name: str
    score: int = 0  # a default; fields with defaults come last
    # NEVER `tags: list[str] = []`. A factory makes a fresh list per object.
    tags: list[str] = field(default_factory=list)


# -- 2. CONCEPT: frozen=True makes objects immutable (and hashable) ------
@dataclass(frozen=True)
class Money:
    amount: int  # in cents: never use float for money
    currency: str

    def __post_init__(self) -> None:  # runs right after the generated __init__
        if len(self.currency) != len("EUR"):
            raise ValueError(f"currency must be a 3-letter code, got {self.currency!r}")

    def add(self, other: "Money") -> "Money":
        if other.currency != self.currency:
            raise ValueError(f"cannot add {other.currency} to {self.currency}")
        return replace(self, amount=self.amount + other.amount)  # a NEW object


# -- 3. CONCEPT: order=True adds <, <=, >, >= (compares fields in order) ---
@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int
    patch: int = 0


def main() -> None:
    ada = Player("Ada")
    print(ada)  # generated __repr__
    ada.score += 10
    ada.tags.append("pro")
    print(ada)
    print("equal by value:", Player("Bo", 5) == Player("Bo", 5))
    print("own tags list:", Player("Cy").tags)
    print("asdict:", asdict(ada))

    price = Money(1999, "EUR")
    total = price.add(Money(500, "EUR"))
    print(price, "->", total)
    print("original unchanged:", price.amount)
    try:
        price.amount = 0  # type: ignore[misc]  # mypy also refuses this
    except FrozenInstanceError as error:
        print("FrozenInstanceError:", error)
    try:
        Money(100, "euro")
    except ValueError as error:
        print("ValueError:", error)
    print("hashable, usable in a set:", len({Money(1, "USD"), Money(1, "USD")}))

    versions = [Version(1, 10), Version(1, 2, 3), Version(0, 9)]
    print("sorted:", [(v.major, v.minor, v.patch) for v in sorted(versions)])
    print("Version(1, 2) < Version(1, 10):", Version(1, 2) < Version(1, 10))

    # -- 4. WHY ------------------------------------------------------------
    # Most classes mainly HOLD data. A dataclass says that in a few lines
    # and can't forget a field in __eq__. Prefer frozen=True: an object
    # that never changes can be shared, cached and used as a dict key.

    # -- 5. PITFALL: a mutable default ------------------------------------
    # @dataclass
    # class Team:
    #     members: list[str] = []
    # ValueError: mutable default <class 'list'> for field members is not
    # allowed: use default_factory
    #
    # frozen only stops REASSIGNING fields: a frozen object holding a list
    # can still have that list changed. Use tuples inside frozen classes.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Make Version print as "1.2.3" by adding a __str__ method.
    # b) Add Money.times(n) that returns a new Money, using replace().
    # c) Try Money(1, "EUR") < Money(2, "EUR"). Why does it fail?


if __name__ == "__main__":
    main()

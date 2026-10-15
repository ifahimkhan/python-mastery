"""
=====================================================================
 LESSON 06.1 - Classes and objects
=====================================================================
 GOAL   : Define a class, create objects from it with __init__, give
          them attributes and methods, and tell instance attributes
          apart from class attributes.
 RUN    : uv run python -m course.l06_oop.lesson01_classes.classes
 OUTPUT :
          Rex is 3 years old
          Fido is 5 years old
          after birthday: Rex is 4 years old
          same as Dog.describe(rex): Rex is 4 years old
          species via the class: Canis familiaris
          species via an object: Canis familiaris
          type(rex): Dog
          isinstance(rex, Dog): True
          counters: 2 1
          vars(rex): {'name': 'Rex', 'age': 4}
          BadTeam blue.members: ['Ann'] (Ann leaked in!)
          GoodTeam yellow.members: []
 NEXT   : lesson02_properties/properties.py
=====================================================================
"""


# -- 1. CONCEPT: a class is a blueprint, an object is one thing built from it
class Dog:
    # A CLASS attribute: one value, shared by every Dog.
    species = "Canis familiaris"

    # __init__ runs when you call Dog(...). `self` is the new object.
    def __init__(self, name: str, age: int) -> None:
        self.name = name  # INSTANCE attributes: every dog has its own
        self.age = age

    # A method is a function defined in a class. Python passes `self` for you:
    # rex.describe() runs Dog.describe(rex).
    def describe(self) -> str:
        return f"{self.name} is {self.age} years old"

    def have_birthday(self) -> None:
        self.age += 1  # methods may change the object's own state


class Counter:
    def __init__(self) -> None:
        self.count = 0

    def increment(self) -> None:
        self.count += 1


# -- 3. PITFALL: a mutable CLASS attribute is shared by every object --------
class BadTeam:
    members: list[str] = []  # ONE list for ALL teams!  # noqa: RUF012

    def add(self, name: str) -> None:
        self.members.append(name)


class GoodTeam:
    def __init__(self) -> None:
        self.members: list[str] = []  # a fresh list for each team

    def add(self, name: str) -> None:
        self.members.append(name)


def main() -> None:
    rex = Dog("Rex", 3)
    fido = Dog("Fido", 5)
    print(rex.describe())
    print(fido.describe())

    rex.have_birthday()
    print("after birthday:", rex.describe())
    print("same as Dog.describe(rex):", Dog.describe(rex))

    print("species via the class:", Dog.species)
    print("species via an object:", fido.species)  # found on the class
    print("type(rex):", type(rex).__name__)
    print("isinstance(rex, Dog):", isinstance(rex, Dog))

    # Every object keeps its own state.
    first, second = Counter(), Counter()
    first.increment()
    first.increment()
    second.increment()
    print("counters:", first.count, second.count)

    # vars() shows an object's own attributes (a dict, level 04).
    print("vars(rex):", vars(rex))

    red, blue = BadTeam(), BadTeam()
    red.add("Ann")
    print("BadTeam blue.members:", blue.members, "(Ann leaked in!)")

    green, yellow = GoodTeam(), GoodTeam()
    green.add("Ann")
    print("GoodTeam yellow.members:", yellow.members)

    # -- 2. WHY classes --------------------------------------------------
    # A class keeps data AND the functions that work on it together.
    # Instead of passing (name, age) tuples to loose functions, you ask the
    # object itself: rex.describe(). Each object guards its own state.

    # -- 4. PITFALL: forgetting `self` -----------------------------------
    # def describe() -> str: ...      (no self)
    # rex.describe()
    # TypeError: Dog.describe() takes 0 positional arguments but 1 was given
    #
    # def __init__(self, name): name = name    (no self.)
    # just sets a local variable; rex.name then raises
    # AttributeError: 'Dog' object has no attribute 'name'

    # -- 5. TRY IT -----------------------------------------------------
    # a) Add a method rename(new_name) to Dog and use it on fido.
    # b) Set Dog.species = "wolf". What do rex.species and fido.species show now?
    # c) Set rex.species = "robot". Does fido change? Print vars(rex) to see why.


if __name__ == "__main__":
    main()

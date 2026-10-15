"""
=====================================================================
 LESSON 06.3 - Dunder methods
=====================================================================
 GOAL   : Make your objects print nicely, compare by value, work in
          sets and dicts, and support len(), `in` and truth tests, by
          writing "double underscore" (dunder) methods.
 RUN    : uv run python -m course.l06_oop.lesson03_dunder_methods.dunder_methods
 OUTPUT :
          plain repr starts with: <__main__.PlainPoint object ...>
          PlainPoint(1, 2) == PlainPoint(1, 2): False
          repr: Point(1, 2)
          str:  (1, 2)
          in a list, repr is used: [Point(1, 2), Point(3, 4)]
          f-string !r: Point(1, 2)
          Point(1, 2) == Point(1, 2): True
          Point(1, 2) == (1, 2): False
          set of three points: 2 unique
          dict lookup with an equal point: origin
          Basket('apple', 'pear') has 2 items
          'pear' in basket: True
          empty basket is truthy? False
 NOTE   : Arithmetic operators like + and < are level 12.
 NEXT   : lesson04_inheritance/inheritance.py
=====================================================================
"""


class PlainPoint:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# -- 1. CONCEPT: Python calls dunder methods for you ---------------------
#   repr(p)  -> p.__repr__()     str(p), print(p) -> p.__str__()
#   p == q   -> p.__eq__(q)      hash(p)          -> p.__hash__()
#   len(b)   -> b.__len__()      x in b           -> b.__contains__(x)
#   if b:    -> b.__bool__()  (falls back to __len__)
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    # For developers: unambiguous, ideally looks like code that rebuilds it.
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    # For users: friendly. Without __str__, print() uses __repr__.
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented  # "I don't know": Python then answers False
        return (self.x, self.y) == (other.x, other.y)

    # Objects that are equal MUST have the same hash. Hash the same fields.
    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Basket:
    def __init__(self, *items: str) -> None:
        self.items = list(items)

    def __len__(self) -> int:
        return len(self.items)

    def __contains__(self, item: str) -> bool:
        return item in self.items

    def __repr__(self) -> str:
        return f"Basket({', '.join(repr(item) for item in self.items)})"


def main() -> None:
    plain = PlainPoint(1, 2)
    print("plain repr starts with:", repr(plain).split(" object")[0] + " object ...>")
    print("PlainPoint(1, 2) == PlainPoint(1, 2):", PlainPoint(1, 2) == PlainPoint(1, 2))

    p = Point(1, 2)
    print("repr:", repr(p))
    print("str: ", p)
    print("in a list, repr is used:", [p, Point(3, 4)])
    print("f-string !r:", f"{p!r}")

    print("Point(1, 2) == Point(1, 2):", Point(1, 2) == Point(1, 2))
    print("Point(1, 2) == (1, 2):", Point(1, 2) == (1, 2))
    print("set of three points:", len({Point(1, 2), Point(1, 2), Point(5, 5)}), "unique")
    labels = {Point(0, 0): "origin"}
    print("dict lookup with an equal point:", labels[Point(0, 0)])

    basket = Basket("apple", "pear")
    print(basket, "has", len(basket), "items")
    print("'pear' in basket:", "pear" in basket)
    print("empty basket is truthy?", bool(Basket()))

    # -- 2. WHY ------------------------------------------------------------
    # Dunder methods let your class plug into Python's own syntax and
    # built-ins. Users of Basket write len(basket), not basket.count_items().
    # Always write __repr__: debugging and test failures print it.

    # -- 3. PITFALL: __eq__ without __hash__ --------------------------------
    # If a class defines __eq__ but not __hash__, Python sets __hash__ to None:
    # {Point(1, 2)}
    # TypeError: unhashable type: 'Point'
    # And never hash a field that can change: a changed object gets "lost"
    # inside the set or dict it was stored in.

    # -- 4. TRY IT -----------------------------------------------------
    # a) Remove __str__ from Point. What does print(p) show now?
    # b) Delete __hash__ and run again. Which line fails?
    # c) Give Basket a __bool__ that is False when it holds only "nothing".


if __name__ == "__main__":
    main()

"""
=====================================================================
 PRACTICE 04.C - Shop inventory
=====================================================================
 GOAL   : Model stock as a tuple of immutable records, then answer
          questions about it and apply a delivery without changing
          the original data.
 RUN    : uv run python -m course.l04_collections.practice.inventory.inventory
 OUTPUT :
          total value: 198.00
          low stock: ['notebook', 'stapler']
          tags: ['cheap', 'kitchen', 'office', 'paper']
          office items: ['pen', 'notebook', 'stapler']
          after delivery: {'pen': 40, 'notebook': 23, 'mug': 12, 'stapler': 7}
          low stock now: []
          old stock unchanged: {'pen': 40, 'notebook': 3, 'mug': 12, 'stapler': 2}
 DESIGN : Item is a NamedTuple, so items can't be changed by accident.
          restock() builds NEW items with _replace() and returns a new
          tuple; the old stock stays exactly as it was.
 EXTEND : Add sell(stock, name, quantity) that refuses to go below zero.
=====================================================================
"""

from typing import NamedTuple

LOW_STOCK_LIMIT = 5


class Item(NamedTuple):
    name: str
    price: float
    quantity: int
    tags: frozenset[str]


Stock = tuple[Item, ...]  # a tuple of any length holding Items


def total_value(stock: Stock) -> float:
    return sum(item.price * item.quantity for item in stock)


def low_stock(stock: Stock, limit: int = LOW_STOCK_LIMIT) -> list[str]:
    """Names of items with fewer than ``limit`` units, alphabetically."""
    return sorted(item.name for item in stock if item.quantity < limit)


def all_tags(stock: Stock) -> set[str]:
    tags: set[str] = set()
    for item in stock:
        tags |= item.tags  # union, written in place on our OWN new set
    return tags


def with_tag(stock: Stock, tag: str) -> list[str]:
    return [item.name for item in stock if tag in item.tags]


def restock(stock: Stock, delivery: dict[str, int]) -> Stock:
    """A NEW stock with each delivered quantity added. Unknown names are ignored."""
    return tuple(
        item._replace(quantity=item.quantity + delivery.get(item.name, 0)) for item in stock
    )


def quantities(stock: Stock) -> dict[str, int]:
    return {item.name: item.quantity for item in stock}


def main() -> None:
    stock: Stock = (
        Item("pen", 1.50, 40, frozenset({"office", "cheap"})),
        Item("notebook", 4.00, 3, frozenset({"office", "paper"})),
        Item("mug", 8.50, 12, frozenset({"kitchen"})),
        Item("stapler", 12.00, 2, frozenset({"office"})),
    )

    print(f"total value: {total_value(stock):.2f}")
    print("low stock:", low_stock(stock))
    print("tags:", sorted(all_tags(stock)))
    print("office items:", with_tag(stock, "office"))

    new_stock = restock(stock, {"notebook": 20, "stapler": 5, "unknown": 99})
    print("after delivery:", quantities(new_stock))
    print("low stock now:", low_stock(new_stock))
    print("old stock unchanged:", quantities(stock))


if __name__ == "__main__":
    main()

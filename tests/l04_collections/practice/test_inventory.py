import pytest

from course.l04_collections.practice.inventory.inventory import (
    Item,
    Stock,
    all_tags,
    low_stock,
    quantities,
    restock,
    total_value,
    with_tag,
)

STOCK: Stock = (
    Item("pen", 1.5, 40, frozenset({"office"})),
    Item("mug", 8.0, 2, frozenset({"kitchen", "gift"})),
    Item("card", 2.0, 0, frozenset({"gift"})),
)


def test_total_value() -> None:
    assert total_value(STOCK) == pytest.approx(76.0)
    assert total_value(()) == 0


def test_low_stock_is_sorted_and_respects_the_limit() -> None:
    assert low_stock(STOCK) == ["card", "mug"]
    assert low_stock(STOCK, limit=1) == ["card"]


def test_all_tags_and_with_tag() -> None:
    assert all_tags(STOCK) == {"office", "kitchen", "gift"}
    assert with_tag(STOCK, "gift") == ["mug", "card"]
    assert with_tag(STOCK, "garden") == []


def test_restock_returns_new_items_and_ignores_unknown_names() -> None:
    new_stock = restock(STOCK, {"mug": 3, "lamp": 10})
    assert quantities(new_stock) == {"pen": 40, "mug": 5, "card": 0}
    assert quantities(STOCK) == {"pen": 40, "mug": 2, "card": 0}, "old stock must not change"
    assert new_stock is not STOCK


def test_items_are_immutable() -> None:
    with pytest.raises(AttributeError):
        STOCK[0].quantity = 99  # type: ignore[misc]

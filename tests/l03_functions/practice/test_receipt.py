import pytest

from course.l03_functions.practice.receipt.receipt import WIDTH, line, rule, subtotal, tip


def test_line_aligns_the_price_to_the_right() -> None:
    row = line("Coffee", 3.5)
    assert row == "Coffee                    3.50"
    assert len(row) == WIDTH


def test_line_multiplies_by_quantity() -> None:
    assert line("Croissant", 2.5, quantity=2) == "Croissant x 2             5.00"


def test_line_accepts_a_custom_width() -> None:
    assert line("Tea", 1, width=10) == "Tea   1.00"


def test_subtotal_adds_any_number_of_prices() -> None:
    assert subtotal() == 0
    assert subtotal(1.25, 2.5, 3) == pytest.approx(6.75)


@pytest.mark.parametrize(("amount", "expected"), [(12.75, 1.27), (0.7, 0.07), (10, 1.0), (0, 0)])
def test_tip_rounds_down_to_the_cent(amount: float, expected: float) -> None:
    assert tip(amount) == pytest.approx(expected)


def test_tip_rate_can_change() -> None:
    assert tip(100, rate=0.15) == pytest.approx(15.0)


def test_rule() -> None:
    assert rule() == "*" * WIDTH
    assert rule("-", 5) == "-----"

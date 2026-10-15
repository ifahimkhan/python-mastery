import random

import pytest

from course.l06_oop.practice.card_deck.card_deck import Card, Deck, Rank, Suit, show


def test_a_new_deck_has_52_unique_cards() -> None:
    deck = Deck()
    assert len(deck) == 52
    assert len(set(deck)) == 52


def test_a_new_deck_is_in_order() -> None:
    deck = Deck()
    assert deck[0] == Card(Rank.TWO, Suit.CLUBS)
    assert deck[-1] == Card(Rank.ACE, Suit.SPADES)


@pytest.mark.parametrize(
    ("card", "text"),
    [
        (Card(Rank.TWO, Suit.CLUBS), "2C"),
        (Card(Rank.TEN, Suit.HEARTS), "10H"),
        (Card(Rank.QUEEN, Suit.DIAMONDS), "QD"),
        (Card(Rank.ACE, Suit.SPADES), "AS"),
    ],
)
def test_card_str(card: Card, text: str) -> None:
    assert str(card) == text


def test_cards_order_by_rank_then_suit() -> None:
    assert Card(Rank.KING, Suit.CLUBS) < Card(Rank.ACE, Suit.CLUBS)
    assert Card(Rank.ACE, Suit.CLUBS) < Card(Rank.ACE, Suit.SPADES)
    assert Card(Rank.TWO, Suit.SPADES) < Card(Rank.THREE, Suit.CLUBS)


def test_deal_takes_cards_from_the_top() -> None:
    deck = Deck()
    hand = deck.deal(3)
    assert show(hand) == "2C 3C 4C"
    assert len(deck) == 49
    assert Card(Rank.TWO, Suit.CLUBS) not in deck


def test_deal_zero_and_all() -> None:
    deck = Deck()
    assert deck.deal(0) == ()
    assert len(deck.deal(52)) == 52
    assert len(deck) == 0


@pytest.mark.parametrize("count", [-1, 53])
def test_deal_rejects_impossible_counts(count: int) -> None:
    deck = Deck()
    with pytest.raises(ValueError):
        deck.deal(count)
    assert len(deck) == 52, "a failed deal must not remove cards"


def test_a_seeded_shuffle_is_repeatable() -> None:
    first, second = Deck(), Deck()
    first.shuffle(random.Random(1))
    second.shuffle(random.Random(1))
    assert list(first) == list(second)
    assert list(first) != list(Deck()), "shuffling changes the order"
    assert sorted(first) == sorted(Deck()), "shuffling keeps the same cards"

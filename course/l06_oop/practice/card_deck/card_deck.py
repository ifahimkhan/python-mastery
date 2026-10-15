"""
=====================================================================
 PRACTICE 06.B - A deck of cards
=====================================================================
 GOAL   : Build playing cards from enums and a frozen dataclass, and a
          Deck that works with len(), indexing, `in`, `for` and sorted().
 RUN    : uv run python -m course.l06_oop.practice.card_deck.card_deck
 OUTPUT :
          new deck: 52 cards
          first and last: 2C AS
          AS in deck: True
          hearts: 13
          hand:   6D 2S 7H QC 3S
          sorted: 2S 3S 6D 7H QC
          highest: QC
          left in deck: 47
          AS still in deck: True
          ValueError: cannot deal 100 cards, only 47 left
 DESIGN : Rank and Suit are IntEnums so cards can be ordered. Card is a
          frozen, ordered dataclass: rank first, so sorting is by rank,
          then suit. The Deck takes a random.Random, so tests and this
          demo can pass a seeded one and get the same shuffle every time.
 EXTEND : Add is_flush(hand) and is_straight(hand), then deal 1000 hands
          and count how often each one happens.
=====================================================================
"""

import random
from collections.abc import Iterator
from dataclasses import dataclass
from enum import IntEnum

SEED = 7
HAND_SIZE = 5


class Suit(IntEnum):  # bridge order: clubs lowest, spades highest
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


FACE_LABELS = {Rank.JACK: "J", Rank.QUEEN: "Q", Rank.KING: "K", Rank.ACE: "A"}


@dataclass(frozen=True, order=True)
class Card:
    rank: Rank
    suit: Suit

    def __str__(self) -> str:
        label = FACE_LABELS.get(self.rank, str(self.rank.value))
        return f"{label}{self.suit.name[0]}"  # e.g. "QH", "10S"


class Deck:
    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in Suit for rank in Rank]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index: int) -> Card:
        return self._cards[index]

    def __contains__(self, card: object) -> bool:
        return card in self._cards

    def __iter__(self) -> Iterator[Card]:  # how iterators work: level 07
        return iter(self._cards)

    def shuffle(self, rng: random.Random) -> None:
        rng.shuffle(self._cards)

    def deal(self, count: int) -> tuple[Card, ...]:
        """Take ``count`` cards from the top of the deck."""
        if count < 0:
            raise ValueError(f"count must not be negative, got {count}")
        if count > len(self._cards):
            raise ValueError(f"cannot deal {count} cards, only {len(self._cards)} left")
        hand = tuple(self._cards[:count])
        del self._cards[:count]
        return hand


def show(cards: tuple[Card, ...]) -> str:
    return " ".join(str(card) for card in cards)


def main() -> None:
    deck = Deck()
    print("new deck:", len(deck), "cards")
    print("first and last:", deck[0], deck[-1])
    print("AS in deck:", Card(Rank.ACE, Suit.SPADES) in deck)
    print("hearts:", sum(1 for card in deck if card.suit is Suit.HEARTS))

    deck.shuffle(random.Random(SEED))
    hand = deck.deal(HAND_SIZE)
    print("hand:  ", show(hand))
    print("sorted:", show(tuple(sorted(hand))))
    print("highest:", max(hand))
    print("left in deck:", len(deck))
    print("AS still in deck:", Card(Rank.ACE, Suit.SPADES) in deck)

    try:
        deck.deal(100)
    except ValueError as error:
        print("ValueError:", error)


if __name__ == "__main__":
    main()

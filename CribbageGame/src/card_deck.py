from dataclasses import dataclass, field
import random
from typing import List


@dataclass(order=True)
class Card:
    """[summary]

    Returns:
        [type]: [description]
    """

    sort_card_value: int = field(init=False, repr=False)
    formal_name: str = field(init=False, repr=False)
    name: str
    suit: str
    value: int
    rank: int

    def __post_init__(self):
        object.__setattr__(self, "sort_card_value", self.value)
        self.formal_name = f"{self.name.title()} of {self.suit.title()}"

    def __str__(self):
        return f"{self.name.title() + ' of '+ self.suit.title(): <20} {self.value: >5}"

    def __hash__(self):
        return hash((self.name, self.suit, self.value, self.rank))


class Deck:
    """[summary]"""

    def __init__(self):
        self.card_deck = self.create_deck()

    @staticmethod
    def create_deck():
        """[summary]

        Returns:
            [type]: [description]
        """
        cards = {
            "ace": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "jack": 10,
            "queen": 10,
            "king": 10,
        }
        suits = ["hearts", "diamonds", "clubs", "spades"]

        full_deck = []

        for suit in suits:
            rank_value = 1
            for card_name, card_value in cards.items():
                full_deck.append(Card(card_name, suit, card_value, rank_value))
                rank_value += 1
        return full_deck

    def shuffle_deck(self, seed_number=None):
        """[summary]"""
        if seed_number:
            random.seed(seed_number)
        random.shuffle(self.card_deck)

    def draw_cards(self, number_of_cards: int) -> List:
        """
        Creates a hand of cards
        :param number_of_cards: user supplied cards to be drawn
        :return: dictionary of cards with (keys=card name, value=numerical value)
        """
        player_hand = []
        for _ in range(number_of_cards):
            player_hand.append(self.card_deck.pop())
        return player_hand

    def draw_specific_card(self, card_name: str = None, suit: str = None) -> Card:
        """allows the user to draw a specific card from the deck

        Args:
            card_name (str): spelled out name of the card
            suit (str): hearts, spades, clubs, diamonds

        Raises:
            KeyError: Raises a KeyError if you try to pick a card that doesn't exist.

        Returns:
            Card: a single card that matches your criteria.
        """

        for index, card in enumerate(self.card_deck):
            if card.name == card_name and card.suit == suit:
                self.card_deck.pop(index)
                return card
        raise KeyError("Card does not exist!")

    def __len__(self):
        return len(self.card_deck)

    def __getitem__(self, __index: int):
        return self.card_deck[__index]


if __name__ == "__main__":
    card_deck = Deck()
    card_deck.draw_specific_card()

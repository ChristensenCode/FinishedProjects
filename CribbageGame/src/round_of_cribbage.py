from src.card_deck import Card, Deck
from src.players import Player
from src.ui import UI
from src.cli import CLI
import random
from typing import List


class RoundCrib:
    def __init__(self) -> None:
        self.crib = []

    def add_cards_to_crib(self, cards_to_add: List[Card]):
        for card in cards_to_add:
            self.crib.append(card)

    def get_crib(self):
        return self.crib

    def add_card_to_crib(self, Card):
        self.crib.append(Card)


class RoundOfCribbage:
    def __init__(
        self,
        deck_of_cards: Deck,
        players: List[Player],
        crib: RoundCrib,
    ):
        self.deck_of_cards = deck_of_cards
        self.deck_of_cards.shuffle_deck()
        self.players = players
        self.crib = crib
        self.user_interface = UI()
        self.cli = CLI()

    def draw_cards(self, hand_size=6):
        return self.deck_of_cards.draw_cards(hand_size)

    def cut_card(self):
        return random.choice(self.deck_of_cards)

    def round_setup(self):
        for player in self.players:
            player.hand = self.draw_phase()
            player = self.discard_and_build_crib(player)
        cut_card = self.cut_card()
        self._jack_cut_point(cut_card, self.players)

        self.user_interface.display_cut_card(cut_card)
        return self.players, self.crib, cut_card

    @staticmethod
    def _jack_cut_point(card_cut: Card, players: List[Player]):
        if card_cut.rank != 11:
            return
        for player in players:
            if not player.has_crib():
                continue
            print(f"--> {player.get_name()} gets 1 point for cutting a Jack!")
            player.total_score += 1

    def draw_phase(self):
        hand = self.draw_cards()
        return sorted(hand, key=lambda x: x.rank)

    def discard_and_build_crib(self, player: Player):
        cards_to_discard = self.cli.get_cards_to_discard(
            player.player_name, player.hand
        )
        player.discard_cards_from_hand(cards_to_discard)
        self.crib.add_cards_to_crib(cards_to_discard)
        return player

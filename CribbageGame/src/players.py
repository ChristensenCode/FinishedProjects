from dataclasses import dataclass, field
from typing import List
from src.card_deck import Card
import random

from src.cli import CLI
from src.ui import UI


@dataclass
class Player:
    player_name: str = ""
    total_score: int = 0
    hand: List[Card] = field(default_factory=lambda: [])
    crib_status: bool = False
    can_lay_card: bool = True

    def sort_hand(self):
        self.hand = sorted(self.hand, key=lambda x: x.rank)

    def discard_cards_from_hand(self, cards_to_remove: List[Card]):
        for card in cards_to_remove:
            self.hand.remove(card)

    def get_name(self) -> str:
        return self.player_name

    def get_score(self) -> int:
        return self.player_name

    def has_crib(self) -> bool:
        return self.crib_status

    def get_hand(self) -> List[Card]:
        return self.hand

    def lay_card(self, card_to_lay: Card) -> Card:
        card_index = self.hand.index(card_to_lay)
        selected_card = self.hand[card_index]
        self.hand.remove(card_to_lay)
        UI().display_laid_card(self.player_name, selected_card)
        return selected_card

    def has_cards(self) -> bool:
        return True if len(self.hand) > 0 else False

    def get_card_by_index(self, index: int) -> Card:
        return self.hand[index]

    def is_player_able_to_lay(self):
        return self.can_lay_card

    def set_can_lay_card(self, new_setting: bool) -> None:
        self.can_lay_card = new_setting

    def set_hand(self, new_hand: List[Card]) -> None:
        self.hand = new_hand

    def add_card(self, card_to_add: Card) -> None:
        self.hand.append(card_to_add)

    def set_crib_status(self, new_value: bool) -> None:
        self.crib_status = new_value


class PlayerFactory:
    def __init__(self, player_count: int = 2) -> None:
        self.player_count = player_count
        self.cli_data = CLI()
        self.user_interface = UI()
        self.players = self.create_players()
        self.get_player_names()
        self.who_starts_with_crib()
        self.set_player_scores()

    def create_players(self):
        return [Player() for _ in range(self.player_count)]

    def get_player_names(self):
        for player in self.players:
            player.player_name = self.cli_data.get_player_names()

    def who_starts_with_crib(self):
        player_with_starting_crib = random.choice(self.players)
        player_index = self.players.index(player_with_starting_crib)
        player_with_starting_crib = self.players[player_index]
        self.user_interface.crib_selection_message(
            player_with_starting_crib.player_name
        )
        player_with_starting_crib.crib_status = True

    def set_player_scores(self):
        for player in self.players:
            player.total_score = 0

    def get_players(self):
        return self.players

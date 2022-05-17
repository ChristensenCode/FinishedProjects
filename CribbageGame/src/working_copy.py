from typing import List
import numpy as np
from src.players import Player
from src.cli import CLI
from src.ui import UI
from src.card_deck import Card
import copy


class PeggingStage:
    def __init__(self, players: List[Player]) -> None:
        self.players = self.order_players_by_crib_status(players)
        self.pegging_players = self.create_player_copies(self.players)
        self.command_line_input = CLI()
        self.user_interface = UI()
        self.able_to_lay = self.able_to_lay()
        self.cards_in_hand = self.get_hand_length()

    def is_player_able_to_lay(self, player_hand: List[Card], current_stack_value: int):
        if not self.does_player_have_cards(player_hand):
            return False
        minimum_card_value = min(player_hand, key=lambda x: x.value).value
        if current_stack_value + minimum_card_value > 31:
            return False
        return True

    def does_player_have_cards(self, player_hand: List[Card]) -> bool:
        return True if len(player_hand) > 0 else False

    def action_if_player_out_of_cards(self, player_name: str):
        self.user_interface.display_out_of_cards_message(player_name)
        self.able_to_lay[player_name] = False

    def count_pegging_points(self):
        laid_stack = []
        laid_count = 0
        last_laid = None
        self.user_interface.display_laid_pile(laid_stack, laid_count)
        while (self.cards_in_hand > 0).all():
            for pegging_player in self.pegging_players:
                current_player_hand = pegging_player.hand
                current_player_name = pegging_player.player_name
                if not self.does_player_have_cards(current_player_hand):
                    self.action_if_player_out_of_cards(current_player_name)
                else:
                    minimum_card_value = min(
                        current_player_hand, key=lambda x: x.value
                    ).value

                # both are unable to lay
                if (
                    not any(self.able_to_lay.values())
                    and last_laid == pegging_player.player_name
                ):
                    self.able_to_lay = {
                        player: True for (player, _) in self.able_to_lay.items()
                    }
                    self.user_interface.display_last_card_to_lay_point(
                        pegging_player.player_name
                    )
                    pegging_player.total_score += 1
                    laid_stack = []
                    laid_count = 0
                    self.user_interface.display_laid_pile(laid_stack, laid_count)
                    continue

                elif not self.able_to_lay[pegging_player.player_name]:
                    continue

                elif laid_count + minimum_card_value > 31:
                    self.user_interface.display_unable_to_message(
                        pegging_player.player_name
                    )
                    self.able_to_lay[pegging_player.player_name] = False
                    continue

                elif last_laid == pegging_player.player_name:
                    continue

                laid_card_index = self.command_line_input.get_card_to_lay(
                    pegging_player.player_name, pegging_player.hand
                )
                laid_card = pegging_player.hand[laid_card_index]
                laid_card_value = laid_card.value

                if laid_count + laid_card_value < 31:
                    pegging_player.hand.pop(laid_card_index)
                    laid_stack.append(laid_card)
                    laid_count += laid_card_value
                    self.user_interface.display_laid_card(
                        pegging_player.player_name, laid_card.formal_name
                    )
                    last_laid = pegging_player.player_name

                elif laid_count + laid_card_value == 31:
                    self.user_interface.display_31_point(pegging_player.player_name)
                    pegging_player.hand.pop(laid_card_index)
                    laid_stack.append(laid_card)
                    laid_count += laid_card_value
                    pegging_player.total_score += 2
                    laid_stack = []
                    laid_count = 0
                    self.user_interface.display_laid_card(
                        pegging_player.player_name, laid_card.formal_name
                    )
                    last_laid = pegging_player.player_name

                self.user_interface.display_laid_pile(laid_stack, laid_count)
            else:
                self.cards_in_hand = self.get_hand_length()
        for pegging_player in self.pegging_players:
            if last_laid != pegging_player.player_name:
                continue
            pegging_player.total_score += 1
            self.user_interface.display_last_card_to_lay_point(
                pegging_player.player_name
            )
        return [player.total_score for player in self.pegging_players]

    def create_player_copies(self, players):
        return [copy.copy(player) for player in players]

    def get_hand_length(self):
        return np.array(
            [len(pegging_hand.hand) for pegging_hand in self.pegging_players]
        )

    def able_to_lay(self):
        return dict([(player.player_name, True) for player in self.pegging_players])

    def order_players_by_crib_status(self, players: List[Player]):
        return sorted(players, key=lambda x: x.crib_status)


class ScoreHandStage:
    pass


class ScoreCribStage:
    pass

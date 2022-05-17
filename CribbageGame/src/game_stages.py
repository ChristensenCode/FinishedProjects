from dataclasses import dataclass, field
from typing import List
from src.players import Player
from src.cli import CLI
from src.ui import UI
import copy
from src.card_deck import Card
from math import perm
import operator
from src.analyze_cribbage_hand import CribbageHandAnalyzer


@dataclass
class DiscardPile:
    current_value: int = 0
    maximum_value: int = 31
    last_played_card: Card = None
    layed_cards: List[Card] = field(default_factory=lambda: [])
    last_player_to_play: Player = None

    def get_current_discard_value(self):
        return self.current_value

    def get_last_played_card(self):
        return self.last_played_card

    def can_lay_card(self, card_value: int):
        if card_value + self.current_value > self.maximum_value:
            return False
        return True

    def get_last_player_to_lay(self) -> None:
        return self.last_player_to_play

    def add_card_to_discard(self, card_to_lay: Card, player_who_laid: Player):
        self.current_value += card_to_lay.value
        self.layed_cards.append(card_to_lay)
        self.last_played_card = card_to_lay
        self.last_player_to_play = player_who_laid
        self.is_pile_fifteen()
        self.is_pile_thirty_one()
        self.is_run()
        self.is_repeat()

    def is_pile_fifteen(self) -> None:
        if self.current_value == 15:
            UI().display_15_point(self.last_player_to_play.get_name())
            self.last_player_to_play.total_score += 2

    def is_pile_thirty_one(self) -> None:
        if self.current_value == self.maximum_value:
            self.last_player_to_play.total_score += 2
            self.reset_discard_pile()
            UI().display_31_point(self.last_player_to_play.get_name())

    def is_run(self) -> None:
        longest_run = self._repeat_or_run_length_finder(
            self.layed_cards, smallest_length=3, function_to_use=self._run_checker
        )
        if longest_run > 0:
            UI().display_longest_run(self.last_player_to_play.get_name(), longest_run)
            self.last_player_to_play.total_score += longest_run

    def is_repeat(self) -> None:
        smallest_needed_for_repeat = 2
        longest_repeat = self._repeat_or_run_length_finder(
            self.layed_cards,
            smallest_length=smallest_needed_for_repeat,
            function_to_use=self._all_same,
        )
        if longest_repeat > 0:
            points = perm(longest_repeat, smallest_needed_for_repeat)
            UI().display_longest_repeat(self.last_player_to_play.get_name(), points)
            self.last_player_to_play.total_score += points

    def _repeat_or_run_length_finder(
        self,
        layed_stack: List[Card],
        smallest_length=0,
        function_to_use=None,
    ) -> int:
        if len(layed_stack) < smallest_length:
            return 0
        flipped_discard_stack = layed_stack[::-1]
        flipped_length = len(flipped_discard_stack)
        longest_value = 0
        for index in range(smallest_length, flipped_length + 1):
            discard_slice = flipped_discard_stack[:index]
            success_pattern = function_to_use(discard_slice)
            longer = index > longest_value
            if success_pattern and longer:
                longest_value = index
        return longest_value

    def _run_diff(self, ordered_list: List[int]) -> List[int]:
        list_length = len(ordered_list)
        first_part = ordered_list[1:]
        last_part = ordered_list[:list_length]
        differences = map(operator.sub, first_part, last_part)
        single_differences = [
            True if difference == 1 else False for difference in differences
        ]
        return single_differences

    def _run_checker(self, cards_to_check: List[Card]) -> bool:
        cards_in_order = sorted(cards_to_check, key=lambda x: x.rank)
        ranks = self._get_ranks(cards_in_order)
        if all(self._run_diff(ranks)):
            return True
        return False

    def _all_same(self, cards_to_check: List[Card]) -> bool:
        get_ranks = self._get_ranks(cards_to_check)
        return True if max(get_ranks) == min(get_ranks) else False

    def _get_ranks(self, cards_to_check: List[Card]) -> List:
        return [card.rank for card in cards_to_check]

    def reset_discard_pile(self) -> None:
        self.current_value = 0
        self.last_played_card = None
        self.layed_cards = []


class PeggingStage:
    def __init__(
        self,
        players: List[Player],
        cli_commands: CLI,
        ui: UI,
        discard_pile: DiscardPile,
    ) -> None:
        self.players = self.order_players_by_crib_status(players)
        self.original_points = self._get_original_points(self.players)
        self.pegging_players = self.create_player_copies(self.players)
        self.command_line_input = cli_commands
        self.user_interface = ui
        self.discard_stack = discard_pile

    def main_pegging_loop(self) -> List[int]:
        number_of_turns = 1
        first_round_flag = True
        while self.cards_left_in_play(self.pegging_players) > 0:
            while self.can_players_lay(self.pegging_players):
                player = self.select_player_to_lay(number_of_turns)
                if player.has_crib() and first_round_flag:
                    first_round_flag = False
                    number_of_turns += 1
                    continue
                UI().display_laid_pile(
                    self.discard_stack.layed_cards,
                    self.discard_stack.get_current_discard_value(),
                )

                chosen_card = self.card_selection_process(player)
                if chosen_card is None:
                    number_of_turns += 1
                    continue
                player.lay_card(chosen_card)
                self.discard_stack.add_card_to_discard(chosen_card, player)
                number_of_turns += 1

            else:
                self.user_interface.display_last_card_to_lay_point(
                    self.discard_stack.get_last_player_to_lay().get_name()
                )
                self.discard_stack.get_last_player_to_lay().total_score += 1
                self.reset_can_lay_status(self.pegging_players)
                self.discard_stack.reset_discard_pile()
        for player_with_hand, player_with_points in zip(
            self.players, self.pegging_players
        ):
            player_with_hand.total_score = player_with_points.total_score
        return self.players

    def _get_original_points(self, players: List[Player]) -> List[int]:
        return {player.get_name(): player.total_score for player in players}

    def get_points_from_pegging(self):
        for player_with_hand, player_with_points in zip(
            self.players, self.pegging_players
        ):
            player_with_hand.total_score = player_with_points.total_score

    def select_player_to_lay(self, turns: int) -> Player:
        return self.pegging_players[turns % len(self.pegging_players)]

    def card_selection_process(self, player: Player) -> Card:
        selected_card_value = self.calculate_smallest_card_value(player)
        if not self.discard_stack.can_lay_card(selected_card_value):
            UI().display_unable_to_lay_message(player.get_name())
            player.set_can_lay_card(False)
            return None
        elif len(player.get_hand()) == 0:
            UI().display_out_of_cards_message(player.get_name())
            return None

        while True:
            selected_card_index = self.command_line_input.get_card_to_lay(
                player.get_name(), player.get_hand()
            )
            selected_card = player.get_card_by_index(selected_card_index)
            if self.discard_stack.can_lay_card(selected_card.value):
                return selected_card
            UI().display_invalid_choice(selected_card)

    def can_players_lay(self, players: List[Player]) -> bool:
        player_lay_status = sum([player.is_player_able_to_lay() for player in players])
        return True if player_lay_status != 0 else False

    def reset_can_lay_status(self, players: List[Player]) -> None:
        for player in players:
            player.set_can_lay_card(True)

    def create_player_copies(self, players: List[Player]):
        return [copy.deepcopy(player) for player in players]

    def cards_left_in_play(self, players: List[Player]):
        return sum([len(player.hand) for player in players])

    def calculate_smallest_card_value(self, player: Player) -> int:
        if player.has_cards():
            return min(player.get_hand(), key=lambda x: x.value).value
        # Returning 32 ensures that if the player is out of cards
        # that they cannot lay.
        return 32

    def order_players_by_crib_status(self, players: List[Player]):
        return sorted(players, key=lambda x: x.crib_status, reverse=True)


class ScoreHandAndCribStage:
    def __init__(self, players: List[Player], crib: List[Card], cut_card: Card):
        self.players = sorted(players, key=lambda x: x.crib_status)
        self.cut_card = cut_card
        self.crib = crib

    def main_hand_loop(self):
        self.crib.append(self.cut_card)
        for player in self.players:
            player.get_hand().append(self.cut_card)
            player.total_score += self.get_card_collection_points(
                player.get_name(), player.get_hand()
            )
            if player.has_crib():
                player.total_score += self.get_card_collection_points("Crib", self.crib)
                player.set_crib_status = False
                continue
            crib_player = player.get_name()
            player.set_crib_status = True
        print(f"--> {crib_player} has the crib next round.")
        self._print_total_score(self.players)

    def _print_total_score(self, players: List[Player]):
        for player in players:
            print(f"{player.get_name()} has {player.total_score} points.")

    def get_card_collection_points(
        self, player_hand: List[Card], player_name: str
    ) -> int:
        print(f"{player_name} Cards")
        print("-" * 50)
        UI().display_collection_of_cards(player_hand)
        hand_points = CribbageHandAnalyzer(player_hand).count_points()
        UI().display_score_template("Total", hand_points)
        print("-" * 50)

        return hand_points


class ScoreCribStage:
    pass


if __name__ == "__main__":
    test_discard = [
        Card(name="one", suit="hearts", value=1, rank=1),
        Card(name="one", suit="hearts", value=1, rank=1),
        Card(name="three", suit="hearts", value=3, rank=3),
        Card(name="four", suit="hearts", value=4, rank=4),
    ]


def _test_data(pegging_players):
    test_hands = [
        [
            Card(name="one", suit="hearts", value=1, rank=1),
            Card(name="one", suit="hearts", value=1, rank=1),
            Card(name="three", suit="hearts", value=3, rank=3),
            Card(name="four", suit="hearts", value=4, rank=4),
        ],
        [
            Card(name="one", suit="spades", value=1, rank=1),
            Card(name="one", suit="spades", value=1, rank=1),
            Card(name="king", suit="spades", value=10, rank=13),
            Card(name="four", suit="spades", value=4, rank=4),
        ],
    ]

    test_hand_two = [
        [
            Card(name="one", suit="hearts", value=1, rank=1),
            Card(name="two", suit="hearts", value=2, rank=2),
            Card(name="three", suit="hearts", value=3, rank=3),
            Card(name="four", suit="hearts", value=4, rank=4),
        ],
        [
            Card(name="six", suit="spades", value=6, rank=6),
            Card(name="five", suit="spades", value=5, rank=5),
            Card(name="four", suit="spades", value=4, rank=4),
            Card(name="three", suit="spades", value=3, rank=3),
        ],
    ]
    test_hand_two = [
        [
            Card(name="one", suit="hearts", value=1, rank=1),
            Card(name="one", suit="spades", value=1, rank=1),
            Card(name="one", suit="clubs", value=1, rank=1),
            Card(name="one", suit="diamonds", value=1, rank=1),
        ],
        [
            Card(name="ten", suit="hearts", value=10, rank=10),
            Card(name="ten", suit="spades", value=10, rank=10),
            Card(name="ten", suit="clubs", value=10, rank=10),
            Card(name="ten", suit="diamonds", value=10, rank=10),
        ],
    ]
    # for player, hand in zip(pegging_players, test_hand_two):
    #     player.set_hand(hand)
    # return pegging_players

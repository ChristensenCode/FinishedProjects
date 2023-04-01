from itertools import combinations, permutations
from typing import Iterable, List, Tuple
from src.card_deck import Card
from src.ui import UI


class CribbageHandAnalyzer:
    """[summary]"""

    def __init__(self, player_hand: List[Card]):
        """[summary]

        Args:
            player_hand ([type]): [description]
        """
        self.player_hand = player_hand
        self._minimum_cards_for_fifteen = 2
        self._minimum_cards_for_run = 3
        self._maximum_number_of_cards = 6

    def count_points(self):
        hand_points = 0
        hand_points += self.count_fifteens()
        hand_points += self.count_flush()
        hand_points += self.count_pairs()
        hand_points += self.count_runs()
        return hand_points

    def all_hand_combinations(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        house_cleaning = map(sorted, permutations(self.player_hand, 4))
        unique_fifteens = []
        for fifteens in house_cleaning:
            fifteens = tuple(fifteens)
            if fifteens in unique_fifteens:
                continue
            unique_fifteens.append(fifteens)
        return permutations(self.player_hand, 4)

    @staticmethod
    def _remove_dup_fifteens(list_of_fifteens: Iterable) -> List[Tuple]:
        """[summary]

        Args:
            list_of_fifteens (Iterable): [description]

        Returns:
            List[Tuple]: [description]
        """
        unique_fifteens = []
        for fifteens in list_of_fifteens:
            fifteens = tuple(fifteens)
            if fifteens in unique_fifteens:
                continue
            unique_fifteens.append(fifteens)
        return unique_fifteens

    def count_fifteens(self):
        fifteen_points = 0
        for index in range(
            self._minimum_cards_for_fifteen, self._maximum_number_of_cards
        ):
            combos = list(combinations(self.player_hand, index))
            for combo in combos:
                if sum(map(lambda x: x.value, combo)) != 15:
                    continue
                fifteen_points += 2
        UI().display_score_template("Fifteens", fifteen_points)
        return fifteen_points

    def count_runs(self):
        run_points = 0
        matched_runs = []
        for index in reversed(
            range(self._minimum_cards_for_run, self._maximum_number_of_cards)
        ):
            combos = list(combinations(self.player_hand, index))
            for combo in combos:
                combo_sorted_by_rank = sorted(combo, key=lambda x: x.rank)
                card_ranks = list(map(lambda x: x.rank, combo_sorted_by_rank))
                rank_differences = self._custom_diff(card_ranks)
                
                if not all(x == 1 for x in rank_differences):
                    continue
                elif combo_sorted_by_rank in matched_runs:
                    continue
                elif self._check_for_duplicate_runs(combo_sorted_by_rank, matched_runs):
                    continue

                run_points += len(combo)
                matched_runs.append(combo_sorted_by_rank)
        UI().display_score_template("Runs", run_points)
        return run_points

    @staticmethod
    def _custom_diff(items_to_diff: List[int]):
        diff_list = []
        for index in range(1, len(items_to_diff)):
            diff_list.append(items_to_diff[index] - items_to_diff[index - 1])
        return diff_list

    def _check_for_duplicate_runs(
        self, combo_sorted_by_rank: List[Card], matched_runs: List[List[Card]]
    ):
        combo_as_set = set(combo_sorted_by_rank)

        for matched_run in matched_runs:
            if set(matched_run).issuperset(combo_as_set):
                return True
        return False

    def count_pairs(self):
        """counts the number of pairs. This means it works for three of a kind too."""
        possible_pairs = combinations(self.player_hand, r=2)
        pair_counter = 0
        for card_one, card_two in possible_pairs:
            if card_one.name == card_two.name:
                pair_counter += 2
        UI().display_score_template("Pairs", pair_counter)
        return pair_counter

    def _does_hand_have_flush(self, player_hand: List[Card]):
        card_faces = set(map(lambda x: x.suit, player_hand))
        if len(card_faces) == 1:

            return True
        return False

    def count_flush(self):
        hand_without_cut = self.player_hand[: len(self.player_hand) - 1]
        hand_without_cut_length = len(hand_without_cut)
        player_hand_length = len(self.player_hand)
        if self._does_hand_have_flush(hand_without_cut) and self._does_hand_have_flush(
            self.player_hand
        ):
            UI().display_score_template("Flush", player_hand_length)
            return player_hand_length
        elif self._does_hand_have_flush(hand_without_cut):
            UI().display_score_template("Flush", hand_without_cut_length)
            return hand_without_cut_length
        UI().display_score_template("Flush", 0)
        return 0


if __name__ == "__main__":

    hand = [
        Card(name="one", suit="hearts", value=1, rank=1),
        Card(name="four", suit="spades", value=4, rank=4),
        Card(name="two", suit="clubs", value=2, rank=2),
        Card(name="three", suit="diamonds", value=3, rank=3),
    ]
    cut_card = Card(name="three", suit="hearts", value=3, rank=3)
    CribbageHandAnalyzer(hand).count_runs(cut_card)

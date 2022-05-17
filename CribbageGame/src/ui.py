from typing import List
from src.card_deck import Card


class UI:
    def __init__(self) -> None:
        banner_length = 50
        self.standard_banner = "-" * banner_length
        self.information_banner = "=" * banner_length

    def display_collection_of_cards(self, cards: List[Card]) -> None:
        for card_number, card in enumerate(cards):
            print(f"[{card_number + 1}]\t{card}")

    def display_asking_for_player_name(self):
        print("Hello, what's your name?")
        print(self.standard_banner)

    def display_welcoming_player(self, player_name: str):
        print(f"Welcome {player_name}!\n")

    def prompt_to_discard_to_crib(self, player_name: str):
        print(f"{player_name} please, select two card numbers to discard:")
        print(self.standard_banner)

    def crib_selection_message(self, person_selected: str):
        print(f"--> {person_selected} starts with the Crib.\n")

    def display_cut_card(self, cut_card: Card):
        print(f"\n--> {cut_card.formal_name} was cut.\n")

    def display_pegging_turn(self, player_name: str):
        print(f"It's {player_name}'s turn to lay.")

    def display_laid_card(self, player_name: str, card_name: str):
        print(f"{player_name} laid {card_name}\n")

    def display_out_of_cards_message(self, player_name: str):
        print(f"{player_name} is out of cards!")

    def display_laid_pile(self, cards: List[Card], pile_total: int):
        print("Current Laydown Pile")
        print(self.standard_banner)
        self.display_collection_of_cards(cards)
        print(f"Pile Total: {pile_total}\n")

    def display_unable_to_lay_message(self, player_name: str):
        print(f"{player_name} is unable to lay.")

    def display_31_point(self, player_name: str):
        print(f"--> {player_name} got 31 for 2 points.")

    def display_15_point(self, player_name: str):
        print(f"--> {player_name} got 15 for 2 points.")

    def display_last_card_to_lay_point(self, player_name: str):
        print(f"--> {player_name} was last to lay for 1 point.")

    def display_longest_run(self, player_name: str, run_score: int) -> None:
        print(f"--> {player_name} got {run_score} points for a run!")

    def display_longest_repeat(self, player_name: str, repeat_score: int) -> None:
        print(f"--> {player_name} got {repeat_score} points for a repeat!")

    def display_invalid_choice(self, selected_card: Card) -> None:
        print(
            f"{selected_card.formal_name} is an invalid choice. Please, select another card."
        )

    def display_score_template(self, score_type: str, point_value: int) -> None:
        print(f">>> {score_type}:\t\t{point_value}")

from src.ui import UI
from typing import List
from src.card_deck import Card
from src.utility import check_user_provided_data


class CLI:
    def __init__(self) -> None:
        self.user_interface = UI()

    def get_player_names(self):
        self.user_interface.display_asking_for_player_name()
        user_supplied_name = input().title()
        self.user_interface.display_welcoming_player(user_supplied_name)
        return user_supplied_name

    def get_cards_to_discard(
        self, player_name: str, player_hand: List[Card]
    ) -> List[Card]:
        self.user_interface.prompt_to_discard_to_crib(player_name)
        self.user_interface.display_collection_of_cards(player_hand)
        acceptable_input = False
        while not acceptable_input:
            card_indexes = input().split()
            checked_user_input = check_user_provided_data(
                card_indexes, len(player_hand)
            )
            if checked_user_input:
                acceptable_input = True

        cards_to_crib = []
        for card_index in card_indexes:
            cards_to_crib.append(player_hand[int(card_index) - 1])

        return cards_to_crib

    def get_card_to_lay(self, player_name: str, player_hand: List[Card]):
        self.user_interface.display_pegging_turn(player_name)
        self.user_interface.display_collection_of_cards(player_hand)
        acceptable_input = False
        while not acceptable_input:
            card_index = input().split()
            checked_user_input = check_user_provided_data(
                card_index, len(player_hand), number_of_cards=1
            )
            if checked_user_input:
                acceptable_input = True

        return int(card_index[0]) - 1

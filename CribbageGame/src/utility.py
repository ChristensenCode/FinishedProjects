from typing import List


def check_number_of_cards(
    indexes_to_check: List[str], acceptable_length: int = 2
) -> bool:
    number_of_cards = len(indexes_to_check)
    if number_of_cards == acceptable_length:
        return True
    elif number_of_cards > acceptable_length:
        print(f"{number_of_cards} is too many cards selected! Try again.")
        return False
    print(f"{number_of_cards} is not enough cards selected! Try again.")
    return False


def check_cards_type(indexes_to_check: List[str]) -> bool:
    for value_to_check in indexes_to_check:
        try:
            _ = int(value_to_check)
        except (TypeError, ValueError):
            print(f"{value_to_check} is not an integer! Try again.")
            return False
    return True


def check_card_in_range(indexes_to_check: List[str], length_of_hand: int) -> bool:
    for index in indexes_to_check:
        index_as_int = int(index)
        if index_as_int <= 0:
            print(f"{index_as_int} is too small! Try again.")
            return False

        elif index_as_int > length_of_hand:
            print(f"{index_as_int} is too large! Try again.")
            return False

    return True


def check_duplicate_card_index(indexes_to_check: List[str]) -> bool:
    if len(indexes_to_check) == 1:
        return True
    return True if len(set(indexes_to_check)) == len(indexes_to_check) else False


def check_user_provided_data(
    indexes_to_check, length_of_hand, number_of_cards=2
) -> bool:
    card_count = check_number_of_cards(
        indexes_to_check, acceptable_length=number_of_cards
    )
    card_type = check_cards_type(indexes_to_check)
    in_range = check_card_in_range(indexes_to_check, length_of_hand)
    unique_values = check_duplicate_card_index(indexes_to_check)
    if all((card_count, card_type, in_range, unique_values)):
        return True
    return False

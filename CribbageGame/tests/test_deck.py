import pytest
from src.card_deck import Deck


def test_card_dealer_count():
    card_deck = Deck()
    card_deck.shuffle_deck(seed_number=11)
    player_hand = card_deck.draw_cards(6)
    assert len(player_hand) == 6


def test_check_specific_card_draw():
    card_deck = Deck()
    jack_of_clubs = card_deck.draw_specific_card(card_name="jack", suit="clubs")
    assert jack_of_clubs.name == "jack"
    assert jack_of_clubs.suit == "clubs"


def test_check_specific_card_draw_error_wrong_name():
    card_deck = Deck()
    with pytest.raises(KeyError):
        card_deck.draw_specific_card(card_name="simon", suit="clubs")


def test_check_specific_card_draw_error_wrong_suit():
    card_deck = Deck()
    with pytest.raises(KeyError):
        card_deck.draw_specific_card(card_name="ace", suit="reds")


def test_check_specific_card_draw_error_both_wrong():
    card_deck = Deck()
    with pytest.raises(KeyError):
        card_deck.draw_specific_card(card_name="carol", suit="balloons")


def test_same_card_cant_be_picked_twice():
    card_deck = Deck()
    card_deck.draw_specific_card(card_name="king", suit="hearts")
    with pytest.raises(KeyError):
        card_deck.draw_specific_card(card_name="king", suit="hearts")

import pytest
from src.analyze_cribbage_hand import CribbageHandAnalyzer
from src.card_deck import Card, Deck


def test_count_zero_pairs():
    deck = Deck()
    hand = []
    hand.append(deck.draw_specific_card(card_name="ace", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="ten", suit="clubs"))
    hand.append(deck.draw_specific_card(card_name="two", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="three", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="four", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="five", suit="hearts"))
    cribbage_analysis = CribbageHandAnalyzer(hand)
    pair_points = cribbage_analysis.count_pairs()
    assert pair_points == 0


def test_count_one_pairs():
    deck = Deck()
    hand = []
    hand.append(deck.draw_specific_card(card_name="ace", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="ace", suit="clubs"))
    hand.append(deck.draw_specific_card(card_name="two", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="three", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="four", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="five", suit="hearts"))
    cribbage_analysis = CribbageHandAnalyzer(hand)
    pair_points = cribbage_analysis.count_pairs()
    assert pair_points == 2


def test_count_two_pairs():
    deck = Deck()
    hand = []
    hand.append(deck.draw_specific_card(card_name="ace", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="ace", suit="clubs"))
    hand.append(deck.draw_specific_card(card_name="two", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="two", suit="clubs"))
    hand.append(deck.draw_specific_card(card_name="four", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="five", suit="hearts"))
    cribbage_analysis = CribbageHandAnalyzer(hand)
    pair_points = cribbage_analysis.count_pairs()
    assert pair_points == 4


def test_count_three_of_a_kind():
    deck = Deck()
    hand = []
    hand.append(deck.draw_specific_card(card_name="ace", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="ace", suit="clubs"))
    hand.append(deck.draw_specific_card(card_name="ace", suit="diamonds"))
    hand.append(deck.draw_specific_card(card_name="two", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="four", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="five", suit="hearts"))
    cribbage_analysis = CribbageHandAnalyzer(hand)
    pair_points = cribbage_analysis.count_pairs()
    assert pair_points == 6


def test_runs_quad_run_of_four():
    hand = [
        Card(name="seven", suit="diamonds", value=7, rank=7),
        Card(name="five", suit="clubs", value=5, rank=5),
        Card(name="six", suit="hearts", value=6, rank=6),
        Card(name="eight", suit="diamonds", value=8, rank=8),
        Card(name="seven", suit="hearts", value=7, rank=7),
        Card(name="eight", suit="spades", value=8, rank=8),
    ]
    cribbage_analysis = CribbageHandAnalyzer(hand)
    pair_points = cribbage_analysis.count_runs()
    assert pair_points == 16


def test_run_of_three():
    hand = [
        Card(name="five", suit="hearts", value=5, rank=5),
        Card(name="jack", suit="spades", value=10, rank=11),
        Card(name="ace", suit="clubs", value=1, rank=1),
        Card(name="ten", suit="clubs", value=10, rank=10),
        Card(name="three", suit="spades", value=3, rank=3),
        Card(name="two", suit="spades", value=2, rank=2),
    ]
    cribbage_analysis = CribbageHandAnalyzer(hand)
    pair_points = cribbage_analysis.count_runs()
    assert pair_points == 3


def test_no_runs():
    hand = [
        Card(name="nine", suit="diamonds", value=9, rank=9),
        Card(name="four", suit="diamonds", value=4, rank=4),
        Card(name="four", suit="spades", value=4, rank=4),
        Card(name="five", suit="clubs", value=5, rank=5),
        Card(name="nine", suit="clubs", value=9, rank=9),
        Card(name="queen", suit="spades", value=10, rank=12),
    ]
    cribbage_analysis = CribbageHandAnalyzer(hand)
    pair_points = cribbage_analysis.count_runs()
    assert pair_points == 0


def test_face_card_run():
    """i only include this test because face cards value differs from their rank"""
    deck = Deck()
    hand = []
    hand.append(deck.draw_specific_card(card_name="king", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="queen", suit="clubs"))
    hand.append(deck.draw_specific_card(card_name="jack", suit="diamonds"))
    hand.append(deck.draw_specific_card(card_name="jack", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="queen", suit="hearts"))
    hand.append(deck.draw_specific_card(card_name="ten", suit="hearts"))
    cribbage_analysis = CribbageHandAnalyzer(hand)
    pair_points = cribbage_analysis.count_runs()
    assert pair_points == 16

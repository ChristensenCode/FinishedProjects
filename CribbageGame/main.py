#! /usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""

import os
from src import analyze_cribbage_hand
from src.card_deck import Deck
from src.game_stages import PeggingStage, DiscardPile
from src.players import PlayerFactory
from src.round_of_cribbage import RoundOfCribbage, RoundCrib
from src.cli import CLI
from src.ui import UI


def run_game():
    """main run script for the cribbage game."""
    # number_of_players = input()
    number_of_players = 2

    players = PlayerFactory(player_count=number_of_players).get_players()
    # for player in players:
    # player.total_score += 100
    game_running = True
    while game_running:
        # TODO create a library for a deck of cards
        round_deck = Deck()
        round_crib = RoundCrib()
        discard_pile = DiscardPile()
        cli = CLI()
        ui = UI()
        round_information = RoundOfCribbage(round_deck, players, round_crib)
        players, round_crib, cut_card = round_information.round_setup()
        peg_stage = PeggingStage(players, cli, ui, discard_pile)
        updated_players = peg_stage.main_pegging_loop()
        original_points = peg_stage.original_points

        # counts points from player hands
        # TODO move this somewhere else
        os.system("cls" if os.name == "nt" else "clear")
        for index, player in enumerate(
            sorted(updated_players, key=lambda x: x.crib_status)
        ):
            print(f"{player.get_name()} Hand")
            print("-" * 50)
            print(f"Starting Point Total: {original_points[player.get_name()]}")
            player.add_card(cut_card)
            ui.display_collection_of_cards(player.get_hand())
            print("-" * 50)
            hand_points = analyze_cribbage_hand.CribbageHandAnalyzer(
                player.get_hand()
            ).count_points()
            print("-" * 50)
            print(f">>> {player.get_name()} got {hand_points} points from hand.")
            print(
                f">>> {player.get_name()} got {player.total_score - original_points[player.get_name()]} points from pegging.\n"
            )
            player.total_score += hand_points
            if player.has_crib():
                print(f"{player.get_name()} Crib")
                print("-" * 50)
                round_crib.add_card_to_crib(cut_card)
                ui.display_collection_of_cards(round_crib.get_crib())
                print("-" * 50)
                crib_points = analyze_cribbage_hand.CribbageHandAnalyzer(
                    round_crib.get_crib()
                ).count_points()
                print("-" * 50)
                print(f">>> {player.get_name()} got {crib_points} points from crib.")
                player.total_score += crib_points
                player.set_crib_status = False
                continue
            crib_player = player.get_name()
            player.set_crib_status = True
        # os.system("cls" if os.name == "nt" else "clear")
        print(f"--> {crib_player} now has the crib.")
        print("")
        print("Score")
        print("-" * 50)
        print(f"{player.get_name()} counts first...")
        first = True
        for player in sorted(updated_players, key=lambda x: x.crib_status):
            print(f"{player.get_name()} has {player.total_score} points.")
            if player.total_score >= 120 and first:
                print(f"{player.get_name()} won!")
                game_running = False
                first = False

        print("-" * 50)


if __name__ == "__main__":
    run_game()

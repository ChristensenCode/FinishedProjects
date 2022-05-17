import numpy as np
from time import time
from pprint import pprint
import pandas as pd

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# How many hands does Player 1 win?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
High Card:          Highest value card.
One Pair:           Two cards of the same value.
Two Pairs:          Two different pairs.
Three of a Kind:    Three cards of the same value.
Straight:           All cards are consecutive values.
Flush:              All cards of the same suit.
Full House:         Three of a kind and a pair.
Four of a Kind:     Four cards of the same value.
Straight Flush:     All cards are consecutive values of same suit.
Royal Flush:        Ten, Jack, Queen, King, Ace, in same suit.
'''
start_time = time()
df = pd.read_csv('Problem_54_data', sep=' ', names=['P1C1', 'P1C2', 'P1C3', 'P1C4', 'P1C5',
                                                    'P2C1', 'P2C2', 'P2C3', 'P2C4', 'P2C5'])
df = df.applymap(tuple)
player_one_hand = df[['P1C1', 'P1C2', 'P1C3', 'P1C4', 'P1C5']]
player_two_hand = df[['P2C1', 'P2C2', 'P2C3', 'P2C4', 'P2C5']]

def card_value(hand_values):
    if isinstance(hand_values, tuple):
        return [x[0] for x in hand_values[1]]
    else:
        return [x[0] for x in hand_values]


def suits(hand_suits):
    if isinstance(hand_suits, tuple):
        return [x[1] for x in hand_suits[1]]
    else:
        return [x[1] for x in hand_suits]


def hand_cleaner(raw_hand):
    face_conversion = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    suit = suits(raw_hand)
    raw_value = card_value(raw_hand)
    value = [face_conversion[x] if x in face_conversion else int(x) for x in raw_value]
    recombined = [(value[x], suit[x]) for x in range(len(value))]
    final_hand = pd.Series(recombined).sort_values()
    return final_hand

def hand_analyzer(player_hand):
    final_hand_dict = {}
    for index, hand in enumerate(player_hand.iterrows()):
        clean_hand = hand_cleaner(hand)
        values = card_value(clean_hand)
        hand_suite = suits(clean_hand)

        suit_types = ['S', 'C', 'H', 'D']
        hand_ranks = {
            'High Card': None,
            'Pair': None,
            'Double Pair': None,
            'Three of a Kind': None,
            'Straight': None,
            'Flush': None,
            'Full House': None,
            'Four of a Kind': None,
            'Straight Flush': None,
            'Royal Flush': None
        }

        hand_score = values[::-1]
        hand_ranks['High Card'] = hand_score
        # Point Checker
        if list(np.diff(values)).count(1) == 4:
            hand_score = 'Straight'
            hand_ranks['Straight'] = values
        for i in range(2, 15):
            if values.count(i) == 4:
                hand_score = 'Four of a Kind'
                hand_ranks['Four of a Kind'] = i
            elif values.count(i) == 3:
                for j in range(2, 15):
                    if values.count(j) == 2 and j != i:
                        hand_score = 'Full House'
                        hand_ranks['Full House'] = (i, j)
                    else:
                        hand_score = 'Three of a Kind'
                        hand_ranks['Three of a Kind'] = i
            elif values.count(i) == 2:
                for j in range(2, 15):
                    if values.count(j) == 2 and j != i:
                        hand_score = 'Double Pairs'
                        hand_ranks['Double Pair'] = (i, j)
                    elif values.count(j) == 2:
                        hand_score = 'Single Pairs'
                        hand_ranks['Pair'] = i
                if hand_ranks['Double Pair'] is not None:
                    hand_ranks['Pair'] = None

        for suit_check in suit_types:
            if hand_suite.count(suit_check) == 5 and sum(np.diff(values)) == 4:
                hand_score = 'Straight Flush'
                hand_ranks['Straight Flush'] = values
            elif hand_suite.count(suit_check) == 5 and values == [10, 11, 12, 13, 14]:
                hand_score = 'Royal Flush'
                hand_ranks['Royal Flush'] = values

        final_hand_dict[index] = (values, hand_ranks)
    return final_hand_dict


player_one_hand_dict = hand_analyzer(player_one_hand)
player_two_hand_dict = hand_analyzer(player_two_hand)
test_1 = []
test_2 = []
for index_value in range(len(player_one_hand_dict)):
    hand_comparing = [
        'High Card',
        'Pair',
        'Double Pair',
        'Three of a Kind',
        'Straight',
        'Flush',
        'Full House',
        'Four of a Kind',
        'Straight Flush',
        'Royal Flush'
    ]
    p1_counter = 0
    p2_counter = 0
    p1_somethings = []
    p2_somethings = []
    for keys in hand_comparing[::-1]:
        p1 = player_one_hand_dict[index_value][1][keys]
        p2 = player_two_hand_dict[index_value][1][keys]
        if p1 is not None:
            p1_somethings.append(p1_counter)
        if p2 is not None:
            p2_somethings.append(p2_counter)
        p1_counter += 1
        p2_counter += 1
    if min(p1_somethings) < min(p2_somethings):
        print('P1 Wins')
        print('P1 Hand --> {}'.format(p1))
        print('P2 Hand --> {}\n'.format(p2))
        test_1.append(1)
    elif min(p1_somethings) > min(p2_somethings):
        print('P2 Wins!')
        print('P1 Hand --> {}'.format(p1))
        print('P2 Hand --> {}\n'.format(p2))
        test_2.append(2)
    else:
        if min(p1_somethings) == 8:
            p1_pair = player_one_hand_dict[index_value][1]['Pair']
            p2_pair = player_two_hand_dict[index_value][1]['Pair']
            if p1_pair > p2_pair:
                print('P1 Wins')
                print('P1 Hand --> {}'.format(p1))
                print('P2 Hand --> {}\n'.format(p2))
                test_1.append(1)
            else:
                print('P2 Wins!')
                print('P1 Hand --> {}'.format(p1))
                print('P2 Hand --> {}\n'.format(p2))
                test_2.append(2)
        else:
            for high_card_1, high_card_2 in zip(p1, p2):
                if high_card_1 > high_card_2:
                    print('P1 Wins!')
                    print('P1 Hand --> {}'.format(p1))
                    print('P2 Hand --> {}\n'.format(p2))
                    test_1.append(1)
                    break
                elif high_card_2 > high_card_1:
                    print('P2 Wins!')
                    print('P1 Hand --> {}'.format(p1))
                    print('P2 Hand --> {}\n'.format(p2))
                    test_2.append(2)
                    break
print('Player 1 wins --> {} Games!'.format(len(test_1)))
print('Player 2 wins --> {} Games!'.format(len(test_2)))
print("The answer is: {}".format(len(test_1)))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
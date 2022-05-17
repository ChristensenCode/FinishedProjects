"""
How many continued fractions for N <= 10,000 have an odd period?
"""

from math import sqrt, floor, gcd
from typing import List
from time import time
from tqdm import tqdm


def shortest_repeated_sequence(input_list: List[int]) -> List[int]:
    for i in range(1, len(input_list)):
        if all(input_list[j] == input_list[j % i] for j in range(i, len(input_list))):
            return input_list[:i]
    return input_list[:]


def find_a_zero(number_to_check: int) -> int:
    return floor(sqrt(number_to_check))


def ignore_perfect_squares(value: int) -> bool:
    if floor(sqrt(value)) ** 2 == value:
        return True
    return False


def determine_loop_count(N: float, numerator: int, denominator: int):
    fraction_value = abs(numerator) / denominator
    above_zero_check = N / denominator
    loop_count = int(1)
    while True:
        check = above_zero_check - (loop_count - fraction_value)
        if check < 0:
            loop_count = loop_count - 1
            break

        loop_count = loop_count + 1
    new_numerator = -round((loop_count - fraction_value) * denominator)
    return int(loop_count), int(new_numerator)


def determine_pull_out_value(
    N: float, numerator: int, denominator: int, first_round: bool = False
):
    if first_round:
        loop_count, new_numerator = determine_loop_count(N, numerator, denominator)
        return loop_count, new_numerator, denominator

    # subsequent rounds
    updated_denominator = round(N ** 2 - numerator ** 2)
    updated_numerator = numerator * denominator
    common_denominator = gcd(updated_numerator, denominator)
    gcd_denom = int(updated_denominator / common_denominator)
    gcd_num = int(updated_numerator / common_denominator)
    loop_count, new_numerator = determine_loop_count(N, int(gcd_num), int(gcd_denom))

    return loop_count, new_numerator, gcd_denom


def main():
    total_odd_periods = 0
    max_pattern = 0
    for N in tqdm(range(2, 10001)):
        if ignore_perfect_squares(N):
            continue
        rooted_n = sqrt(N)
        starting_point = find_a_zero(N)
        denominator = N - starting_point ** 2
        sequence, numerator, denominator = determine_pull_out_value(
            rooted_n, starting_point, denominator, True
        )

        possible_pattern = []
        while True:
            sequence, numerator, denominator = determine_pull_out_value(
                rooted_n, numerator, denominator
            )

            possible_pattern.append(sequence)
            check_pattern = shortest_repeated_sequence(possible_pattern)
            if len(possible_pattern) > 225 and check_pattern:
                pattern_length = len(check_pattern)
                if pattern_length > max_pattern:
                    max_pattern = pattern_length
                if pattern_length % 2 != 0:
                    total_odd_periods += 1
                break
    return total_odd_periods


if __name__ == "__main__":
    start_time = time()
    answer = main()
    print("The answer is: {}".format(answer))
    elapsed_time = time() - start_time
    print("The answer was found in {0:.4f} s.".format(elapsed_time))

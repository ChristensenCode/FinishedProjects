"""
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
https://en.wikipedia.org/wiki/Continued_fraction
"""
from typing import List
from time import time


h_values = [2, 3, 8]
k_values = [1, 1, 3]


def calculate_numerator(a_s: int, h_s: List[int], index: int) -> int:
    return a_s * h_s[index - 1] + h_s[index - 2]


def calculate_denominator(a_s: int, k_s: List[int], index: int) -> int:
    return a_s * k_s[index - 1] + k_s[index - 2]


def main_loop() -> int:
    k = 1
    for index in range(3, 100):
        new_a = 1
        if (index - 2) % 3 == 0:
            k += 1
            new_a = k * 2
        h_n = calculate_numerator(new_a, h_values, index)
        h_values.append(h_n)
        k_n = calculate_denominator(new_a, k_values, index)
        k_values.append(k_n)
        if index + 1 != 100:
            continue
        return h_n


def get_sum_from_integer(starting_value: int) -> int:
    starting_value = list(str(starting_value))
    list_of_strings_to_ints = map(int, starting_value)
    return sum(list_of_strings_to_ints)


if __name__ == "__main__":
    start_time = time()
    final_numerator = main_loop()
    final_answer = get_sum_from_integer(final_numerator)
    print("The answer is: {}".format(final_answer))
    elapsed_time = time() - start_time
    print("The answer was found in {0:.4f} s.".format(elapsed_time))

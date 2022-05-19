"""
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
661
778
"""
import math
from numba import njit, prange
from numba.typed import List
from time import time
import numpy as np


def another_tight_loop(D):
    n = 0
    D = int(D)
    r = math.sqrt(D)
    a_values = []
    q_list = [1]
    Q_list = [1]
    p_list = []
    P_list = [0]
    while True:
        # Calculates the Continued fraction
        # https://proofwiki.org/wiki/Continued_Fraction_Expansion_of_Irrational_Square_Root/Examples/61
        new_a = int((int(r) + P_list[-1]) / Q_list[-1])
        a_values.append(new_a)
        new_P = a_values[-1] * Q_list[-1] - P_list[-1]
        P_list.append(new_P)
        new_Q = (D - P_list[-1] ** 2) / Q_list[-1]
        Q_list.append(new_Q)

        # Calculates the fundamental solution
        # https://mathworld.wolfram.com/PellEquation.html
        if n == 0:
            n += 1
            continue

        elif n == 1:
            a_0 = a_values[0]
            a_1 = a_values[1]
            q_list.append(a_1)
            p_list.append(a_0)
            p_list.append(a_0 * a_1 + 1)
            n += 1
            if p_list[-1] * p_list[-1] - D * q_list[-1] * q_list[-1] == 1.0:
                return p_list[-1]
            continue
        new_q = a_values[n] * q_list[n - 1] + q_list[n - 2]
        new_p = a_values[n] * p_list[n - 1] + p_list[n - 2]
        q_list.append(new_q)
        p_list.append(new_p)
        if p_list[-1] * p_list[-1] - D * q_list[-1] * q_list[-1] == 1:
            return p_list[-1]
        n += 1


def another_main():
    non_perfects = filter(lambda x: not math.sqrt(x).is_integer(), range(2, 1001))
    x_s = {}
    for non_perfect in non_perfects:
        x_s[non_perfect] = another_tight_loop(non_perfect)
    return max(x_s, key=x_s.get)


if __name__ == "__main__":
    start_time = time()
    answer = another_main()
    print("The answer is: {}".format(answer))
    elapsed_time = time() - start_time
    print("The answer was found in {0:.4f} s.".format(elapsed_time))

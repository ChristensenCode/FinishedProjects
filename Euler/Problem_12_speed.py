from time import time
import numpy as np
from math import sqrt
from functools import reduce

from numba import njit


@njit(fastmath=True)
def generate_tri_number(sequence_number):
    return np.sum(np.arange(1, sequence_number + 1))


def factors(n):
    step = 2 if n % 2 else 1
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0),
        )
    )


triangle_value = generate_tri_number(7)
factor_number = 0
guess_value = 1
start_time = time()
while factor_number < 500:
    triangle_value = generate_tri_number(guess_value)
    triangle_factors = factors(triangle_value)
    factor_number = len(triangle_factors)
    guess_value += 2
elapsed_time = time() - start_time
print(f"Total Time {elapsed_time}")
print(f"The answer is {triangle_value}.")

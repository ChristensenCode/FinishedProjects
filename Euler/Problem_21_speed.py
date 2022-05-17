from time import time
from numba import njit, prange
import numpy as np
import pandas as pd
from functools import reduce
from math import sqrt


def factors(n):
    step = 2 if n % 2 else 1
    return sum(sorted(list(set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))))[:-1])


@njit
def factors_two(n):
    values = []
    step = 2 if n % 2 else 1
    for i in range(1, int(sqrt(n)), step):
        if n % i == 0:
            values.extend([i, n // i])
    try:
        values.remove(n)
    except:
        pass
    total = 0
    for j in values:
        total += j
    return total


start_time = time()
possibles = []
for i in prange(1, 10001):
    iter_one = factors_two(i)
    iter_two = factors_two(iter_one)
    if iter_one == iter_two:
        continue
    elif i == iter_two:
        possibles.extend([iter_one, iter_two])
elapsed_time = time() - start_time
print(f'Total Time {elapsed_time}')
answer = sum(set(possibles))
print(f"The answer is {answer}.")

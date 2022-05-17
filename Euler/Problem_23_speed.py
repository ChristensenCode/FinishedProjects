from numba import njit
from math import sqrt, ceil
from time import time
import numpy as np
import pandas as pd


@njit
def factors(n):
    values = []
    step = 2 if n % 2 else 1
    for i in range(1, ceil(sqrt(n)), step):
        if n % i == 0:
            values.extend([i, n // i])
    try:
        values.remove(n)
    except:
        pass
    total = 0
    for j in values:
        total += j
    return sorted(values), total


start_time = time()
j = 0
abundant_values = []
for i in range(28124):
    if factors(i)[1] > i:
        abundant_values.append(i)

abundant_values_set = set(abundant_values)
abundant_values_array = np.array(abundant_values)
one_abundant_values_array = np.ones_like(abundant_values_array)

non_sum = []
breaker = 1
for abundant_value in abundant_values:
    comparison = abundant_values_array + one_abundant_values_array * abundant_value
    divisor = comparison / abundant_value
    df = pd.DataFrame(
        {
            "abundant": abundant_values_array,
            "abundant_value": one_abundant_values_array * abundant_value,
            "comparison": comparison,
            "divisor": divisor,
        }
    )
    # if breaker > 1:
    # break
    # breaker += 1

print(df)
print((non_sum))
elapsed_time = time() - start_time
print(f"Total Time {elapsed_time}")

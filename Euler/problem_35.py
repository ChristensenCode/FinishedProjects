import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# How many circular primes are there below one million?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3 :: 2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3 :: 2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]


counter = 0
possible_primes = primesfrom2to(1000000)
rotation_primes = []
prime_set = set(possible_primes)

for value in possible_primes:
    value = str(value)
    value_length = len(value)
    rotated_value = value[value_length - 1 :] + value[: value_length - 1]
    possible_solution = set()
    for N in rotated_value:
        rotated_value = (
            rotated_value[value_length - 1 :] + rotated_value[: value_length - 1]
        )
        possible_solution.add(int(rotated_value))
    if possible_solution.issubset(prime_set):
        counter += 1
elapsed_time = time() - start_time
print("Compute Time: " + str(elapsed_time) + " seconds")
print("Answer: " + str(counter))

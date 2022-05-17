import numpy as np
from time import time
import re
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Find the sum of the only eleven primes that are both
# truncatable from left to right and right to left.
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


possible_primes = primesfrom2to(1000000)
prime_length = len(possible_primes)
winners = []

for i in possible_primes:
    string_prime = str(i)
    primers_left = []
    primers_right = []
    for j in range(len(string_prime)):
        shortened_left = string_prime[j:]
        zero_checker = re.compile("[0].*")
        if re.search(zero_checker, shortened_left):
            break
        integer_shortened = int(shortened_left)
        primers_left.append(integer_shortened)
        primers_set = set(primers_left)
    possible_primes_set = set(possible_primes)
    if possible_primes_set.issuperset(primers_set) and len(primers_left) > 0:
        winners.append(i)
print(winners)

cleaner = []
for i in winners:
    string_prime = str(i)
    primers_left = []
    primers_right = []

    for j in range(len(string_prime)):
        shortened_left = string_prime[: -j - 1]
        if len(shortened_left) == 0:
            continue
        zero_checker = re.compile("[0].*")
        if re.search(zero_checker, shortened_left):
            break
        integer_shortened = int(shortened_left)
        primers_left.append(integer_shortened)
        primers_set = set(primers_left)
    possible_primes_set = set(possible_primes)
    if possible_primes_set.issuperset(primers_set) and len(primers_left) > 0:
        cleaner.append(i)
print(cleaner)
print("The answer is {}.".format(sum(cleaner)))
elapsed_time = time() - start_time
print("The answer was found in {0:.4f} s.".format(elapsed_time))

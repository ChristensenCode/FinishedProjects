import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3 :: 2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3 :: 2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]


start_time = time()
prime_list = primesfrom2to(1000000)

# This solution would work, but it would take days to find the answer.
max_value = [[0], [0]]
max_prime_value = max(prime_list)
for i in range(0, len(prime_list)):
    for k in range(i + 1, len(prime_list) + 1):
        prime_slice = prime_list[i:k]
        if sum(prime_slice) < max_prime_value:
            if len(prime_slice) > len(max_value[1]) and sum(prime_slice) in prime_list:
                max_value[0] = sum(prime_slice)
                max_value[1] = prime_slice
        else:
            break

print("The answer is {} and contains {} terms.".format(max_value[0], len(max_value[1])))
elapsed_time = time() - start_time
print("The answer was found in {0:.4f} s.".format(elapsed_time))


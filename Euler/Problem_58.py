import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# what is the side length of the square spiral for which
# the ratio of primes along both diagonals first falls below 10%?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2, 3, ((3*np.nonzero(sieve)[0][1:]+1)|1)]


possible_primes = set(primesfrom2to(1000000000))
length = 3
corner_values = []
while True:
    corners = [
        length ** 2,
        length ** 2 - length + 1,
        length ** 2 - 2 * length + 2,
        length ** 2 - 3 * length + 3
    ]

    corner_list = corner_values.extend(corners)
    corner_set = set(corner_values)
    common_values = corner_set.intersection(possible_primes)
    all_corners = len(corner_values)+1
    number_of_matches = len(common_values)
    percentage = number_of_matches/all_corners

    if percentage < 0.1:
        break
    length += 2

print("The answer is: {}".format(length))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))

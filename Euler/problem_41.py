import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# What is the largest n-digit pandigital prime that exists?
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
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]


value = primesfrom2to(10000000)
value = value[4:]

pandigital_list = [str(i) for i in range(1, 10)]
possibles = []
for i in value:
    prime_string = str(i)
    pandigital_comparison = pandigital_list[:len(prime_string)]
    pandigital_sorted = sorted(prime_string)
    if pandigital_comparison == pandigital_sorted:
        possibles.append(i)

elapsed_time = time() - start_time
print('The answer is {}.'.format(max(possibles)))
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
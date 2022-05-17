import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# What is the smallest odd composite that cannot be
# written as the sum of a prime and twice a square?
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

prime_list = primesfrom2to(10000)
prime_array = np.asarray(prime_list)
squarer = np.arange(1, 1000)
starter_array = np.array([])
for i in prime_list:
    primer = np.zeros_like(squarer)
    primer.fill(i)

    value = primer + np.multiply(np.square(squarer), 2)
    value[value % 2 == 0] = 0
    starter_array = np.concatenate((starter_array, value))

cleaned_array = np.sort(starter_array)
lister = cleaned_array.tolist()
lister_set = set(lister)
odd_numbers = set([i for i in range(1, 10000, 2)])
final = odd_numbers - lister_set - set(prime_list)
print('The answer is {}'.format(list(final)[1]))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))

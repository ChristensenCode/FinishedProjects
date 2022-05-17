from time import time
import numpy as np
from pprint import pprint

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

list_of_primes = primesfrom2to(1000)
list_of_possibles = [x for x in range(2, 200000)]
prime_removal = set(list_of_possibles) - set(list_of_primes)
smaller_list = sorted(list(prime_removal))
answer = []
factors = []
counter = 0
for i in smaller_list:
    smaller_list_array = np.ones_like(list_of_primes) * i
    factor_finder = smaller_list_array % list_of_primes
    zero_locations = np.where(factor_finder == 0)[0]

    prime_factors = list_of_primes[zero_locations]
    unique_count = np.count_nonzero(factor_finder == 0)

    if unique_count == 4:
        answer.append(i)
        factors.append(list(prime_factors))
        counter += 1
        if counter == 4:
            break
    else:
        counter = 0
        answer = []
        factors = []

print('The answer is {}'.format(answer[0]))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))

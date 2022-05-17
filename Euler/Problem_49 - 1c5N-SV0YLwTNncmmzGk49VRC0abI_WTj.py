import numpy as np
from time import time
from pprint import pprint
from itertools import permutations

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# What 12-digit number do you form by concatenating the three terms in this sequence?
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

list_of_primes = primesfrom2to(10000)
shortened_list = list_of_primes[168:]
shortened_list_set = set(shortened_list)
answer_dict = {}
# print(list_of_primes[168:])
for i in shortened_list:
    stringer = str(i)
    if '0' in stringer:
        continue
    j = permutations(stringer)
    x = [int(''.join(y)) for y in j]

    z = sorted(list(set(x).intersection(shortened_list_set)))
    for value in range(len(z)):
        for value2 in range(len(z)):
            check = (z[value2] + z[value])/2
            if check in z and check != z[value]:
                answer_dict[i] = sorted(list(set([z[value], int(check), z[value2]])))

string_convert = [str(value) for value in answer_dict[9629]]
final_answer = [''.join(string_convert)]

print('The answer is {}'.format(final_answer[0]))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))


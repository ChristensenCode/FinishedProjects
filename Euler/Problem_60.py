from itertools import product, permutations, combinations


import numpy as np
import pandas as pd
from time import time
from pprint import pprint
import pyglet


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
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

total_primes = primesfrom2to(30000)
total_primes_string = list(np.char.mod('%d', total_primes))

primes_check = primesfrom2to(100000000)
primes_check_string = set(np.char.mod('%d', primes_check))

test_list = [3, 7, 109, 673]
answer = [13, 5197, 5701, 6733, 8389]
dict = {}
for pass_one in total_primes_string:
    values = []

    for pass_two in total_primes_string:
        after_value = pass_one + pass_two
        before_value = pass_two + pass_one
        if before_value in primes_check_string and after_value in primes_check_string:
            values.append(pass_two)
    dict[(pass_one)] = values
# pprint(dict)

second_dict = {}
for key, value in dict.items():
    for pass_one in value:
        values = []
        for pass_two in value:
            after_value = pass_one + pass_two
            before_value = pass_two + pass_one
            if before_value in primes_check_string and after_value in primes_check_string:
                values.append(pass_two)
        if len(values) > 0:
            second_dict[(key, pass_one)] = values
        else:
            break
# pprint(second_dict)

third_dict = {}
for key, value in second_dict.items():
    # print(key)
    for pass_one in value:
        values = []
        for pass_two in value:
            after_value = pass_one + pass_two
            before_value = pass_two + pass_one
            if before_value in primes_check_string and after_value in primes_check_string:
                values.append(pass_two)
        if len(values) > 0:
            third_dict[tuple(list(key) + [pass_one])] = values
        else:
            break

fourth_dict = {}
for key, value in third_dict.items():
    # print(key)
    for pass_one in value:
        values = []
        for pass_two in value:
            after_value = pass_one + pass_two
            before_value = pass_two + pass_one
            if before_value in primes_check_string and after_value in primes_check_string:
                values.append(pass_two)
        if len(values) > 0:
            fourth_dict[tuple(list(key) + [pass_one])] = values
        else:
            break
# pprint(fourth_dict)
test_numpy = np.empty(shape=(len(fourth_dict), 5))
counter = 0
for key, value in fourth_dict.items():
    final_list = sorted(list(key) + value)
    test_numpy[counter] = np.array(final_list)
    counter += 1
final = sum(list(np.unique(test_numpy)))
print("The answer is: {}".format(final))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))

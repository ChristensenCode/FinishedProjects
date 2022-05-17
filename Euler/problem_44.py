import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Find the pair of pentagonal numbers, Pj and Pk,
# for which their sum and difference are pentagonal
# and D = |Pk − Pj| is minimised; what is the value of D?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
pentagonal_values = [i * (3 * i - 1) / 2 for i in range(1, 2500)]
print(pentagonal_values)
counter = 1
for i in pentagonal_values:
    inner_counter = 1
    for j in pentagonal_values[counter:]:
        if i + j in pentagonal_values:
            if j - i in pentagonal_values:
                print(i)
                print(j)
                print('The answer is {}'.format(j-i))
                break
        inner_counter += 1
    counter += 1

elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))

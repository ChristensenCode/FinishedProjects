import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Find the sum of all numbers, less than one million,
# which are palindromic in base 10 and base 2.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
total = []
for i in range(1, 1000000):
    binary_number = str(bin(i))[2:]

    if binary_number == binary_number[::-1] and str(i) == str(i)[::-1]:
        total.append(i)

answer = sum(total)
print("The answer is {}.".format(answer))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
